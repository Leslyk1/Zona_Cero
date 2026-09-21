# Importamos pygame
import pygame


# Importamos colores
from configuracion import (
    GRIS,
    GRIS_OSCURO,
    GRIS_CLARO,
    BLANCO,
    AMARILLO,
    ASFALTO
)


# ===================================
# REFUGIO
# ===================================

def crear_paredes_refugio():

    paredes = []


    paredes.append(
        pygame.Rect(
            50,
            50,
            900,
            25
        )
    )


    paredes.append(
        pygame.Rect(
            50,
            575,
            900,
            25
        )
    )


    paredes.append(
        pygame.Rect(
            50,
            75,
            25,
            500
        )
    )


    paredes.append(
        pygame.Rect(
            925,
            75,
            25,
            200
        )
    )


    paredes.append(
        pygame.Rect(
            925,
            375,
            25,
            200
        )
    )


    paredes.append(
        pygame.Rect(
            400,
            75,
            25,
            180
        )
    )


    paredes.append(
        pygame.Rect(
            400,
            355,
            25,
            220
        )
    )


    paredes.append(
        pygame.Rect(
            75,
            320,
            220,
            25
        )
    )


    paredes.append(
        pygame.Rect(
            550,
            430,
            375,
            25
        )
    )


    return paredes


def crear_salida_refugio():

    return pygame.Rect(
        860,
        285,
        90,
        90
    )


def dibujar_refugio(
    ventana,
    paredes
):

    ventana.fill(
        GRIS_OSCURO
    )


    # Piso.
    for x in range(
        0,
        1000,
        40
    ):

        pygame.draw.line(
            ventana,
            (45, 45, 45),
            (x, 0),
            (x, 650)
        )


    for y in range(
        0,
        650,
        40
    ):

        pygame.draw.line(
            ventana,
            (45, 45, 45),
            (0, y),
            (1000, y)
        )


    # Paredes.
    for pared in paredes:

        pygame.draw.rect(
            ventana,
            GRIS,
            pared
        )

        pygame.draw.rect(
            ventana,
            GRIS_CLARO,
            pared,
            2
        )


    fuente = pygame.font.SysFont(
        "Arial",
        20
    )


    texto = fuente.render(
        "DORMITORIO",
        True,
        BLANCO
    )

    ventana.blit(
        texto,
        (130, 100)
    )


    texto = fuente.render(
        "ALMACEN",
        True,
        BLANCO
    )

    ventana.blit(
        texto,
        (130, 370)
    )


    texto = fuente.render(
        "SALA PRINCIPAL",
        True,
        BLANCO
    )

    ventana.blit(
        texto,
        (560, 100)
    )


    texto = fuente.render(
        "SALIDA",
        True,
        AMARILLO
    )

    ventana.blit(
        texto,
        (850, 320)
    )


# ===================================
# CALLE
# ===================================

def crear_paredes_calle():

    paredes = []


    # Refugio.
    paredes.append(
        pygame.Rect(
            0,
            200,
            70,
            250
        )
    )


    # Hospital.
    paredes.append(
        pygame.Rect(
            700,
            50,
            250,
            130
        )
    )


    # Comisaría.
    paredes.append(
        pygame.Rect(
            50,
            450,
            220,
            100
        )
    )


    # Auto.
    paredes.append(
        pygame.Rect(
            350,
            180,
            170,
            80
        )
    )


    # Auto.
    paredes.append(
        pygame.Rect(
            550,
            390,
            180,
            75
        )
    )


    # Barricada.
    paredes.append(
        pygame.Rect(
            320,
            500,
            150,
            40
        )
    )


    return paredes


def crear_entrada_refugio():

    return pygame.Rect(
        50,
        270,
        100,
        110
    )


def crear_entrada_hospital():

    return pygame.Rect(
        780,
        150,
        110,
        80
    )


def crear_entrada_comisaria():

    return pygame.Rect(
        100,
        410,
        120,
        70
    )


