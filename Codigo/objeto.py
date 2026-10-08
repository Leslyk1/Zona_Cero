from arte import objeto as dibujar_objeto

import pygame

from configuracion import (
    AMARILLO,
    GRIS_CLARO
)


# ===================================
# CLASE OBJETO
# ===================================

class Objeto:

    def __init__(
        self,
        nombre,
        x,
        y,
        color,
        cantidad=1
    ):

        self.nombre = nombre
        self.cantidad = cantidad

        self.rectangulo = pygame.Rect(
            x,
            y,
            30,
            30
        )

        self.color = color

        self.zona_interaccion = pygame.Rect(
            x - 25,
            y - 25,
            80,
            80
        )

        self.recogido = False


    def dibujar(self, ventana):

        if self.recogido == False:

            dibujar_objeto(
                ventana,
                self.rectangulo,
                self.nombre
            )


    def recoger(
        self,
        inventario
    ):

        if self.recogido == False:

            inventario.agregar(
                self.nombre,
                self.cantidad
            )

            self.recogido = True

            return True

        return False


# ===================================
# MEDICAMENTO
# ===================================

class Medicamento(Objeto):

    def __init__(self):

        super().__init__(
            "Medicamento",
            720,
            430,
            AMARILLO,
            1
        )


# ===================================
# PISTOLA
# ===================================

class Pistola(Objeto):

    def __init__(self):

        super().__init__(
            "Pistola",
            610,
            390,
            GRIS_CLARO,
            1
        )


# ===================================
# MUNICIÓN
# ===================================

class Municion(Objeto):

    def __init__(self):

        super().__init__(
            "Balas",
            820,
            390,
            AMARILLO,
            12
        )


# ===================================
# RADIO
# ===================================

class Radio(Objeto):

    def __init__(self):

        # Radio ubicada en el archivo
        # de la comisaría.
        super().__init__(
            "Radio",
            700,
            200,
            AMARILLO,
            1
        )