from arte import escenario
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


def dibujar_refugio(ventana, paredes):
    # Diego: nueva capa de arte; las paredes y sus colisiones siguen intactas.
    escenario(ventana, paredes, "REFUGIO")


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


def dibujar_calle(ventana, paredes):
    # Diego: nueva capa de arte; las paredes y sus colisiones siguen intactas.
    escenario(ventana, paredes, "CALLE")


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


def dibujar_hospital(ventana, paredes):
    # Diego: nueva capa de arte; las paredes y sus colisiones siguen intactas.
    escenario(ventana, paredes, "HOSPITAL")


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


def dibujar_sotano(ventana, paredes):
    # Diego: nueva capa de arte; las paredes y sus colisiones siguen intactas.
    escenario(ventana, paredes, "SOTANO_HOSPITAL")


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


def dibujar_comisaria(ventana, paredes):
    # Diego: nueva capa de arte; las paredes y sus colisiones siguen intactas.
    escenario(ventana, paredes, "COMISARIA")