def dibujar_calle(
    ventana,
    paredes
):

    ventana.fill(
        ASFALTO
    )


    # Aceras.
    pygame.draw.rect(
        ventana,
        GRIS,
        (0, 0, 1000, 100)
    )


    pygame.draw.rect(
        ventana,
        GRIS,
        (0, 550, 1000, 100)
    )


    # Líneas de carretera.
    for x in range(
        150,
        1000,
        160
    ):

        pygame.draw.rect(
            ventana,
            AMARILLO,
            (x, 320, 90, 8)
        )


    # Edificios y obstáculos.
    for pared in paredes:

        pygame.draw.rect(
            ventana,
            GRIS_OSCURO,
            pared
        )

        pygame.draw.rect(
            ventana,
            GRIS_CLARO,
            pared,
            2
        )


    # Puerta del refugio.
    pygame.draw.rect(
        ventana,
        AMARILLO,
        (60, 285, 15, 80)
    )


    # Hospital.
    pygame.draw.rect(
        ventana,
        AMARILLO,
        (800, 170, 70, 10)
    )


    # Comisaría.
    pygame.draw.rect(
        ventana,
        AMARILLO,
        (120, 440, 80, 10)
    )


    fuente = pygame.font.SysFont(
        "Arial",
        20
    )


    texto = fuente.render(
        "CALLE ABANDONADA",
        True,
        BLANCO
    )

    ventana.blit(
        texto,
        (400, 285)
    )


    texto = fuente.render(
        "REFUGIO",
        True,
        AMARILLO
    )

    ventana.blit(
        texto,
        (80, 230)
    )


    texto = fuente.render(
        "HOSPITAL",
        True,
        BLANCO
    )

    ventana.blit(
        texto,
        (780, 100)
    )


    texto = fuente.render(
        "COMISARIA",
        True,
        BLANCO
    )

    ventana.blit(
        texto,
        (100, 490)
    )


# ===================================
# HOSPITAL
# ===================================

def crear_paredes_hospital():

    paredes = []


    # Exterior.
    paredes.append(
        pygame.Rect(
            50,
            50,
            900,
            25
        )
    )


    paredes.append(
        pygame.Rect(
            50,
            75,
            25,
            500
        )
    )


    paredes.append(
        pygame.Rect(
            925,
            75,
            25,
            500
        )
    )


    # Parte inferior con abertura.
    paredes.append(
        pygame.Rect(
            50,
            575,
            390,
            25
        )
    )


    paredes.append(
        pygame.Rect(
            560,
            575,
            390,
            25
        )
    )


    # Divisiones.
    paredes.append(
        pygame.Rect(
            400,
            75,
            25,
            200
        )
    )


    paredes.append(
        pygame.Rect(
            400,
            375,
            25,
            200
        )
    )


    paredes.append(
        pygame.Rect(
            550,
            320,
            375,
            25
        )
    )


    return paredes


def crear_salida_hospital():

    return pygame.Rect(
        440,
        520,
        120,
        80
    )


# -----------------------------------
# ESCALERAS AL SÓTANO
# -----------------------------------

def crear_entrada_sotano_hospital():

    return pygame.Rect(
        120,
        200,
        110,
        90
    )


def dibujar_hospital(
    ventana,
    paredes
):

    ventana.fill(
        (28, 36, 32)
    )


    # Piso.
    for x in range(
        0,
        1000,
        40
    ):

        pygame.draw.line(
            ventana,
            (38, 48, 42),
            (x, 0),
            (x, 650)
        )


    for y in range(
        0,
        650,
        40
    ):

        pygame.draw.line(
            ventana,
            (38, 48, 42),
            (0, y),
            (1000, y)
        )


    # Paredes.
    for pared in paredes:

        pygame.draw.rect(
            ventana,
            GRIS,
            pared
        )

        pygame.draw.rect(
            ventana,
            GRIS_CLARO,
            pared,
            2
        )


    # Escaleras.
    pygame.draw.rect(
        ventana,
        (70, 60, 40),
        (130, 210, 90, 65)
    )


    # Líneas de las escaleras.
    for y in range(
        215,
        270,
        10
    ):

        pygame.draw.line(
            ventana,
            AMARILLO,
            (135, y),
            (215, y)
        )


    fuente = pygame.font.SysFont(
        "Arial",
        20
    )


    texto = fuente.render(
        "RECEPCION",
        True,
        BLANCO
    )

    ventana.blit(
        texto,
        (120, 110)
    )


    texto = fuente.render(
        "LABORATORIO",
        True,
        BLANCO
    )

    ventana.blit(
        texto,
        (600, 110)
    )


    texto = fuente.render(
        "FARMACIA",
        True,
        BLANCO
    )

    ventana.blit(
        texto,
        (600, 400)
    )


    texto = fuente.render(
        "SOTANO",
        True,
        AMARILLO
    )

    ventana.blit(
        texto,
        (135, 175)
    )


    texto = fuente.render(
        "SALIDA",
        True,
        AMARILLO
    )

    ventana.blit(
        texto,
        (465, 540)
    )


# ===================================
# SÓTANO DEL HOSPITAL
# ===================================

def crear_paredes_sotano():

    paredes = []


    # Pared superior izquierda.
    paredes.append(
        pygame.Rect(
            50,
            50,
            390,
            25
        )
    )


    # Pared superior derecha.
    paredes.append(
        pygame.Rect(
            560,
            50,
            390,
            25
        )
    )


    # Pared inferior.
    paredes.append(
        pygame.Rect(
            50,
            575,
            900,
            25
        )
    )


    # Pared izquierda.
    paredes.append(
        pygame.Rect(
            50,
            75,
            25,
            500
        )
    )


    # Pared derecha.
    paredes.append(
        pygame.Rect(
            925,
            75,
            25,
            500
        )
    )


    # División izquierda superior.
    paredes.append(
        pygame.Rect(
            350,
            75,
            25,
            170
        )
    )


    # División izquierda inferior.
    paredes.append(
        pygame.Rect(
            350,
            345,
            25,
            230
        )
    )


    # División derecha.
    paredes.append(
        pygame.Rect(
            550,
            300,
            375,
            25
        )
    )


    return paredes


