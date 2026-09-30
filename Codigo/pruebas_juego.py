"""Regresiones de combate y misiones: ejecutar con python Codigo/pruebas_juego.py."""
import unittest
from unittest.mock import patch
from combate import Combate
from enemigo import ZombiPolicia, ZombiCorredor
from jugador import Jugador
from inventario import Inventario
from mision import Mision, DiarioMisiones
from finales import SistemaFinales


class PruebasCombate(unittest.TestCase):
    def setUp(self):
        # Diego: controlar el reloj y el azar hace las pruebas reproducibles,
        # sin esperar animaciones ni depender de ganar por suerte.
        self.ahora = 100
        self.reloj = patch('combate.pygame.time.get_ticks', side_effect=lambda: self.ahora)
        self.reloj.start()
        self.addCleanup(self.reloj.stop)
        self.jugador = Jugador()
        self.enemigo = ZombiCorredor()
        self.inventario = Inventario()
        self.combate = Combate()
        self.combate.iniciar(self.enemigo, self.jugador)

    def avanzar(self, ms):
        self.ahora += ms
        self.combate.actualizar(self.jugador)

    def test_ataque_y_respuesta_separados_y_bloqueo_de_repeticion(self):
        with patch('combate.random.randint', return_value=50):
            self.combate.golpear(self.jugador)
            self.assertEqual(self.enemigo.vida, 60)
            self.assertEqual(self.jugador.vida, 100)
            self.assertEqual(self.combate.estado, 'ATACANDO')
            self.combate.golpear(self.jugador)
            self.combate.disparar(self.jugador, self.inventario)
            self.assertEqual(self.enemigo.vida, 60)
            self.avanzar(849)
            self.assertEqual(self.jugador.vida, 100)
            self.avanzar(1)
            self.assertEqual(self.combate.estado, 'TURNO_ENEMIGO')
            self.assertEqual(self.jugador.vida, 85)
            self.avanzar(1000)
            self.assertEqual(self.combate.estado, 'ELEGIR_ACCION')
            self.assertEqual(self.combate.turno, 2)

    def test_limites_golpe(self):
        for valor, esperado in ((1,20), (20,20), (21,10), (85,10), (86,0), (100,0)):
            with self.subTest(valor=valor), patch('combate.random.randint', return_value=valor):
                combate = Combate()
                enemigo = ZombiCorredor()
                combate.iniciar(enemigo, self.jugador)
                combate.golpear(self.jugador)
                self.assertEqual(enemigo.vida, 70-esperado)

    def test_disparo_requiere_arma_y_municion(self):
        self.combate.disparar(self.jugador, self.inventario)
        self.assertEqual(self.combate.estado, 'ELEGIR_ACCION')
        self.inventario.agregar('Pistola')
        self.combate.disparar(self.jugador, self.inventario)
        self.assertEqual(self.combate.estado, 'ELEGIR_ACCION')
        self.assertEqual(self.combate.turno, 1)
        self.assertEqual(self.enemigo.vida, 70)

    def test_limites_disparo_y_consumo_incluso_si_falla(self):
        for valor, esperado in ((1,30), (30,30), (31,20), (90,20), (91,0), (100,0)):
            with self.subTest(valor=valor), patch('combate.random.randint', return_value=valor):
                combate, enemigo, inv = Combate(), ZombiCorredor(), Inventario()
                inv.agregar('Pistola')
                inv.agregar('Balas', 2)
                combate.iniciar(enemigo, self.jugador)
                combate.disparar(self.jugador, inv)
                self.assertEqual(enemigo.vida, 70-esperado)
                self.assertEqual(inv.obtener_cantidad('Balas'), 1)
                combate.disparar(self.jugador, inv)
                self.assertEqual(inv.obtener_cantidad('Balas'), 1)

    def test_defender_reduce_dano_y_puede_esquivar(self):
        for valor, dano in ((30,0), (31,7), (100,7)):
            with self.subTest(valor=valor), patch('combate.random.randint', return_value=valor):
                self.combate = Combate()
                self.jugador.vida = 100
                self.combate.iniciar(self.enemigo, self.jugador)
                self.combate.defender(self.jugador)
                self.assertEqual(self.jugador.vida, 100)
                self.avanzar(850)
                self.assertEqual(self.jugador.vida, 100-dano)
                self.avanzar(1000)
                self.assertEqual(self.combate.estado, 'ELEGIR_ACCION')

    def test_victoria_no_permite_contraataque(self):
        self.enemigo.vida = 10
        with patch('combate.random.randint', return_value=50):
            self.combate.golpear(self.jugador)
            self.avanzar(850)
            self.assertEqual(self.combate.estado, 'VICTORIA')
            self.avanzar(10000)
            self.assertEqual(self.jugador.vida, 100)

    def test_derrota_se_confirma_despues_de_la_respuesta(self):
        self.jugador.vida = 5
        with patch('combate.random.randint', return_value=50):
            self.combate.defender(self.jugador)
            self.avanzar(850)
            self.assertEqual(self.jugador.vida, 0)
            self.assertEqual(self.combate.estado, 'TURNO_ENEMIGO')
            self.avanzar(1000)
            self.assertEqual(self.combate.estado, 'DERROTA')

    def test_barras_y_limpieza_no_alteran_vida(self):
        self.jugador.vida = 37
        for _ in range(90):
            self.combate.actualizar(self.jugador)
        self.assertEqual(self.jugador.vida, 37)
        self.assertEqual(self.combate.vida_visible_jugador, 37)
        self.combate.terminar()
        self.assertFalse(self.combate.activo)
        self.assertIsNone(self.combate.enemigo)


