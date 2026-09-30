from arte import objeto as dibujar_objeto
# Importamos pygame
import pygame


# Importamos colores
from configuracion import (
    AMARILLO,
    GRIS_CLARO
)


# -----------------------------------
# CLASE OBJETO
# -----------------------------------

class Objeto:

    def __init__(
        self,
        nombre,
        x,
        y,
        color,
        cantidad=1
    ):

        # Nombre del objeto.
        self.nombre = nombre


        # Cantidad que entrega.
        self.cantidad = cantidad


        # Creamos su rectángulo.
        self.rectangulo = pygame.Rect(
            x,
            y,
            30,
            30
        )


        # Color temporal del objeto.
        self.color = color


        # Zona de interacción.
        self.zona_interaccion = pygame.Rect(
            x - 25,
            y - 25,
            80,
            80
        )


        # Indica si ya fue recogido.
        self.recogido = False


    # -----------------------------------
    # DIBUJAR OBJETO
    # -----------------------------------

    def dibujar(self, ventana):
        if not self.recogido:
            # Diego: iconos reconocibles para medicina, pistola y munición.
            dibujar_objeto(ventana, self.rectangulo, self.nombre)


    # -----------------------------------
    # RECOGER OBJETO
    # -----------------------------------

    def recoger(
        self,
        inventario
    ):

        # Revisamos que todavía
        # esté disponible.
        if self.recogido == False:

            # Agregamos el objeto
            # al inventario.
            inventario.agregar(
                self.nombre,
                self.cantidad
            )


            # Marcamos que fue recogido.
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

        # La pistola aparecerá
        # dentro de la armería.
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

        # Este objeto entregará
        # 12 balas.
        super().__init__(
            "Balas",
            820,
            390,
            AMARILLO,
            12
        )