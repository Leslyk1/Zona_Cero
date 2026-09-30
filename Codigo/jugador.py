from arte import personaje
# Importamos pygame
import pygame

# Importamos configuraciones
from configuracion import (
    VERDE,
    ANCHO,
    ALTO
)


# -----------------------------------
# CLASE JUGADOR
# -----------------------------------

class Jugador:

    # Datos iniciales del jugador
    def __init__(self):

        # Creamos el rectángulo del jugador
        self.rectangulo = pygame.Rect(
            150,
            150,
            40,
            40
        )

        # Velocidad del jugador
        self.velocidad = 5
        self.espalda = False
        self.moviendo = False

        # Vida máxima del jugador
        self.vida_maxima = 100

        # Vida actual del jugador
        self.vida = 100


    # -----------------------------------
    # MOVIMIENTO DEL JUGADOR
    # -----------------------------------

    def mover(self, paredes):

        # Detectamos las teclas presionadas
        teclas = pygame.key.get_pressed()

        # Movimiento horizontal
        movimiento_x = 0

        # Movimiento vertical
        movimiento_y = 0


        self.moviendo = False

        # W = arriba
        if teclas[pygame.K_w]:
            movimiento_y = -self.velocidad


        # S = abajo
        if teclas[pygame.K_s]:
            movimiento_y = self.velocidad


        # A = izquierda
        if teclas[pygame.K_a]:
            movimiento_x = -self.velocidad


        # D = derecha
        if teclas[pygame.K_d]:
            movimiento_x = self.velocidad


        # -----------------------------------
        # MOVIMIENTO HORIZONTAL
        # -----------------------------------

        self.moviendo = bool(movimiento_x or movimiento_y)
        if movimiento_y:
            self.espalda = movimiento_y < 0

        self.rectangulo.x = (
            self.rectangulo.x + movimiento_x
        )


        # Revisamos colisiones
        for pared in paredes:

            if self.rectangulo.colliderect(pared):

                # Si iba hacia la derecha
                if movimiento_x > 0:
                    self.rectangulo.right = pared.left

                # Si iba hacia la izquierda
                if movimiento_x < 0:
                    self.rectangulo.left = pared.right


        # -----------------------------------
        # MOVIMIENTO VERTICAL
        # -----------------------------------

        self.rectangulo.y = (
            self.rectangulo.y + movimiento_y
        )


        # Revisamos colisiones
        for pared in paredes:

            if self.rectangulo.colliderect(pared):

                # Si iba hacia abajo
                if movimiento_y > 0:
                    self.rectangulo.bottom = pared.top

                # Si iba hacia arriba
                if movimiento_y < 0:
                    self.rectangulo.top = pared.bottom


        # -----------------------------------
        # LÍMITES DE LA PANTALLA
        # -----------------------------------

        if self.rectangulo.left < 0:
            self.rectangulo.left = 0


        if self.rectangulo.right > ANCHO:
            self.rectangulo.right = ANCHO


        if self.rectangulo.top < 0:
            self.rectangulo.top = 0


        if self.rectangulo.bottom > ALTO:
            self.rectangulo.bottom = ALTO


    # -----------------------------------
    # CAMBIAR POSICIÓN
    # -----------------------------------

    def cambiar_posicion(self, x, y):

        self.rectangulo.x = x

        self.rectangulo.y = y


    # -----------------------------------
    # RECIBIR DAÑO
    # -----------------------------------

    def recibir_dano(self, cantidad):

        # Restamos la cantidad recibida
        # de la vida actual.
        self.vida = self.vida - cantidad


        # Evitamos que la vida
        # sea menor que cero.
        if self.vida < 0:

            self.vida = 0


    # -----------------------------------
    # CURAR AL JUGADOR
    # -----------------------------------

    def curar(self, cantidad):

        # Sumamos vida.
        self.vida = self.vida + cantidad


        # Evitamos superar la vida máxima.
        if self.vida > self.vida_maxima:

            self.vida = self.vida_maxima


    # -----------------------------------
    # REVISAR SI SIGUE VIVO
    # -----------------------------------

    def esta_vivo(self):

        if self.vida > 0:

            return True

        else:

            return False


    # -----------------------------------
    # DIBUJAR JUGADOR
    # -----------------------------------

    def dibujar(self, ventana):
        # Diego: dibujo del superviviente, conservando el rectángulo de colisión.
        personaje(ventana, self.rectangulo, "superviviente", self.espalda, self.moviendo)
