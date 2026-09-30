# Importamos pygame
import pygame


# Importamos colores
from configuracion import (
    ROJO,
    BLANCO
)


# -----------------------------------
# CLASE ENEMIGO
# -----------------------------------

class Enemigo:

    def __init__(
        self,
        nombre,
        x,
        y,
        vida,
        danio
    ):

        # Nombre del enemigo.
        self.nombre = nombre


        # Rectángulo del enemigo.
        self.rectangulo = pygame.Rect(
            x,
            y,
            40,
            40
        )


        # Zona utilizada para iniciar
        # el combate.
        self.zona_interaccion = pygame.Rect(
            x - 45,
            y - 45,
            130,
            130
        )


        # Vida máxima.
        self.vida_maxima = vida


        # Vida actual.
        self.vida = vida


        # Daño.
        self.danio = danio


        # El enemigo comienza vivo.
        self.vivo = True


    # -----------------------------------
    # RECIBIR DAÑO
    # -----------------------------------

    def recibir_dano(
        self,
        cantidad
    ):

        # Restamos vida.
        self.vida = (
            self.vida - cantidad
        )


        # Evitamos valores negativos.
        if self.vida < 0:

            self.vida = 0


        # Si llega a cero...
        if self.vida == 0:

            self.vivo = False


    # -----------------------------------
    # REINICIAR
    # -----------------------------------

    def reiniciar(self):

        # Recuperamos toda la vida.
        self.vida = (
            self.vida_maxima
        )


        # Volvemos a marcararlo
        # como vivo.
        self.vivo = True


    # -----------------------------------
    # DIBUJAR
    # -----------------------------------

    def dibujar(
        self,
        ventana
    ):

        # Solo dibujamos
        # enemigos vivos.
        if self.vivo == True:

            # Dibujamos enemigo.
            pygame.draw.rect(
                ventana,
                ROJO,
                self.rectangulo
            )


            # Fuente.
            fuente = pygame.font.SysFont(
                "Consolas",
                18,
                bold=True
            )


            # Nombre.
            texto = fuente.render(
                self.nombre,
                True,
                BLANCO
            )


            ventana.blit(
                texto,
                (
                    self.rectangulo.x - 30,
                    self.rectangulo.y - 25
                )
            )


# ===================================
# ZOMBI POLICÍA
# ===================================

class ZombiPolicia(Enemigo):

    def __init__(self):

        super().__init__(
            "Zombi Policia",
            700,
            420,
            40,
            10
        )


# ===================================
# ZOMBI CORREDOR
# ===================================

class ZombiCorredor(Enemigo):

    def __init__(self):

        # El corredor será más fuerte
        # que el Zombi Policía.
        #
        # Vida:
        # 70
        #
        # Daño:
        # 15
        super().__init__(
            "Zombi Corredor",
            700,
            400,
            70,
            15
        )
