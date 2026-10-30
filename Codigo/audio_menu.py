"""Efectos discretos de navegación; sin música de fondo."""

from array import array
import math

import pygame


class AudioMenu:
    def __init__(self):
        self.ambiente = self.seleccion = self.confirmacion = None
        self.canal = None
        formato = pygame.mixer.get_init()
        if not formato or formato[1] != -16:
            return
        frecuencia, _, canales = formato

        def tono(duracion, notas, volumen):
            muestras = array("h")
            cantidad = int(frecuencia * duracion)
            for i in range(cantidad):
                t = i / frecuencia
                envolvente = min(1, t / .025, (duracion - t) / .08)
                valor = sum(math.sin(2 * math.pi * nota * t) for nota in notas) / len(notas)
                muestras.extend([int(32767 * volumen * envolvente * valor)] * canales)
            return pygame.mixer.Sound(buffer=muestras.tobytes())

        try:
            self.seleccion = tono(.075, (330,), .018)
            self.confirmacion = tono(.12, (330, 495), .023)
        except (pygame.error, OSError):
            pass

    def sonar(self, confirmar=False):
        sonido = self.confirmacion if confirmar else self.seleccion
        if sonido:
            sonido.play()

    def detener(self):
        if self.canal:
            self.canal.fadeout(500)
