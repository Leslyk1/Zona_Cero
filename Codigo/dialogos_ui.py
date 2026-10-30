"""Presentación de conversaciones; no genera texto ni modifica las misiones."""

from functools import lru_cache
import pygame
from arte import sprite
from arte_inicio import fuente, panel, MENTA, MARFIL, GRIS, ORO


@lru_cache(maxsize=2)
def retrato(personaje):
    # Ampliación entera del mismo sprite que aparece en el mundo.
    cara = sprite(personaje).subsurface((8, 3, 32, 32))
    return pygame.transform.scale(cara, (64, 64))


class DialogoUI:
    MS_POR_LETRA = 28
    TIEMPO_LECTURA = 4000

    def __init__(self):
        self.personaje = None
        self.mensaje = ""
        self.contenido = ""
        self.inicio = 0
        self.fin_escritura = 0
        self.completo = False
        self.oculto_desde = None

    def iniciar(self, personaje, mensaje):
        self.personaje = personaje
        self.mensaje = mensaje
        self.contenido = mensaje.removeprefix(personaje.capitalize() + ":").strip()
        self.inicio = pygame.time.get_ticks()
        self.fin_escritura = self.inicio + len(self.contenido) * self.MS_POR_LETRA
        self.completo = False
        self.oculto_desde = None

    def sincronizar(self, mensaje, zona):
        lugar = {"elena": "HOSPITAL", "marcos": "COMISARIA"}.get(self.personaje)
        if mensaje != self.mensaje or zona != lugar:
            self.personaje = None
            self.oculto_desde = None

    def cantidad_visible(self):
        if self.completo:
            return len(self.contenido)
        ahora = self.oculto_desde if self.oculto_desde is not None else pygame.time.get_ticks()
        return min(len(self.contenido), max(0, (ahora - self.inicio) // self.MS_POR_LETRA))

    @property
    def escribiendo(self):
        return bool(self.personaje) and self.cantidad_visible() < len(self.contenido)

    def revelar(self):
        if self.escribiendo:
            self.fin_escritura = (self.oculto_desde if self.oculto_desde is not None
                                  else pygame.time.get_ticks())
        self.completo = True

    @property
    def caducado(self):
        ahora = self.oculto_desde if self.oculto_desde is not None else pygame.time.get_ticks()
        return bool(self.personaje) and ahora >= self.fin_escritura + self.TIEMPO_LECTURA

    def visibilidad(self, visible):
        ahora = pygame.time.get_ticks()
        if not visible and self.oculto_desde is None:
            self.oculto_desde = ahora
        elif visible and self.oculto_desde is not None:
            pausa = ahora - self.oculto_desde
            self.inicio += pausa
            self.fin_escritura += pausa
            self.oculto_desde = None

    def dibujar(self, superficie):
        panel(superficie, pygame.Rect(10, 4, 980, 70), borde=MENTA)
        pygame.draw.rect(superficie, (29, 49, 48), (17, 7, 66, 64))
        superficie.blit(retrato(self.personaje), (18, 7))
        superficie.blit(fuente(19, True).render(self.personaje.upper(), True, MENTA), (96, 13))
        lugar = "HOSPITAL" if self.personaje == "elena" else "COMISARÍA"
        superficie.blit(fuente(12).render(lugar, True, GRIS), (96, 39))
        pygame.draw.line(superficie, (55, 78, 75), (222, 13), (222, 61), 2)

        # Ajustamos el texto completo primero, para que las palabras no salten
        # de línea mientras aparecen las letras. Los diálogos actuales caben
        # en dos líneas; no se toca la cadena generada por la gramática.
        tipografia = fuente(18)
        lineas = [""]
        for palabra in self.contenido.split():
            prueba = (lineas[-1] + " " + palabra).strip()
            if tipografia.size(prueba)[0] > 738 and lineas[-1]:
                lineas.append(palabra)
            else:
                lineas[-1] = prueba
        restantes = self.cantidad_visible()
        for fila, linea in enumerate(lineas):
            superficie.blit(tipografia.render(linea[:max(0, restantes)], True, MARFIL),
                            (238, 5 + fila * 24))
            restantes -= len(linea) + 1
        ayuda = "ESPACIO · Mostrar todo" if self.escribiendo else "CONVERSACIÓN / " + lugar
        superficie.blit(fuente(11).render(ayuda, True, ORO if self.escribiendo else GRIS), (238, 54))


def indicador_interaccion(superficie, jugador, mensaje):
    """Aviso anclado al jugador; solo lo llaman las condiciones originales."""
    accion = mensaje.removeprefix("E -").strip()
    activo = mensaje.startswith("E -")
    # Nombre corto sobre el personaje; el detalle se conserva en la franja.
    for prefijo, corto in (("Hablar con ", "Hablar"), ("Entrar", "Entrar"),
                           ("Salir", "Salir"), ("Recoger", "Recoger"),
                           ("Examinar", "Examinar"), ("Bajar", "Bajar"),
                           ("Subir", "Subir"), ("Ir al", "Evacuar")):
        if accion.startswith(prefijo):
            accion = corto
            break
    if not activo:
        accion = "Acceso bloqueado"
    etiqueta = ("E · " if activo else "") + accion
    dibujo = fuente(15, True).render(etiqueta, True, MARFIL)
    rect = pygame.Rect(0, 0, dibujo.get_width() + 28, 32)
    rect.midbottom = (jugador.centerx, jugador.top - 30)
    if rect.top < 8:
        rect.midtop = (jugador.centerx, jugador.bottom + 12)
    rect.clamp_ip(superficie.get_rect().inflate(-16, -16))
    color = MENTA if activo else ORO
    panel(superficie, rect, borde=color)
    superficie.blit(dibujo, dibujo.get_rect(center=rect.center))
    return rect
