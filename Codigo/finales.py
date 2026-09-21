# Importamos pygame
import pygame


# Importamos colores
from configuracion import (
    NEGRO,
    BLANCO,
    VERDE,
    AMARILLO,
    ROJO,
    GRIS,
    GRIS_CLARO
)


# ===================================
# SISTEMA DE FINALES
# ===================================

class SistemaFinales:

    def __init__(self):

        # Zona que estará ubicada
        # en la calle.
        #
        # Cuando el jugador complete
        # los objetivos podrá entrar
        # al punto de evacuación.
        self.zona_entrada = pygame.Rect(
            850,
            240,
            120,
            130
        )


    # ===================================
    # REVISAR REQUISITOS
    # ===================================

    def requisitos_completos(
        self,
        mision,
        zombi_comisaria,
        zombi_sotano
    ):

        # Para desbloquear el final:
        #
        # 1. La misión de Elena debe
        #    estar completada.
        #
        # 2. El Zombi Policía debe
        #    estar derrotado.
        #
        # 3. El Zombi Corredor debe
        #    estar derrotado.

        if (
            mision.completada == True
            and
            zombi_comisaria.vivo == False
            and
            zombi_sotano.vivo == False
        ):

            return True


        return False


    # ===================================
    # DIBUJAR ENTRADA EN LA CALLE
    # ===================================

    def dibujar_entrada_calle(
        self,
        ventana,
        desbloqueado
    ):

        # Si ya está desbloqueado
        # utilizamos verde.
        if desbloqueado == True:

            color = VERDE

        else:

            # Si todavía faltan objetivos
            # utilizamos rojo.
            color = ROJO


        # Dibujamos una especie
        # de puerta militar.
        pygame.draw.rect(
            ventana,
            GRIS,
            (
                880,
                245,
                90,
                120
            )
        )


        pygame.draw.rect(
            ventana,
            color,
            (
                880,
                245,
                90,
                120
            ),
            3
        )


        # Líneas de la puerta.
        pygame.draw.line(
            ventana,
            GRIS_CLARO,
            (910, 250),
            (910, 360),
            3
        )


        pygame.draw.line(
            ventana,
            GRIS_CLARO,
            (940, 250),
            (940, 360),
            3
        )


        # Texto.
        fuente = pygame.font.SysFont(
            "Arial",
            16
        )


        texto = fuente.render(
            "EVACUACION",
            True,
            color
        )


        ventana.blit(
            texto,
            (870, 215)
        )


    # ===================================
    # MOSTRAR MENÚ DE DECISIÓN FINAL
    # ===================================

    def dibujar_menu_final(
        self,
        ventana
    ):

        # Limpiamos completamente
        # la pantalla.
        ventana.fill(
            NEGRO
        )


        # -----------------------------------
        # TÍTULO
        # -----------------------------------

        fuente_titulo = pygame.font.SysFont(
            "Arial",
            34
        )


        titulo = fuente_titulo.render(
            "PUNTO DE EVACUACION",
            True,
            AMARILLO
        )


        ventana.blit(
            titulo,
            (315, 70)
        )


        # -----------------------------------
        # HISTORIA
        # -----------------------------------

        fuente = pygame.font.SysFont(
            "Arial",
            19
        )


        texto1 = fuente.render(
            "El helicoptero militar esta listo para partir.",
            True,
            BLANCO
        )


        ventana.blit(
            texto1,
            (275, 145)
        )


        texto2 = fuente.render(
            "Pero la horda se aproxima y debes tomar una decision.",
            True,
            BLANCO
        )


        ventana.blit(
            texto2,
            (245, 180)
        )


        # -----------------------------------
        # OPCIÓN 1
        # -----------------------------------

        caja1 = pygame.Rect(
            180,
            245,
            640,
            65
        )


        pygame.draw.rect(
            ventana,
            GRIS,
            caja1
        )


        pygame.draw.rect(
            ventana,
            VERDE,
            caja1,
            2
        )


        opcion1 = fuente.render(
            "1 - Subir al helicoptero y escapar",
            True,
            BLANCO
        )


        ventana.blit(
            opcion1,
            (250, 267)
        )


        # -----------------------------------
        # OPCIÓN 2
        # -----------------------------------

        caja2 = pygame.Rect(
            180,
            330,
            640,
            65
        )


        pygame.draw.rect(
            ventana,
            GRIS,
            caja2
        )


        pygame.draw.rect(
            ventana,
            AMARILLO,
            caja2,
            2
        )


        opcion2 = fuente.render(
            "2 - Quedarte para detener a la horda",
            True,
            BLANCO
        )


        ventana.blit(
            opcion2,
            (235, 352)
        )


        # -----------------------------------
        # OPCIÓN 3
        # -----------------------------------

        caja3 = pygame.Rect(
            180,
            415,
            640,
            65
        )


        pygame.draw.rect(
            ventana,
            GRIS,
            caja3
        )


        pygame.draw.rect(
            ventana,
            ROJO,
            caja3,
            2
        )


        opcion3 = fuente.render(
            "3 - Utilizar el suero experimental",
            True,
            BLANCO
        )


        ventana.blit(
            opcion3,
            (250, 437)
        )


        # -----------------------------------
        # REGRESAR
        # -----------------------------------

        fuente_pequena = pygame.font.SysFont(
            "Arial",
            16
        )


        regresar = fuente_pequena.render(
            "ESC - Regresar a la calle",
            True,
            GRIS_CLARO
        )


        ventana.blit(
            regresar,
            (400, 525)
        )


    # ===================================
    # MOSTRAR FINAL
    # ===================================

    def dibujar_final(
        self,
        ventana,
        estado
    ):

        # Limpiamos pantalla.
        ventana.fill(
            NEGRO
        )


        fuente_titulo = pygame.font.SysFont(
            "Arial",
            36
        )


        fuente = pygame.font.SysFont(
            "Arial",
            20
        )


        fuente_pequena = pygame.font.SysFont(
            "Arial",
            16
        )


        # ===================================
        # FINAL EVACUACIÓN
        # ===================================

        if estado == "FINAL_EVACUACION":

            color = VERDE

            titulo_final = (
                "FINAL: EVACUACION"
            )


            mensaje1 = (
                "Logras subir al helicoptero junto a los sobrevivientes."
            )


            mensaje2 = (
                "El refugio queda atras mientras comienza una nueva esperanza."
            )


        # ===================================
        # FINAL SACRIFICIO
        # ===================================

        elif estado == "FINAL_SACRIFICIO":

            color = AMARILLO

            titulo_final = (
                "FINAL: SACRIFICIO"
            )


            mensaje1 = (
                "Decides quedarte para detener el avance de la horda."
            )


            mensaje2 = (
                "Tu sacrificio permite que los demas sobrevivientes escapen."
            )


        # ===================================
        # FINAL INFECTADO
        # ===================================

        else:

            color = ROJO

            titulo_final = (
                "FINAL: INFECTADO"
            )


            mensaje1 = (
                "Utilizas el suero experimental encontrado durante la crisis."
            )


            mensaje2 = (
                "El compuesto falla y la infeccion termina apoderandose de ti."
            )


        # -----------------------------------
        # MOSTRAMOS FINAL
        # -----------------------------------

        titulo = fuente_titulo.render(
            titulo_final,
            True,
            color
        )


        ventana.blit(
            titulo,
            (330, 150)
        )


        texto1 = fuente.render(
            mensaje1,
            True,
            BLANCO
        )


        ventana.blit(
            texto1,
            (190, 245)
        )


        texto2 = fuente.render(
            mensaje2,
            True,
            BLANCO
        )


        ventana.blit(
            texto2,
            (170, 285)
        )


        # -----------------------------------
        # INFORMACIÓN FORMAL
        # -----------------------------------

        caja = pygame.Rect(
            300,
            370,
            400,
            80
        )


        pygame.draw.rect(
            ventana,
            GRIS,
            caja
        )


        pygame.draw.rect(
            ventana,
            color,
            caja,
            2
        )


        texto_aceptacion = fuente.render(
            "ESTADO DE ACEPTACION",
            True,
            color
        )


        ventana.blit(
            texto_aceptacion,
            (380, 395)
        )


        # -----------------------------------
        # PRUEBA
        # -----------------------------------

        prueba = fuente_pequena.render(
            "R - Regresar a la calle para probar otro final",
            True,
            GRIS_CLARO
        )


        ventana.blit(
            prueba,
            (335, 520)
        )