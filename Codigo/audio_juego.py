"""Solo voces de NPC y efectos puntuales de combate; sin música de fondo."""

from pathlib import Path

import pygame


class AudioJuego:
    VOLUMEN_EFECTOS = .22
    VOLUMEN_VOZ = .22
    EFECTOS = ("golpe", "disparo", "defensa", "esquive", "herida", "victoria", "derrota", "vacio")

    def __init__(self):
        self.disponible = bool(pygame.mixer.get_init())
        self.pausado = False
        self.sonidos = {}
        self.canales = ()
        self.voz = None
        self.ultimo_evento = None
        self.leyendo_dialogo = False
        if not self.disponible:
            return
        try:
            pygame.mixer.set_num_channels(max(8, pygame.mixer.get_num_channels()))
            pygame.mixer.set_reserved(3)
            self.canales = (pygame.mixer.Channel(0), pygame.mixer.Channel(1))
            self.voz = pygame.mixer.Channel(2)
            carpeta = Path(__file__).resolve().parent / "sonidos"
            for nombre in ("elena", "marcos"):
                self.sonidos[nombre] = pygame.mixer.Sound(str(carpeta / (nombre + ".wav")))
            for nombre in self.EFECTOS:
                self.sonidos[nombre] = pygame.mixer.Sound(str(carpeta / ("efecto_" + nombre + ".wav")))
        except (pygame.error, OSError):
            self.disponible = False

    def _reproducir(self, nombre):
        # Efectos breves y sin bucles; el segundo canal permite solapar impactos.
        canal = next((c for c in self.canales if not c.get_busy()), self.canales[0])
        canal.set_volume(self.VOLUMEN_EFECTOS)
        canal.play(self.sonidos[nombre])

    def actualizar(self, combate):
        if not self.disponible or self.pausado:
            return
        if not combate.activo:
            self.ultimo_evento = None
            return
        evento = (combate.estado, combate.inicio_fase, combate.turno,
                  len(combate.historial), combate.mensaje)
        if evento == self.ultimo_evento:
            return
        self.ultimo_evento = evento
        efecto = None
        if combate.estado == "ATACANDO":
            efecto = "esquive" if combate.resultado_actual == "FALLO" else "golpe"
        elif combate.estado == "DISPARANDO":
            efecto = "disparo"
        elif combate.estado == "DEFENDIENDO":
            efecto = "defensa"
        elif combate.estado == "TURNO_ENEMIGO":
            efecto = ("esquive" if combate.dano_animacion == 0 else
                      "defensa" if combate.transicion.endswith("BLOQUEO") else "herida")
        elif combate.estado == "VICTORIA":
            efecto = "victoria"
        elif combate.estado == "DERROTA":
            efecto = "derrota"
        elif combate.estado == "ELEGIR_ACCION" and combate.mensaje.startswith(("Necesitas una pistola", "No quedan balas")):
            efecto = "vacio"
        if efecto:
            self._reproducir(efecto)

    def dialogo(self, personaje):
        if self.disponible and not self.pausado:
            self.leyendo_dialogo = True
            self.voz.set_volume(self.VOLUMEN_VOZ)
            self.voz.play(self.sonidos[personaje], fade_ms=25)

    def actualizar_dialogo(self, personaje, escribiendo):
        """Acompaña las letras; se calla al completar u ocultar el diálogo."""
        if not self.disponible or self.pausado:
            return
        if personaje and escribiendo:
            if not self.voz.get_busy():
                self.dialogo(personaje)
        elif self.leyendo_dialogo:
            self.voz.fadeout(70)
            self.leyendo_dialogo = False

    def suspender(self):
        self.pausado = True
        if self.disponible:
            for canal in (*self.canales, self.voz):
                canal.pause()

    def reanudar(self):
        self.pausado = False
        if self.disponible:
            for canal in (*self.canales, self.voz):
                canal.unpause()

    def detener(self):
        if self.disponible:
            for canal in (*self.canales, self.voz):
                canal.stop()
