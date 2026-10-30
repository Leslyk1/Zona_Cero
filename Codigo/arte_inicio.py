"""Portada pixel art dibujada en Pygame con el superviviente del juego."""

from functools import lru_cache
from pathlib import Path
import pygame
from arte import sprite


MENTA = (98, 225, 176)
MARFIL = (224, 232, 214)
GRIS = (181, 197, 192)
ORO = (232, 190, 111)
BOTONES = tuple(pygame.Rect(90, 500 + i * 76, 440, 60) for i in range(3))
VOLVER = pygame.Rect(405, 680, 440, 60)
BOTONES_CONFIRMAR = tuple(pygame.Rect(405, 440 + i * 82, 440, 60) for i in range(2))
GLIFOS = {
    "Z": (31, 1, 2, 4, 8, 16, 31), "O": (14, 17, 17, 17, 17, 17, 14),
    "N": (17, 25, 25, 21, 19, 19, 17), "A": (14, 17, 17, 31, 17, 17, 17),
    "C": (14, 17, 16, 16, 16, 17, 14), "E": (31, 16, 16, 30, 16, 16, 31),
    "R": (30, 17, 17, 30, 20, 18, 17), "U": (17, 17, 17, 17, 17, 17, 14),
    "L": (16, 16, 16, 16, 16, 16, 31), "T": (31, 4, 4, 4, 4, 4, 4),
    "I": (31, 4, 4, 4, 4, 4, 31), "M": (17, 27, 21, 21, 17, 17, 17),
    "F": (31, 16, 16, 30, 16, 16, 16), "G": (14, 17, 16, 23, 17, 17, 14),
    "0": (14, 17, 19, 21, 25, 17, 14), "1": (4, 12, 4, 4, 4, 4, 14),
}


def letras(superficie, contenido, x, y, pixel, color):
    for letra in contenido:
        for fila, bits in enumerate(GLIFOS.get(letra, ())):
            for columna in range(5):
                if bits & (1 << (4 - columna)):
                    pygame.draw.rect(superficie, color, (x + columna * pixel, y + fila * pixel, pixel, pixel))
        x += (4 if letra == " " else 6) * pixel


@lru_cache(maxsize=48)
def fuente(tamano, negrita=False):
    # Letras de lectura claras; el título conserva sus glifos pixel art.
    ruta = pygame.font.match_font("Segoe UI,DejaVu Sans", bold=negrita)
    if ruta and Path(ruta).stem.lower().startswith("segoeui"):
        # En Windows, SysFont puede seleccionar la variante Light. Elegimos
        # los archivos regular/negrita para mantener el grosor de las letras.
        variante = Path(ruta).with_name("segoeuib.ttf" if negrita else "segoeui.ttf")
        if variante.is_file():
            ruta = str(variante)
    return pygame.font.Font(ruta, max(14, tamano))


def texto(lienzo, contenido, x, y, color=MARFIL, tamano=23, centro=False):
    imagen = fuente(tamano).render(contenido, True, color)
    rect = imagen.get_rect(center=(x, y)) if centro else imagen.get_rect(topleft=(x, y))
    lienzo.blit(imagen, rect)