def crear_salida_sotano():

    # Zona de las escaleras
    # que regresan al Hospital.
    return pygame.Rect(
        440,
        50,
        120,
        100
    )


def dibujar_sotano(
    ventana,
    paredes
):

    # Fondo más oscuro.
    ventana.fill(
        (18, 22, 20)
    )


    # Piso.
    for x in range(
        0,
        1000,
        40
    ):

        pygame.draw.line(
            ventana,
            (28, 32, 30),
            (x, 0),
            (x, 650)
        )


    for y in range(
        0,
        650,
        40
    ):

        pygame.draw.line(
            ventana,
            (28, 32, 30),
            (0, y),
            (1000, y)
        )


    # Paredes.
    for pared in paredes:

        pygame.draw.rect(
            ventana,
            GRIS_OSCURO,
            pared
        )

        pygame.draw.rect(
            ventana,
            GRIS,
            pared,
            2
        )


    # Escaleras de regreso.
    pygame.draw.rect(
        ventana,
        (70, 60, 40),
        (460, 55, 80, 60)
    )


    for y in range(
        60,
        110,
        10
    ):

        pygame.draw.line(
            ventana,
            AMARILLO,
            (465, y),
            (535, y)
        )


    fuente = pygame.font.SysFont(
        "Arial",
        20
    )


    texto = fuente.render(
        "SOTANO DEL HOSPITAL",
        True,
        BLANCO
    )

    ventana.blit(
        texto,
        (390, 160)
    )


    texto = fuente.render(
        "GENERADORES",
        True,
        BLANCO
    )

    ventana.blit(
        texto,
        (100, 110)
    )


    texto = fuente.render(
        "ARCHIVO CLINICO",
        True,
        BLANCO
    )

    ventana.blit(
        texto,
        (620, 110)
    )


    texto = fuente.render(
        "ESCALERAS",
        True,
        AMARILLO
    )

    ventana.blit(
        texto,
        (450, 120)
    )


# ===================================
# COMISARÍA
# ===================================

def crear_paredes_comisaria():

    paredes = []


    paredes.append(
        pygame.Rect(
            50,
            50,
            900,
            25
        )
    )


    paredes.append(
        pygame.Rect(
            50,
            75,
            25,
            500
        )
    )


    paredes.append(
        pygame.Rect(
            925,
            75,
            25,
            500
        )
    )


    paredes.append(
        pygame.Rect(
            50,
            575,
            390,
            25
        )
    )


    paredes.append(
        pygame.Rect(
            560,
            575,
            390,
            25
        )
    )


    paredes.append(
        pygame.Rect(
            350,
            75,
            25,
            200
        )
    )


    paredes.append(
        pygame.Rect(
            350,
            375,
            25,
            200
        )
    )


    paredes.append(
        pygame.Rect(
            550,
            300,
            375,
            25
        )
    )


    return paredes


def crear_salida_comisaria():

    return pygame.Rect(
        440,
        520,
        120,
        80
    )


def dibujar_comisaria(
    ventana,
    paredes
):

    ventana.fill(
        (30, 32, 38)
    )


    # Piso.
    for x in range(
        0,
        1000,
        40
    ):

        pygame.draw.line(
            ventana,
            (42, 44, 50),
            (x, 0),
            (x, 650)
        )


    for y in range(
        0,
        650,
        40
    ):

        pygame.draw.line(
            ventana,
            (42, 44, 50),
            (0, y),
            (1000, y)
        )


    # Paredes.
    for pared in paredes:

        pygame.draw.rect(
            ventana,
            GRIS,
            pared
        )

        pygame.draw.rect(
            ventana,
            GRIS_CLARO,
            pared,
            2
        )


    fuente = pygame.font.SysFont(
        "Arial",
        20
    )


    texto = fuente.render(
        "RECEPCION",
        True,
        BLANCO
    )

    ventana.blit(
        texto,
        (100, 110)
    )


    texto = fuente.render(
        "ARCHIVO",
        True,
        BLANCO
    )

    ventana.blit(
        texto,
        (600, 110)
    )


    texto = fuente.render(
        "ARMERIA",
        True,
        BLANCO
    )

    ventana.blit(
        texto,
        (600, 380)
    )


    texto = fuente.render(
        "SALIDA",
        True,
        AMARILLO
    )

    ventana.blit(
        texto,
        (465, 540)
    )