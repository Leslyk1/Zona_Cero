"""Pruebas de voces y efectos: python Codigo/pruebas_audio.py."""
import os
os.environ["SDL_AUDIODRIVER"] = "dummy"
os.environ["SDL_VIDEODRIVER"] = "dummy"

import unittest
from unittest.mock import patch
import pygame
from audio_juego import AudioJuego
from combate import Combate
from enemigo import ZombiPolicia
from jugador import Jugador
from inventario import Inventario


class PruebasAudio(unittest.TestCase):
    def setUp(self):
        pygame.mixer.init(frequency=22050, size=-16, channels=2)
        self.addCleanup(pygame.mixer.quit)
        self.audio = AudioJuego()
        self.assertTrue(self.audio.disponible)
        self.jugador = Jugador()
        self.combate = Combate()
        self.combate.iniciar(ZombiPolicia(), self.jugador)
        self.sonar = patch.object(self.audio, "_reproducir")
        self.efecto = self.sonar.start()
        self.addCleanup(self.sonar.stop)

    def actualizar(self):
        self.audio.actualizar(self.combate)

    def test_exploracion_y_combate_inicial_sin_musica(self):
        self.actualizar()
        self.efecto.assert_not_called()
        self.assertFalse(any(c.get_busy() for c in self.audio.canales))
        self.assertEqual(set(self.audio.sonidos), {"elena", "marcos", *self.audio.EFECTOS})

    def test_golpe_y_fallo_una_sola_vez(self):
        for azar, efecto in ((50, "golpe"), (100, "esquive")):
            self.combate.terminar()
            self.actualizar()
            self.combate.iniciar(ZombiPolicia(), self.jugador)
            with patch("combate.random.randint", return_value=azar):
                self.combate.golpear(self.jugador)
            self.efecto.reset_mock()
            for _ in range(10):
                self.actualizar()
            self.efecto.assert_called_once_with(efecto)

    def test_disparo_y_arma_sin_recursos(self):
        inv = Inventario()
        self.combate.disparar(self.jugador, inv)
        self.actualizar()
        self.efecto.assert_called_with("vacio")
        inv.agregar("Pistola")
        inv.agregar("Balas", 2)
        with patch("combate.random.randint", return_value=100):
            self.combate.disparar(self.jugador, inv)
        self.actualizar()
        self.efecto.assert_called_with("disparo")
        self.assertEqual(inv.obtener_cantidad("Balas"), 1)

    def test_defensa_bloqueo_y_esquive_enemigo(self):
        self.combate.defender(self.jugador)
        self.actualizar()
        self.efecto.assert_called_with("defensa")
        with patch("combate.random.randint", return_value=100):
            self.combate.turno_enemigo(self.jugador, "DEFENDER", "GUARDIA")
        self.actualizar()
        self.efecto.assert_called_with("defensa")
        with patch("combate.random.randint", return_value=1):
            self.combate.turno_enemigo(self.jugador, "GOLPEAR", "GOLPE_NORMAL")
        self.actualizar()
        self.efecto.assert_called_with("esquive")

    def test_dano_y_resultados(self):
        with patch("combate.random.randint", return_value=100):
            self.combate.turno_enemigo(self.jugador, "GOLPEAR", "GOLPE_NORMAL")
        self.actualizar()
        self.efecto.assert_called_with("herida")
        for estado, efecto in (("VICTORIA", "victoria"), ("DERROTA", "derrota")):
            self.combate.estado = estado
            self.actualizar()
            self.efecto.assert_called_with(efecto)

    def test_pausa_y_voces(self):
        self.audio.dialogo("elena")
        self.assertEqual(self.audio.voz.get_sound(), self.audio.sonidos["elena"])
        self.audio.suspender()
        self.combate.defender(self.jugador)
        self.actualizar()
        self.efecto.assert_not_called()
        self.audio.reanudar()
        self.actualizar()
        self.efecto.assert_called_once_with("defensa")
        self.audio.dialogo("marcos")
        self.assertEqual(self.audio.voz.get_sound(), self.audio.sonidos["marcos"])

    def test_efectos_breves_volumen_bajo(self):
        for nombre in self.audio.EFECTOS:
            self.assertLess(self.audio.sonidos[nombre].get_length(), .5)
        self.sonar.stop()
        self.audio._reproducir("golpe")
        self.assertTrue(any(c.get_busy() for c in self.audio.canales))
        self.assertTrue(all(c.get_volume() <= .23 for c in self.audio.canales if c.get_busy()))

    def test_sin_dispositivo_de_audio(self):
        with patch("pygame.mixer.get_init", return_value=None):
            audio = AudioJuego()
            audio.actualizar(self.combate)
            audio.dialogo("marcos")
            audio.suspender()
            audio.reanudar()
            audio.detener()

    def test_menu_con_botones_sin_musica(self):
        from audio_menu import AudioMenu
        with patch("pygame.mixer.Sound", wraps=pygame.mixer.Sound) as cargar:
            menu = AudioMenu()
            self.assertIsNone(menu.ambiente)
            self.assertIsNone(menu.canal)
            self.assertTrue(all(not c.args or not isinstance(c.args[0], str) for c in cargar.call_args_list))
        self.assertIsNotNone(menu.seleccion)
        self.assertIsNotNone(menu.confirmacion)
        menu.sonar()
        menu.sonar(confirmar=True)

    def test_menu_restaura_navegacion_y_confirmacion(self):
        import inicio
        pygame.display.init()
        pygame.font.init()
        self.addCleanup(pygame.display.quit)
        pantalla = pygame.display.set_mode((800, 600))
        def tecla(k): return pygame.event.Event(pygame.KEYDOWN, key=k)
        eventos = iter([[tecla(pygame.K_DOWN)], [tecla(pygame.K_RETURN)],
                        [tecla(pygame.K_ESCAPE)], [tecla(pygame.K_RETURN)]])
        with patch("pygame.event.get", side_effect=lambda: next(eventos)), patch("inicio.AudioMenu") as audio:
            self.assertTrue(inicio.mostrar_inicio(pantalla, pausa=True))
            audio.return_value.sonar.assert_any_call()
            audio.return_value.sonar.assert_any_call(confirmar=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
