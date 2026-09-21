# Importamos pygame
import pygame


# Importamos colores
from configuracion import (
    BLANCO,
    VERDE
)


# -----------------------------------
# CLASE NPC
# -----------------------------------

class NPC:

    def __init__(
        self,
        nombre,
        x,
        y
    ):

        # Nombre del NPC.
        self.nombre = nombre


        # Rectángulo.
        self.rectangulo = pygame.Rect(
            x,
            y,
            40,
            40
        )


        # Zona utilizada para
        # interactuar.
        self.zona_interaccion = pygame.Rect(
            x - 35,
            y - 35,
            110,
            110
        )


    # -----------------------------------
    # DIBUJAR NPC
    # -----------------------------------

    def dibujar(
        self,
        ventana
    ):

        pygame.draw.rect(
            ventana,
            BLANCO,
            self.rectangulo
        )


        fuente = pygame.font.SysFont(
            "Arial",
            16
        )


        texto = fuente.render(
            self.nombre,
            True,
            VERDE
        )


        ventana.blit(
            texto,
            (
                self.rectangulo.x - 5,
                self.rectangulo.y - 25
            )
        )


# ===================================
# ELENA
# ===================================

class Elena(NPC):

    def __init__(self):

        super().__init__(
            "Elena",
            680,
            220
        )


    # ===================================
    # HABLAR CON ELENA
    # ===================================

    def hablar(
        self,
        mision,
        inventario,
        gramatica
    ):

        # -----------------------------------
        # JUGADOR TIENE MEDICAMENTO
        # -----------------------------------

        if inventario.tiene(
            "Medicamento"
        ):

            # Si todavía no se había
            # completado la misión.
            if mision.completada == False:

                # Si tampoco estaba activa,
                # la activamos primero.
                if mision.activa == False:

                    mision.activar()


                # Completamos la misión.
                mision.completar()


            # -----------------------------------
            # DIÁLOGO GENERADO POR LA GLC
            # -----------------------------------

            return gramatica.generar(
                "<DIALOGO_FINAL>"
            )


        # -----------------------------------
        # PRIMERA VEZ QUE HABLAMOS
        # -----------------------------------

        if (
            mision.activa == False
            and
            mision.completada == False
        ):

            # Activamos misión.
            mision.activar()


            # La descripción de la misión
            # también sale de la gramática.
            mision.descripcion = (
                gramatica.generar(
                    "<MISION>"
                )
            )


            # Generamos diálogo inicial.
            return gramatica.generar(
                "<DIALOGO_INICIO>"
            )


        # -----------------------------------
        # MISIÓN ACTIVA
        # -----------------------------------

        elif mision.activa == True:

            # Generamos un recordatorio
            # mediante nuestra GLC.
            return gramatica.generar(
                "<DIALOGO_RECORDATORIO>"
            )


        # -----------------------------------
        # MISIÓN COMPLETADA
        # -----------------------------------

        else:

            return gramatica.generar(
                "<DIALOGO_FINAL>"
            )