class PruebasDiario(unittest.TestCase):
    def setUp(self):
        self.mision = Mision('Medicinas perdidas', 'Busca medicamentos')
        self.inv = Inventario()
        self.policia = ZombiPolicia()
        self.corredor = ZombiCorredor()
        self.diario = DiarioMisiones()

    def actualizar(self):
        self.diario.actualizar(self.mision, self.inv, self.policia, self.corredor)

    def test_progreso_paso_a_paso_y_misiones_completadas(self):
        self.actualizar()
        self.assertEqual(self.diario.porcentaje, 0)
        self.mision.activar()
        self.actualizar()
        self.assertEqual(self.diario.porcentaje, 20)
        self.inv.agregar('Medicamento')
        self.actualizar()
        self.assertEqual(self.diario.porcentaje, 40)
        self.mision.completar()
        self.actualizar()
        self.assertEqual(self.diario.porcentaje, 60)
        self.assertEqual(self.diario.completadas, 1)
        self.policia.recibir_dano(40)
        self.actualizar()
        self.assertEqual(self.diario.porcentaje, 80)
        self.corredor.recibir_dano(70)
        self.actualizar()
        self.assertEqual(self.diario.porcentaje, 100)
        self.assertEqual(self.diario.completadas, 3)
        self.assertIn('evacuación', self.diario.siguiente)

    def test_recoger_medicina_antes_de_hablar_no_completa_mision(self):
        self.inv.agregar('Medicamento')
        self.actualizar()
        self.assertEqual(self.diario.porcentaje, 20)
        self.assertEqual(self.diario.completadas, 0)
        self.assertEqual(self.diario.siguiente, 'Habla con Elena')

    def test_diario_coincide_con_requisitos_de_evacuacion(self):
        finales = SistemaFinales()
        for medicina in (False, True):
            for policia in (False, True):
                for corredor in (False, True):
                    with self.subTest(medicina=medicina, policia=policia, corredor=corredor):
                        self.mision.completada = medicina
                        self.policia.vivo = not policia
                        self.corredor.vivo = not corredor
                        self.actualizar()
                        self.assertEqual(self.diario.completadas == 3,
                                         finales.requisitos_completos(self.mision, self.policia, self.corredor))

    def test_abrir_diario_no_modifica_el_mundo(self):
        self.inv.agregar('Balas', 12)
        for _ in range(20):
            self.actualizar()
        self.assertEqual(self.inv.obtener_cantidad('Balas'), 12)
        self.assertFalse(self.mision.activa)
        self.assertTrue(self.policia.vivo)
        self.assertTrue(self.corredor.vivo)


if __name__ == '__main__':
    unittest.main(verbosity=2)