@lru_cache(maxsize=1)
def escena():
    s = pygame.Surface((625, 400))
    s.fill((9, 19, 25))
    # Horizonte en capas, ventanas aisladas y una luna parcialmente cubierta.
    pygame.draw.rect(s, (39, 58, 61), (514, 48, 23, 23))
    pygame.draw.rect(s, (9, 19, 25), (510, 43, 21, 20))
    for capa in range(2):
        for i in range(11):
            x = 250 + i * 39 + capa * 13
            alto = 38 + (i * 37 + capa * 19) % 92
            y = 220 - alto + capa * 25
            color = (17, 34, 40) if capa == 0 else (20, 41, 44)
            pygame.draw.rect(s, color, (x, y, 32, 240 - y))
            pygame.draw.rect(s, color, (x + 5, y - 5, 19, 6))
            for fila in range(3):
                for columna in range(3):
                    if (i + fila * 2 + columna) % 4 == 0:
                        pygame.draw.rect(s, (52, 73, 66), (x + 5 + columna * 8, y + 13 + fila * 18, 3, 5))
    pygame.draw.rect(s, (18, 32, 35), (0, 287, 625, 113))
    for i in range(65):
        x, y = (i * 83) % 625, 295 + (i * 31) % 101
        pygame.draw.rect(s, (28, 47, 47), (x, y, 6 + i % 9, 2))
    # Fachada del refugio: hormigón, juntas, contrafuertes y chapa remachada.
    pygame.draw.rect(s, (7, 16, 20), (391, 175, 216, 172))
    pygame.draw.rect(s, (47, 61, 59), (400, 186, 192, 147))
    pygame.draw.rect(s, (69, 79, 69), (397, 179, 201, 11))
    pygame.draw.rect(s, (27, 42, 43), (404, 190, 184, 6))
    for y in range(205, 330, 23):
        pygame.draw.line(s, (36, 51, 50), (404, y), (590, y), 2)
        for x in range(408 + (y // 23 % 2) * 22, 586, 44):
            pygame.draw.line(s, (36, 51, 50), (x, y), (x, y + 21))
    pygame.draw.rect(s, (27, 42, 42), (411, 203, 168, 22))
    letras(s, "REFUGIO 01", 424, 208, 2, MENTA)
    pygame.draw.rect(s, (13, 27, 29), (467, 235, 63, 101))
    pygame.draw.rect(s, (83, 102, 83), (471, 239, 55, 96))
    pygame.draw.rect(s, (35, 58, 52), (476, 243, 45, 92))
    pygame.draw.rect(s, (64, 110, 88), (479, 246, 37, 86))
    for y in (251, 278, 314):
        pygame.draw.rect(s, (107, 127, 91), (479, y, 37, 3))
    pygame.draw.rect(s, ORO, (510, 291, 4, 9))
    pygame.draw.rect(s, (8, 23, 28), (415, 240, 38, 29))
    pygame.draw.rect(s, (66, 100, 94), (418, 243, 32, 23))
    pygame.draw.rect(s, (9, 30, 33), (421, 246, 26, 16))
    for x in (427, 438):
        pygame.draw.rect(s, (95, 126, 105), (x, 243, 2, 23))
    pygame.draw.rect(s, (25, 32, 30), (545, 245, 23, 32))
    pygame.draw.rect(s, (141, 119, 72), (547, 247, 19, 26))
    pygame.draw.rect(s, (74, 71, 52), (550, 251, 12, 2))
    pygame.draw.rect(s, (74, 71, 52), (550, 257, 8, 2))
    pygame.draw.rect(s, (14, 24, 26), (480, 226, 40, 6))
    pygame.draw.rect(s, ORO, (485, 230, 30, 3))
    # Peldaños, sacos, cajas y reflejos de luz sobre el asfalto.
    for i in range(3):
        pygame.draw.rect(s, (48 - i * 6, 67 - i * 7, 58 - i * 6), (462 - i * 5, 333 + i * 5, 73 + i * 10, 5))
    for x, y in ((409, 313), (420, 325), (553, 316), (566, 329)):
        pygame.draw.rect(s, (76, 78, 56), (x, y, 25, 10))
        pygame.draw.rect(s, (102, 99, 67), (x + 2, y, 21, 2))
        pygame.draw.rect(s, (41, 49, 40), (x + 11, y + 2, 2, 7))
    pygame.draw.rect(s, (73, 66, 44), (369, 313, 26, 25))
    pygame.draw.rect(s, (112, 96, 61), (369, 313, 26, 3))
    pygame.draw.line(s, (44, 44, 32), (372, 317), (391, 334), 3)
    for i in range(8):
        pygame.draw.rect(s, (39, 64, 55), (474 - i * 3, 351 + i * 5, 48 + i * 6, 2))
    # El mismo sprite que utiliza la partida, sin crear otro protagonista.
    pygame.draw.ellipse(s, (8, 17, 21), (447, 352, 55, 12))
    s.blit(sprite("superviviente", espalda=True), (450, 294))
    # Vegetación que invade el borde del refugio.
    for i in range(12):
        x = 587 + (i * 7) % 35
        pygame.draw.rect(s, (23, 46, 35), (x, 320 - i % 4 * 6, 3, 33 + i % 5))
    return s


def panel(lienzo, rect, color=(16, 29, 35), borde=(55, 78, 75)):
    x, y, w, h = rect
    pygame.draw.rect(lienzo, (4, 11, 16), (x + 5, y + 6, w, h))
    pygame.draw.rect(lienzo, borde, rect)
    pygame.draw.rect(lienzo, color, (x + 3, y + 3, w - 6, h - 6))
    for px, py in ((x + 9, y + 9), (x + w - 13, y + 9), (x + 9, y + h - 13), (x + w - 13, y + h - 13)):
        pygame.draw.rect(lienzo, borde, (px, py, 4, 4))


def boton(lienzo, rect, etiqueta, activo, indice=0):
    panel(lienzo, rect, (26, 51, 46) if activo else (14, 27, 33), MENTA if activo else (52, 73, 73))
    if activo:
        pygame.draw.rect(lienzo, MENTA, (rect.x + 3, rect.y + 3, 5, rect.h - 6))
        pygame.draw.polygon(lienzo, ORO, [(rect.x + 22, rect.centery - 7), (rect.x + 29, rect.centery), (rect.x + 22, rect.centery + 7)])
    texto(lienzo, etiqueta, rect.x + 48, rect.y + 16, MARFIL if activo else GRIS, 23)
    texto(lienzo, "0" + str(indice + 1), rect.right - 42, rect.y + 20, MENTA if activo else (66, 90, 86), 16)


def dibujar_inicio(lienzo, vista, seleccion, pausa, partida_activa, destino, tiempo):
    fondo = escena().copy()
    for i in range(45):
        x = 315 + (i * 73) % 310
        y = (i * 47 + tiempo // 40) % 400
        pygame.draw.line(fondo, (51, 73, 77), (x, y), (x - 2, y + 5))
    lienzo.blit(pygame.transform.scale(fondo, lienzo.get_size()), (0, 0))
    # Oscurecimiento escalonado: deja legible el menú y visible la escena.
    for x, ancho, alpha in ((0, 590, 180), (590, 40, 130), (630, 30, 70)):
        velo = pygame.Surface((ancho, 800), pygame.SRCALPHA)
        velo.fill((5, 14, 20, alpha))
        lienzo.blit(velo, (x, 0))
    pygame.draw.rect(lienzo, (35, 61, 59), (36, 36, 1178, 728), 2)
    for x, y, dx, dy in ((36, 36, 1, 1), (1214, 36, -1, 1), (36, 764, 1, -1), (1214, 764, -1, -1)):
        pygame.draw.line(lienzo, MENTA, (x, y), (x + dx * 25, y), 4)
        pygame.draw.line(lienzo, MENTA, (x, y), (x, y + dy * 25), 4)

    if vista == "menu":
        texto(lienzo, "■  REFUGIO 01 / SEÑAL ACTIVA", 92, 106, MENTA, 18)
        letras(lienzo, "ZONA", 96, 196, 13, (2, 9, 13))
        letras(lienzo, "ZONA", 90, 190, 13, MARFIL)
        letras(lienzo, "CERO", 96, 306, 13, (2, 9, 13))
        letras(lienzo, "CERO", 90, 300, 13, MARFIL)
        texto(lienzo, "PARTIDA EN PAUSA" if pausa else "ÚLTIMO REFUGIO", 92, 421, ORO, 28)
        texto(lienzo, "Todavía queda una oportunidad.", 92, 465, GRIS, 17)
        opciones = ("Continuar partida" if pausa or partida_activa else "Iniciar partida", "Controles", "Salir al menú" if pausa else "Salir")
        for i, etiqueta in enumerate(opciones):
            boton(lienzo, BOTONES[i], etiqueta, seleccion == i, i)
        texto(lienzo, "↑↓ ELEGIR   ENTER CONFIRMAR   MOUSE", 92, 737, GRIS, 15)
        texto(lienzo, "ZONA DE CUARENTENA", 846, 109, (111, 138, 130), 16)
        texto(lienzo, "EL REFUGIO SIGUE EN PIE.", 826, 734, MENTA, 17)
        return

    panel(lienzo, pygame.Rect(72, 82, 1106, 658), (10, 23, 29), (57, 86, 80))
    letras(lienzo, "ZONA CERO", 421, 117, 8, MARFIL)
    titulos = {"controles": "MANUAL DEL SUPERVIVIENTE", "introduccion": "ANTES DE SALIR AL MUNDO",
               "confirmar": "¿VOLVER AL MENÚ?" if destino == "menu" else "¿CERRAR EL JUEGO?"}
    texto(lienzo, titulos[vista], 625, 222, ORO, 24, True)
    pygame.draw.line(lienzo, (45, 70, 66), (160, 260), (1090, 260), 2)
    if vista == "controles":
        lineas = (("W A S D", "Moverse"), ("E", "Hablar, recoger objetos y abrir puertas"),
                  ("ESPACIO", "Mostrar el diálogo completo"), ("J", "Diario de misiones"),
                  ("G", "GLC / BNF     A / D: cambiar página"), ("X", "Explorar desde la calle"),
                  ("COMBATE", "Flechas + Enter, 1 / 2 / 3 o clic"),
                  ("ESC", "Cerrar paneles / Pausar la partida"))
        for i, (tecla, descripcion) in enumerate(lineas):
            texto(lienzo, tecla, 180, 304 + i * 45, MENTA, 23)
            texto(lienzo, descripcion, 350, 304 + i * 45, MARFIL, 23)
        boton(lienzo, VOLVER, "Volver al menú", True)
    elif vista == "confirmar":
        texto(lienzo, "La partida seguirá disponible mientras el juego esté abierto." if destino == "menu"
              else "El progreso de esta sesión se perderá al salir.", 625, 333, GRIS, 22, True)
        for i, etiqueta in enumerate(("Cancelar", "Sí, volver al menú" if destino == "menu" else "Sí, salir")):
            # Conserva los rectángulos que también utiliza la detección del mouse.
            boton(lienzo, BOTONES_CONFIRMAR[i], etiqueta, seleccion == i, i)
    else:
        lineas = ("La ciudad ha caído. Las calles ya no son seguras.",
                  "Entre el silencio y las señales de auxilio,", "un refugio sigue en pie.", "",
                  "Despiertas entre sus paredes. Afuera quedan", "supervivientes, suministros y decisiones por tomar.",
                  "Tu historia comienza aquí.")
        for i, linea in enumerate(lineas):
            texto(lienzo, linea, 625, 314 + i * 43, MENTA if i == 6 else GRIS, 23, True)
        boton(lienzo, VOLVER, "Entrar al refugio", True)
