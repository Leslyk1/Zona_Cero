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


from interfaz import (
    AMARILLO_NEON,
    BLANCO as BLANCO_UI,
    FONDO_INTERNO,
    GRIS_TEXTO,
    ROJO_COMBATE,
    VERDE_NEON,
    _caja_interna,
    _fuente,
    _panel,
    _tecla
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
        fuente = _fuente(
            14,
            True
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

        ventana.fill(
            (3, 11, 12)
        )


        # Cuadrícula oscura de fondo.
        for x in range(0, 1000, 40):

            pygame.draw.line(
                ventana,
                (12, 31, 31),
                (x, 0),
                (x, 650)
            )


        for y in range(0, 650, 40):

            pygame.draw.line(
                ventana,
                (12, 31, 31),
                (0, y),
                (1000, y)
            )


        panel_principal = pygame.Rect(
            80,
            40,
            840,
            560
        )


        _panel(
            ventana,
            panel_principal,
            AMARILLO_NEON,
            2,
            14
        )


        titulo = _fuente(28, True).render(
            "PUNTO DE EVACUACION",
            True,
            AMARILLO_NEON
        )


        ventana.blit(
            titulo,
            titulo.get_rect(center=(500, 82))
        )


        pygame.draw.line(
            ventana,
            AMARILLO_NEON,
            (120, 112),
            (880, 112),
            2
        )


        fuente_historia = _fuente(14)

        historia1 = fuente_historia.render(
            "El helicoptero militar esta listo para partir.",
            True,
            BLANCO_UI
        )

        historia2 = fuente_historia.render(
            "La horda se aproxima. Debes elegir una ruta final.",
            True,
            GRIS_TEXTO
        )


        ventana.blit(
            historia1,
            historia1.get_rect(center=(500, 145))
        )

        ventana.blit(
            historia2,
            historia2.get_rect(center=(500, 172))
        )


        opciones = [
            (
                "1",
                "SUBIR AL HELICOPTERO Y ESCAPAR",
                VERDE_NEON
            ),
            (
                "2",
                "QUEDARTE PARA DETENER A LA HORDA",
                AMARILLO_NEON
            ),
            (
                "3",
                "UTILIZAR EL SUERO EXPERIMENTAL",
                ROJO_COMBATE
            )
        ]


        posicion_y = 220


        for tecla, mensaje, color in opciones:

            caja = pygame.Rect(
                155,
                posicion_y,
                690,
                72
            )


            _panel(
                ventana,
                caja,
                color,
                2,
                9
            )


            _tecla(
                ventana,
                tecla,
                180,
                posicion_y + 16,
                color
            )


            texto = _fuente(15, True).render(
                mensaje,
                True,
                BLANCO_UI
            )


            ventana.blit(
                texto,
                (250, posicion_y + 27)
            )


            posicion_y += 88


        regresar = _fuente(13, True).render(
            "ESC = REGRESAR A LA CALLE",
            True,
            GRIS_TEXTO
        )


        ventana.blit(
            regresar,
            regresar.get_rect(center=(500, 560))
        )


    # ===================================
    # MOSTRAR FINAL
    # ===================================

    def dibujar_final(
        self,
        ventana,
        estado
    ):

        ventana.fill(
            (3, 11, 12)
        )


        # ===================================
        # FINAL EVACUACIÓN
        # ===================================

        if estado == "FINAL_EVACUACION":

            color = VERDE_NEON

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

            color = AMARILLO_NEON

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

            color = ROJO_COMBATE

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

        panel_final = pygame.Rect(
            100,
            70,
            800,
            500
        )


        _panel(
            ventana,
            panel_final,
            color,
            3,
            16
        )


        titulo = _fuente(30, True).render(
            titulo_final,
            True,
            color
        )


        ventana.blit(
            titulo,
            titulo.get_rect(center=(500, 135))
        )


        texto1 = _fuente(15).render(
            mensaje1,
            True,
            BLANCO_UI
        )


        ventana.blit(
            texto1,
            texto1.get_rect(center=(500, 225))
        )


        texto2 = _fuente(15).render(
            mensaje2,
            True,
            BLANCO_UI
        )


        ventana.blit(
            texto2,
            texto2.get_rect(center=(500, 260))
        )


        # -----------------------------------
        # INFORMACIÓN FORMAL
        # -----------------------------------

        caja = pygame.Rect(
            280,
            330,
            440,
            90
        )


        _caja_interna(
            ventana,
            caja,
            color
        )


        texto_aceptacion = _fuente(18, True).render(
            "ESTADO DE ACEPTACION",
            True,
            color
        )


        ventana.blit(
            texto_aceptacion,
            texto_aceptacion.get_rect(center=caja.center)
        )


        # -----------------------------------
        # PRUEBA
        # -----------------------------------

        prueba = _fuente(13, True).render(
            "R = REGRESAR A LA CALLE Y PROBAR OTRO FINAL",
            True,
            GRIS_TEXTO
        )


        ventana.blit(
            prueba,
            prueba.get_rect(center=(500, 500))
        )
