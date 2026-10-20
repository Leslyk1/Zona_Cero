"""Cinemáticas finales dibujadas con Pygame.

No utiliza imágenes externas. Cada final conserva su estado formal del AFN
y solamente agrega una escena visual antes de mostrar la pantalla final.
"""

import math
import pygame


FONDO = (3, 11, 12)
AZUL_OSCURO = (8, 20, 27)
MENTA = (98, 225, 176)
DORADO = (232, 190, 111)
BLANCO = (228, 235, 232)
GRIS = (145, 158, 158)
ROJO = (236, 79, 79)
VERDE_SUERO = (76, 255, 151)


class CinematicasFinales:

    DURACION = 7600

    def __init__(self):
        self.estado = None
        self.inicio = 0
        self.terminada = False

    def iniciar(self, estado):
        self.estado = estado
        self.inicio = pygame.time.get_ticks()
        self.terminada = False

    def reiniciar(self):
        self.estado = None
        self.inicio = 0
        self.terminada = False

    def saltar(self):
        self.terminada = True

    def tiempo(self):
        if self.estado is None:
            return 0
        return pygame.time.get_ticks() - self.inicio

    def actualizar(self):
        if (
            self.estado is not None
            and not self.terminada
            and self.tiempo() >= self.DURACION
        ):
            self.terminada = True

    def dibujar(self, ventana, estado):
        if self.estado != estado:
            self.iniciar(estado)

        self.actualizar()

        if self.terminada:
            return

        t = self.tiempo()

        if estado == "FINAL_EVACUACION":
            self._evacuacion(ventana, t)
        elif estado == "FINAL_SACRIFICIO":
            self._sacrificio(ventana, t)
        else:
            self._infectado(ventana, t)

    # ===================================
    # ELEMENTOS GENERALES
    # ===================================

    def _fondo(self, ventana, titulo, color):
        ventana.fill(FONDO)

        for x in range(0, 1000, 40):
            pygame.draw.line(ventana, (11, 29, 30), (x, 0), (x, 650))

        for y in range(0, 650, 40):
            pygame.draw.line(ventana, (11, 29, 30), (0, y), (1000, y))

        pygame.draw.rect(
            ventana,
            (11, 24, 31),
            (50, 35, 900, 565),
            border_radius=12
        )

        pygame.draw.rect(
            ventana,
            color,
            (50, 35, 900, 565),
            2,
            border_radius=12
        )

        fuente_titulo = pygame.font.SysFont("Segoe UI", 30, bold=True)
        texto = fuente_titulo.render(titulo, True, color)
        ventana.blit(texto, texto.get_rect(center=(500, 78)))

        pygame.draw.line(ventana, color, (100, 110), (900, 110), 2)

        pygame.draw.rect(
            ventana,
            AZUL_OSCURO,
            (90, 135, 820, 355),
            border_radius=10
        )

        pygame.draw.rect(
            ventana,
            MENTA,
            (90, 135, 820, 355),
            2,
            border_radius=10
        )

    def _mensaje(self, ventana, linea1, linea2=""):
        caja = pygame.Rect(110, 510, 780, 62)

        pygame.draw.rect(ventana, (9, 22, 29), caja, border_radius=8)
        pygame.draw.rect(ventana, DORADO, caja, 2, border_radius=8)

        fuente1 = pygame.font.SysFont("Segoe UI", 17, bold=True)
        fuente2 = pygame.font.SysFont("Segoe UI", 13)

        texto1 = fuente1.render(linea1, True, BLANCO)
        ventana.blit(texto1, texto1.get_rect(center=(500, 530)))

        if linea2:
            texto2 = fuente2.render(linea2, True, GRIS)
            ventana.blit(texto2, texto2.get_rect(center=(500, 554)))

        ayuda = pygame.font.SysFont(
            "Segoe UI",
            12,
            bold=True
        ).render(
            "ENTER = SALTAR ESCENA",
            True,
            GRIS
        )
        ventana.blit(ayuda, ayuda.get_rect(center=(500, 585)))

    def _ciudad(self, ventana, incendio=True):
        edificios = [
            (110, 285, 70, 190),
            (190, 330, 85, 145),
            (285, 255, 75, 220),
            (370, 310, 95, 165),
            (475, 270, 65, 205),
            (555, 320, 85, 155),
            (655, 250, 80, 225),
            (750, 300, 90, 175),
        ]

        for x, y, ancho, alto in edificios:
            pygame.draw.rect(ventana, (18, 27, 33), (x, y, ancho, alto))

            for wx in range(x + 12, x + ancho - 10, 18):
                for wy in range(y + 18, y + alto - 12, 25):
                    color = (
                        (118, 74, 43)
                        if incendio and (wx + wy) % 3 == 0
                        else (34, 50, 54)
                    )
                    pygame.draw.rect(ventana, color, (wx, wy, 5, 8))

    def _personaje(self, ventana, x, y, escala=1.0, mirando="derecha"):
        x = int(x)
        y = int(y)
        e = escala

        pygame.draw.circle(
            ventana,
            (204, 161, 122),
            (x, int(y - 28 * e)),
            int(10 * e)
        )

        pygame.draw.circle(
            ventana,
            (34, 33, 36),
            (x, int(y - 33 * e)),
            int(10 * e)
        )

        pygame.draw.rect(
            ventana,
            (36, 73, 75),
            (
                int(x - 10 * e),
                int(y - 20 * e),
                int(20 * e),
                int(30 * e)
            ),
            border_radius=max(1, int(4 * e))
        )

        lado = -1 if mirando == "derecha" else 1
        pygame.draw.rect(
            ventana,
            (29, 44, 47),
            (
                int(x + lado * -13 * e),
                int(y - 17 * e),
                int(9 * e),
                int(24 * e)
            ),
            border_radius=max(1, int(2 * e))
        )

        pygame.draw.line(
            ventana,
            MENTA,
            (int(x + lado * -10 * e), int(y - 14 * e)),
            (int(x + lado * -10 * e), int(y + 3 * e)),
            max(1, int(2 * e))
        )

        dir_x = 1 if mirando == "derecha" else -1
        pygame.draw.line(
            ventana,
            (204, 161, 122),
            (x, int(y - 12 * e)),
            (int(x + dir_x * 19 * e), int(y - 8 * e)),
            max(2, int(4 * e))
        )

        pygame.draw.line(
            ventana,
            (44, 49, 52),
            (int(x - 5 * e), int(y + 8 * e)),
            (int(x - 11 * e), int(y + 27 * e)),
            max(2, int(5 * e))
        )

        pygame.draw.line(
            ventana,
            (44, 49, 52),
            (int(x + 5 * e), int(y + 8 * e)),
            (int(x + 12 * e), int(y + 27 * e)),
            max(2, int(5 * e))
        )

    def _helicoptero(self, ventana, x, y, escala=1.0):
        x = int(x)
        y = int(y)
        e = escala

        cuerpo = pygame.Rect(
            int(x - 70 * e),
            int(y - 28 * e),
            int(140 * e),
            int(56 * e)
        )

        pygame.draw.ellipse(ventana, (42, 52, 55), cuerpo)
        pygame.draw.ellipse(
            ventana,
            (95, 108, 105),
            cuerpo,
            max(1, int(2 * e))
        )

        pygame.draw.polygon(
            ventana,
            (49, 76, 78),
            [
                (int(x + 30 * e), int(y - 20 * e)),
                (int(x + 62 * e), int(y - 12 * e)),
                (int(x + 62 * e), int(y + 10 * e)),
                (int(x + 30 * e), int(y + 18 * e))
            ]
        )

        pygame.draw.rect(
            ventana,
            (207, 167, 92),
            (
                int(x - 20 * e),
                int(y - 20 * e),
                int(32 * e),
                int(40 * e)
            )
        )

        pygame.draw.rect(
            ventana,
            (19, 24, 26),
            (
                int(x - 15 * e),
                int(y - 16 * e),
                int(26 * e),
                int(32 * e)
            )
        )

        pygame.draw.line(
            ventana,
            (51, 62, 64),
            (int(x - 60 * e), y),
            (int(x - 125 * e), int(y - 10 * e)),
            max(2, int(10 * e))
        )

        pygame.draw.line(
            ventana,
            GRIS,
            (int(x - 45 * e), int(y + 32 * e)),
            (int(x + 45 * e), int(y + 32 * e)),
            max(1, int(3 * e))
        )

        fase = pygame.time.get_ticks() // 45
        extension = int(95 * e)

        if fase % 2 == 0:
            pygame.draw.line(
                ventana,
                (130, 142, 140),
                (x - extension, int(y - 38 * e)),
                (x + extension, int(y - 38 * e)),
                max(1, int(3 * e))
            )
        else:
            pygame.draw.line(
                ventana,
                (130, 142, 140),
                (x - int(extension * .72), int(y - 54 * e)),
                (x + int(extension * .72), int(y - 22 * e)),
                max(1, int(3 * e))
            )

        pygame.draw.circle(
            ventana,
            MENTA,
            (int(x - 124 * e), int(y - 10 * e)),
            max(2, int(4 * e))
        )

    def _zombi(self, ventana, x, y, escala=1.0):
        e = escala

        pygame.draw.circle(
            ventana,
            (96, 108, 91),
            (int(x), int(y - 24 * e)),
            max(3, int(8 * e))
        )

        pygame.draw.line(
            ventana,
            (74, 83, 72),
            (int(x), int(y - 16 * e)),
            (int(x), int(y + 9 * e)),
            max(2, int(6 * e))
        )

        pygame.draw.line(
            ventana,
            (74, 83, 72),
            (int(x), int(y - 7 * e)),
            (int(x - 13 * e), int(y + 2 * e)),
            max(2, int(4 * e))
        )

        pygame.draw.line(
            ventana,
            (74, 83, 72),
            (int(x), int(y - 7 * e)),
            (int(x + 13 * e), int(y - 1 * e)),
            max(2, int(4 * e))
        )

        pygame.draw.circle(
            ventana,
            ROJO,
            (int(x - 3 * e), int(y - 26 * e)),
            max(1, int(2 * e))
        )

        pygame.draw.circle(
            ventana,
            ROJO,
            (int(x + 3 * e), int(y - 26 * e)),
            max(1, int(2 * e))
        )

    # ===================================
    # FINAL 1 - EVACUACION
    # ===================================

    def _evacuacion(self, ventana, t):
        self._fondo(ventana, "ESCAPE EN HELICOPTERO", MENTA)
        self._ciudad(ventana, True)

        pygame.draw.rect(ventana, (32, 39, 41), (90, 430, 820, 60))

        for x in range(120, 890, 90):
            pygame.draw.rect(ventana, MENTA, (x, 458, 20, 5))

        for i in range(7):
            zx = 115 + i * 55 + min(t / 90, 60)
            zy = 415 + (i % 2) * 15
            self._zombi(ventana, zx, zy, .75)

        if t < 4500:
            hx = 735
            hy = 320
        else:
            progreso = min(1.0, (t - 4500) / 2800)
            hx = 735 + 110 * progreso
            hy = 320 - 150 * progreso

        self._helicoptero(ventana, hx, hy, .95)

        if t < 4500:
            pygame.draw.polygon(
                ventana,
                (78, 83, 81),
                [(665, 340), (710, 340), (650, 455), (610, 455)]
            )

        if t < 2500:
            progreso = t / 2500
            px = 260 + 330 * progreso
            py = 425
            self._personaje(ventana, px, py, 1.0)
            self._mensaje(
                ventana,
                "Corres hacia el helicoptero antes de que cierre la ruta.",
                "La horda se acerca al punto de evacuacion."
            )

        elif t < 4500:
            progreso = (t - 2500) / 2000
            px = 590 + 85 * progreso
            py = 425 - 85 * progreso
            self._personaje(ventana, px, py, 1.0)
            self._mensaje(
                ventana,
                "Un soldado te ayuda a subir al helicoptero.",
                "La aeronave comienza a levantar vuelo."
            )

        else:
            self._mensaje(
                ventana,
                "El helicoptero despega con los sobrevivientes.",
                "Has logrado escapar de Zona Cero."
            )

    # ===================================
    # FINAL 2 - SACRIFICIO
    # ===================================

    def _sacrificio(self, ventana, t):
        self._fondo(ventana, "SACRIFICIO HEROICO", DORADO)
        self._ciudad(ventana, True)

        pygame.draw.rect(ventana, (32, 39, 41), (90, 430, 820, 60))

        progreso_heli = min(1.0, t / 6500)
        self._helicoptero(
            ventana,
            730 + 120 * progreso_heli,
            270 - 130 * progreso_heli,
            .72
        )

        self._personaje(ventana, 500, 420, 1.25)

        pygame.draw.line(ventana, (75, 82, 84), (515, 394), (565, 385), 7)

        if (t // 180) % 2 == 0:
            pygame.draw.circle(ventana, DORADO, (573, 383), 12)
            pygame.draw.line(ventana, DORADO, (573, 383), (615, 375), 3)

        for i in range(10):
            inicio_x = (
                120 + (i % 5) * 55
                if i < 5
                else 870 - (i % 5) * 55
            )
            direccion = 1 if i < 5 else -1
            zx = inicio_x + direccion * min(t / 45, 120)
            zy = 430 + (i % 3) * 12
            self._zombi(ventana, zx, zy, .85)

        if t < 3000:
            self._mensaje(
                ventana,
                "Te quedas atras y cubres la retirada.",
                "El helicoptero comienza a alejarse."
            )
        elif t < 6000:
            self._mensaje(
                ventana,
                "La horda te rodea mientras sigues disparando.",
                "Cada segundo permite que los demas ganen distancia."
            )
        else:
            self._mensaje(
                ventana,
                "Tu ultima resistencia asegura la evacuacion.",
                "Los sobrevivientes logran escapar."
            )

    # ===================================
    # FINAL 3 - INFECTADO
    # ===================================

    def _infectado(self, ventana, t):
        self._fondo(ventana, "SUERO EXPERIMENTAL", ROJO)
        self._ciudad(ventana, True)

        pygame.draw.rect(ventana, (32, 39, 41), (90, 430, 820, 60))

        self._helicoptero(ventana, 760, 315, .82)
        self._personaje(ventana, 470, 420, 1.35)

        pygame.draw.rect(
            ventana,
            (185, 200, 194),
            (500, 355, 14, 42),
            border_radius=4
        )
        pygame.draw.rect(
            ventana,
            VERDE_SUERO,
            (503, 362, 8, 27),
            border_radius=3
        )
        pygame.draw.line(ventana, GRIS, (507, 397), (490, 410), 2)

        if t > 1800:
            pulso = 20 + 18 * math.sin(t / 170)
            pygame.draw.circle(
                ventana,
                VERDE_SUERO,
                (470, 390),
                int(abs(pulso)),
                2
            )

            for desplazamiento in (-26, -15, 14, 28):
                pygame.draw.line(
                    ventana,
                    VERDE_SUERO,
                    (470, 392),
                    (470 + desplazamiento, 350 + abs(desplazamiento)),
                    2
                )

        for i in range(6):
            self._zombi(ventana, 140 + i * 70, 445, .7)

        if t < 1800:
            self._mensaje(
                ventana,
                "Decides utilizar el suero experimental.",
                "No existe garantia de que funcione."
            )

        elif t < 4700:
            self._mensaje(
                ventana,
                "El compuesto comienza a recorrer tu cuerpo.",
                "Una energia extraña se extiende por tus venas."
            )

        else:
            intensidad = min(120, int((t - 4700) / 18))
            capa = pygame.Surface((1000, 650), pygame.SRCALPHA)
            capa.fill((110, 10, 10, intensidad))
            ventana.blit(capa, (0, 0))

            self._mensaje(
                ventana,
                "El suero falla y la infeccion toma el control.",
                "Tu destino queda sellado."
            )
