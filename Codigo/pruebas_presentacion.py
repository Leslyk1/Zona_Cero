"""Regresiones de la presentación sobre el bucle real, con reloj controlado."""
import ast
import copy
import os
from pathlib import Path
import random
import unittest
from unittest.mock import patch

os.environ["SDL_VIDEODRIVER"] = "dummy"
os.environ["SDL_AUDIODRIVER"] = "dummy"
import pygame
import inicio
import interfaz
from batalla import dibujar_batalla, BOTONES_COMBATE
from arte import sprite


class PruebasPresentacion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ruta = Path(__file__).with_name("main.py")
        arbol = ast.parse(ruta.read_text(encoding="utf-8"))
        bucle = next(n for n in arbol.body if isinstance(n, ast.While))
        cls.inicializar = compile(ast.Module(body=arbol.body[:arbol.body.index(bucle)],
                                            type_ignores=[]), str(ruta), "exec")
        paso = ast.While(test=ast.Constant(True), body=bucle.body + [ast.Break()], orelse=[])
        cls.fotograma = compile(ast.fix_missing_locations(ast.Module(body=[paso], type_ignores=[])),
                                str(ruta), "exec")

    def setUp(self):
        self.ahora = 10000
        reloj = patch("pygame.time.get_ticks", side_effect=lambda: self.ahora)
        reloj.start()
        self.addCleanup(reloj.stop)
        self.ns = {"__name__": "prueba_presentacion"}
        with patch.object(inicio, "mostrar_inicio", return_value=True):
            exec(self.inicializar, self.ns)
        self.ns["inicio_fundido"] = 0
        self.addCleanup(self.ns["audio_juego"].detener)

    def frame(self, *teclas, eventos=()):
        entradas = [pygame.event.Event(pygame.KEYDOWN, key=k) for k in teclas]
        with patch("pygame.event.get", return_value=entradas + list(eventos)):
            exec(self.fotograma, self.ns)

    def ir(self, zona, x, y):
        self.ns["automata"].forzar_estado(zona, "PRUEBA")
        self.ns["jugador"].cambiar_posicion(x, y)

    def test_espacio_revela_sin_volver_a_ejecutar_misiones(self):
        for nombre, zona, posicion in (("elena", "HOSPITAL", (630, 220)),
                                       ("marcos", "COMISARIA", (160, 220))):
            with self.subTest(npc=nombre):
                self.ns["zombi_comisaria"].vivo = False
                self.ir(zona, *posicion)
                npc = self.ns[nombre]
                with patch.object(npc, "hablar", wraps=npc.hablar) as hablar:
                    self.frame(pygame.K_e)
                    ui = self.ns["dialogo_ui"]
                    self.assertEqual(ui.personaje, nombre)
                    self.ahora += 280
                    self.frame()
                    self.assertEqual(ui.cantidad_visible(), 10)
                    estado = copy.deepcopy([self.ns[k].__dict__ for k in
                                            ("inventario", "mision_medicamentos", "mision_radio")])
                    self.frame(pygame.K_SPACE)
                    self.assertFalse(ui.escribiendo)
                    self.assertFalse(self.ns["audio_juego"].leyendo_dialogo)
                    hablar.assert_called_once()
                    self.assertEqual(estado, [self.ns[k].__dict__ for k in
                                            ("inventario", "mision_medicamentos", "mision_radio")])

    def test_texto_se_pausa_en_diario_y_menu_y_se_limpia_al_salir(self):
        self.ir("HOSPITAL", 630, 220)
        self.frame(pygame.K_e)
        self.ahora += 280
        self.frame(pygame.K_j)
        ui = self.ns["dialogo_ui"]
        self.ahora += 5000
        self.frame()
        self.assertEqual(ui.cantidad_visible(), 10)
        self.frame(pygame.K_j)
        self.assertEqual(ui.cantidad_visible(), 10)
        def pausa(*args, **kwargs):
            self.ahora += 5000
            return True
        with patch.dict(self.ns, mostrar_inicio=pausa):
            self.frame(pygame.K_ESCAPE)
        self.assertEqual(ui.cantidad_visible(), 10)
        self.ir("CALLE", 480, 500)
        self.frame()
        self.assertIsNone(ui.personaje)

    def test_aviso_solo_cerca_y_sin_paneles_superpuestos(self):
        with patch("interfaz.indicador_interaccion", wraps=interfaz.indicador_interaccion) as aviso:
            self.ir("HOSPITAL", 630, 220)
            self.frame()
            self.assertEqual(aviso.call_count, 1)
            self.assertEqual(aviso.call_args.args[-1], "E - Hablar con Elena")
            aviso.reset_mock()
            self.frame(pygame.K_j)
            aviso.assert_not_called()
            self.frame(pygame.K_j)
            aviso.reset_mock()
            self.ir("HOSPITAL", 480, 340)
            self.frame()
            aviso.assert_not_called()

    def test_dialogos_caducan_sin_salir_y_se_pueden_repetir(self):
        for nombre, zona, posicion in (("elena", "HOSPITAL", (630, 220)),
                                       ("marcos", "COMISARIA", (160, 220))):
            with self.subTest(npc=nombre):
                self.ns["zombi_comisaria"].vivo = False
                self.ir(zona, *posicion)
                self.frame(pygame.K_e)
                ui = self.ns["dialogo_ui"]
                estado = copy.deepcopy([self.ns[k].__dict__ for k in
                                        ("inventario", "mision_medicamentos", "mision_radio")])
                self.ahora = ui.fin_escritura - 1
                self.frame()
                self.assertTrue(ui.escribiendo)
                self.ahora = ui.fin_escritura + ui.TIEMPO_LECTURA - 1
                self.frame()
                self.assertEqual(ui.personaje, nombre)
                self.assertTrue(self.ns["dialogo_actual"])
                self.ahora += 1
                self.frame()
                self.assertEqual(self.ns["dialogo_actual"], "")
                self.assertIsNone(ui.personaje)
                self.assertFalse(self.ns["audio_juego"].leyendo_dialogo)
                self.assertEqual(self.ns["automata"].estado_actual, zona)
                self.assertEqual(estado, [self.ns[k].__dict__ for k in
                                        ("inventario", "mision_medicamentos", "mision_radio")])
                self.ahora += 10000
                self.frame()
                self.assertEqual(self.ns["dialogo_actual"], "")
                self.frame(pygame.K_e)
                self.assertEqual(ui.personaje, nombre)
                self.assertTrue(ui.escribiendo)

    def test_espacio_conserva_cuatro_segundos_para_leer(self):
        self.ir("HOSPITAL", 630, 220)
        self.frame(pygame.K_e)
        self.ahora += 280
        self.frame(pygame.K_SPACE)
        self.ahora += 3999
        self.frame()
        self.assertEqual(self.ns["dialogo_ui"].personaje, "elena")
        self.ahora += 1
        self.frame()
        self.assertEqual(self.ns["dialogo_actual"], "")

    def test_tiempo_de_lectura_se_detiene_en_diario_glc_y_pausa(self):
        self.ir("HOSPITAL", 630, 220)
        for tecla in (pygame.K_j, pygame.K_g, pygame.K_ESCAPE):
            with self.subTest(panel=tecla):
                self.frame(pygame.K_e, pygame.K_SPACE)
                self.ahora += 3000
                if tecla == pygame.K_ESCAPE:
                    def pausa(*args, **kwargs):
                        self.ahora += 12000
                        return True
                    with patch.dict(self.ns, mostrar_inicio=pausa):
                        self.frame(tecla)
                else:
                    self.frame(tecla)
                    self.ahora += 12000
                    self.frame()
                    self.assertEqual(self.ns["dialogo_ui"].personaje, "elena")
                    self.frame(tecla)
                self.ahora += 999
                self.frame()
                self.assertEqual(self.ns["dialogo_ui"].personaje, "elena")
                self.ahora += 1
                self.frame()
                self.assertEqual(self.ns["dialogo_actual"], "")

    def test_caducidad_no_borra_un_aviso_que_reemplaza_al_npc(self):
        self.ir("HOSPITAL", 630, 220)
        self.frame(pygame.K_e)
        aviso = "Has recogido un medicamento."
        self.ns["dialogo_actual"] = aviso
        self.frame()
        self.ahora += 20000
        self.frame()
        self.assertIsNone(self.ns["dialogo_ui"].personaje)
        self.assertEqual(self.ns["dialogo_actual"], aviso)

    def test_clics_en_los_tres_botones_en_cuatro_tamanos(self):
        inv, combate = self.ns["inventario"], self.ns["combate"]
        inv.agregar("Pistola")
        inv.agregar("Balas", 20)
        self.ir("COMISARIA", 480, 500)
        for tamano in ((1200, 780), (1920, 1080), (800, 600), (500, 850)):
            self.ns["pantalla"] = pygame.display.set_mode(tamano, pygame.RESIZABLE)
            self.frame(eventos=[pygame.event.Event(pygame.VIDEORESIZE, size=tamano, w=tamano[0], h=tamano[1])])
            for indice, estado in enumerate(("ATACANDO", "DISPARANDO", "DEFENDIENDO")):
                with self.subTest(tamano=tamano, accion=estado):
                    combate.terminar()
                    self.ns["zombi_comisaria"].reiniciar()
                    combate.iniciar(self.ns["zombi_comisaria"], self.ns["jugador"])
                    cx, cy = BOTONES_COMBATE[indice].center
                    escala, (x, y) = self.ns["escala_interfaz"], self.ns["posicion_interfaz"]
                    pos = (round(x + cx * escala), round(y + (cy + 70) * escala))
                    self.frame(eventos=[pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=pos)])
                    self.assertEqual(combate.estado, estado)

    def test_efectos_no_modifican_estado_azar_ni_sprites(self):
        c, j, inv = self.ns["combate"], self.ns["jugador"], self.ns["inventario"]
        c.iniciar(self.ns["zombi_comisaria"], j)
        inv.agregar("Pistola")
        inv.agregar("Balas", 4)
        for estado, objetivo, dano, resultado in (
                ("ATACANDO", "enemigo", 20, "CRITICO"),
                ("DISPARANDO", "enemigo", 0, "FALLO"),
                ("DEFENDIENDO", "escudo", 0, "GUARDIA"),
                ("TURNO_ENEMIGO", "jugador", 7, "BLOQUEO"),
                ("TURNO_ENEMIGO", "jugador", 0, "ESQUIVE")):
            c.estado, c.objetivo_animacion, c.dano_animacion = estado, objetivo, dano
            c.resultado_actual = resultado
            c.transicion = "TURNO_ENEMIGO -> " + resultado
            c.inicio_fase = self.ahora - 110
            antes = copy.deepcopy((c.__dict__, j.__dict__, inv.__dict__))
            azar = random.getstate()
            pixeles = pygame.image.tostring(sprite("superviviente", True), "RGBA")
            dibujar_batalla(self.ns["ventana"], c, j, inv)
            despues = copy.deepcopy((c.__dict__, j.__dict__, inv.__dict__))
            # Los enemigos son objetos: comparar sus datos, no su identidad.
            antes[0]["enemigo"] = antes[0]["enemigo"].__dict__
            despues[0]["enemigo"] = despues[0]["enemigo"].__dict__
            self.assertEqual(antes, despues)
            self.assertEqual(azar, random.getstate())
            self.assertEqual(pixeles, pygame.image.tostring(sprite("superviviente", True), "RGBA"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
