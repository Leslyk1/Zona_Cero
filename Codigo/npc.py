from arte import (
    personaje,
    etiqueta,
    MENTA
)

import pygame


# ===================================
# CLASE NPC
# ===================================

class NPC:

    def __init__(
        self,
        nombre,
        x,
        y,
        tipo_sprite
    ):

        self.nombre = nombre

        self.tipo_sprite = tipo_sprite

        self.rectangulo = pygame.Rect(
            x,
            y,
            40,
            40
        )

        self.zona_interaccion = pygame.Rect(
            x - 35,
            y - 35,
            110,
            110
        )


    def dibujar(
        self,
        ventana
    ):

        personaje(
            ventana,
            self.rectangulo,
            self.tipo_sprite
        )

        etiqueta(
            ventana,
            self.nombre,
            (
                self.rectangulo.centerx,
                self.rectangulo.top - 30
            ),
            MENTA
        )


# ===================================
# ELENA
# ===================================

class Elena(NPC):

    def __init__(self):

        super().__init__(
            "Elena",
            680,
            220,
            "elena"
        )


    def hablar(
        self,
        mision,
        inventario,
        gramatica
    ):

        # Jugador ya tiene medicamento.
        if inventario.tiene(
            "Medicamento"
        ):

            if mision.completada == False:

                if mision.activa == False:

                    mision.activar()

                mision.completar()

            return gramatica.generar(
                "<DIALOGO_FINAL>"
            )


        # Primera conversación.
        if (
            mision.activa == False
            and
            mision.completada == False
        ):

            mision.activar()

            mision.descripcion = (
                gramatica.generar(
                    "<MISION>"
                )
            )

            return gramatica.generar(
                "<DIALOGO_INICIO>"
            )


        # Misión activa.
        elif mision.activa == True:

            return gramatica.generar(
                "<DIALOGO_RECORDATORIO>"
            )


        # Misión completada.
        else:

            return gramatica.generar(
                "<DIALOGO_FINAL>"
            )


# ===================================
# MARCOS
# ===================================

class Marcos(NPC):

    def __init__(self):

        super().__init__(
            "Marcos",
            210,
            220,
            "marcos"
        )


    # ===================================
    # HABLAR CON MARCOS
    # ===================================

    def hablar(
        self,
        mision,
        inventario,
        gramatica
    ):

        # -----------------------------------
        # MISIÓN YA COMPLETADA
        # -----------------------------------

        if mision.completada == True:

            return gramatica.generar(
                "<DIALOGO_MARCOS_FINAL>"
            )


        # -----------------------------------
        # JUGADOR TIENE LA RADIO
        # -----------------------------------

        if inventario.tiene(
            "Radio"
        ):

            # Quitamos la radio
            # del inventario.
            inventario.usar(
                "Radio",
                1
            )

            # Completamos la misión.
            mision.completar()

            # Recompensa.
            if inventario.tiene(
                "Tarjeta Militar"
            ) == False:

                inventario.agregar(
                    "Tarjeta Militar",
                    1
                )

            return gramatica.generar(
                "<DIALOGO_MARCOS_FINAL>"
            )


        # -----------------------------------
        # PRIMERA CONVERSACIÓN
        # -----------------------------------

        if mision.activa == False:

            mision.activar()

            mision.descripcion = (
                gramatica.generar(
                    "<MISION_MARCOS>"
                )
            )

            return gramatica.generar(
                "<DIALOGO_MARCOS_INICIO>"
            )


        # -----------------------------------
        # MISIÓN ACTIVA
        # -----------------------------------

        return gramatica.generar(
            "<DIALOGO_MARCOS_RECORDATORIO>"
        )