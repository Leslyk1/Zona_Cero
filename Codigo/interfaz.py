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
# MOSTRAR INTERACCIÓN
# ===================================

def mostrar_interaccion(
    ventana,
    mensaje
):

    fuente = pygame.font.SysFont(
        "Arial",
        22
    )


    fondo = pygame.Rect(
        300,
        570,
        400,
        55
    )


    pygame.draw.rect(
        ventana,
        NEGRO,
        fondo
    )


    pygame.draw.rect(
        ventana,
        VERDE,
        fondo,
        2
    )


    texto = fuente.render(
        mensaje,
        True,
        BLANCO
    )


    ventana.blit(
        texto,
        (330, 585)
    )


# ===================================
# MOSTRAR ESTADO DEL AFN
# ===================================

def mostrar_estado_afn(
    ventana,
    estado
):

    fuente = pygame.font.SysFont(
        "Arial",
        18
    )


    texto = fuente.render(
        "Estado AFN: "
        + estado,
        True,
        VERDE
    )


    ventana.blit(
        texto,
        (20, 15)
    )


    # Indicamos que podemos
    # visualizar la gramática.
    fuente_pequena = pygame.font.SysFont(
        "Arial",
        13
    )


    ayuda = fuente_pequena.render(
        "G = Ver GLC / BNF",
        True,
        BLANCO
    )


    ventana.blit(
        ayuda,
        (275, 18)
    )


# ===================================
# MOSTRAR VIDA
# ===================================

def mostrar_vida(
    ventana,
    jugador
):

    x = 20
    y = 190

    ancho_barra = 200
    alto_barra = 25


    porcentaje = (
        jugador.vida
        /
        jugador.vida_maxima
    )


    ancho_vida = int(
        ancho_barra * porcentaje
    )


    fuente = pygame.font.SysFont(
        "Arial",
        16
    )


    texto = fuente.render(
        "VIDA: "
        + str(jugador.vida)
        + "/"
        + str(jugador.vida_maxima),
        True,
        BLANCO
    )


    ventana.blit(
        texto,
        (x, y - 25)
    )


    pygame.draw.rect(
        ventana,
        NEGRO,
        (
            x,
            y,
            ancho_barra,
            alto_barra
        )
    )


    pygame.draw.rect(
        ventana,
        ROJO,
        (
            x,
            y,
            ancho_vida,
            alto_barra
        )
    )


    pygame.draw.rect(
        ventana,
        BLANCO,
        (
            x,
            y,
            ancho_barra,
            alto_barra
        ),
        2
    )


# ===================================
# MOSTRAR DIÁLOGO
# ===================================

def mostrar_dialogo(
    ventana,
    mensaje
):

    fondo = pygame.Rect(
        120,
        470,
        760,
        80
    )


    pygame.draw.rect(
        ventana,
        NEGRO,
        fondo
    )


    pygame.draw.rect(
        ventana,
        VERDE,
        fondo,
        2
    )


    fuente = pygame.font.SysFont(
        "Arial",
        19
    )


    texto = fuente.render(
        mensaje,
        True,
        BLANCO
    )


    ventana.blit(
        texto,
        (145, 500)
    )


# ===================================
# MOSTRAR MISIÓN
# ===================================

def mostrar_mision(
    ventana,
    mision
):

    if (
        mision.activa == False
        and
        mision.completada == False
    ):

        return


    fondo = pygame.Rect(
        660,
        15,
        320,
        80
    )


    pygame.draw.rect(
        ventana,
        NEGRO,
        fondo
    )


    if mision.activa == True:

        color = AMARILLO

        titulo_mision = (
            "MISION ACTUAL"
        )

    else:

        color = VERDE

        titulo_mision = (
            "MISION COMPLETADA"
        )


    pygame.draw.rect(
        ventana,
        color,
        fondo,
        2
    )


    fuente_titulo = pygame.font.SysFont(
        "Arial",
        16
    )


    titulo = fuente_titulo.render(
        titulo_mision,
        True,
        color
    )


    ventana.blit(
        titulo,
        (680, 25)
    )


    fuente = pygame.font.SysFont(
        "Arial",
        14
    )


    texto = fuente.render(
        mision.descripcion,
        True,
        BLANCO
    )


    ventana.blit(
        texto,
        (680, 55)
    )


# ===================================
# MOSTRAR INVENTARIO
# ===================================

def mostrar_inventario(
    ventana,
    inventario
):

    fondo = pygame.Rect(
        20,
        45,
        240,
        110
    )


    pygame.draw.rect(
        ventana,
        NEGRO,
        fondo
    )


    pygame.draw.rect(
        ventana,
        VERDE,
        fondo,
        2
    )


    fuente_titulo = pygame.font.SysFont(
        "Arial",
        16
    )


    titulo = fuente_titulo.render(
        "INVENTARIO",
        True,
        VERDE
    )


    ventana.blit(
        titulo,
        (35, 55)
    )


    fuente = pygame.font.SysFont(
        "Arial",
        15
    )


    posicion_y = 85


    if len(
        inventario.objetos
    ) == 0:

        texto = fuente.render(
            "Vacio",
            True,
            BLANCO
        )


        ventana.blit(
            texto,
            (35, posicion_y)
        )


    else:

        for nombre in inventario.objetos:

            cantidad = (
                inventario.objetos[
                    nombre
                ]
            )


            texto = fuente.render(
                nombre
                + " x"
                + str(cantidad),
                True,
                BLANCO
            )


            ventana.blit(
                texto,
                (35, posicion_y)
            )


            posicion_y = (
                posicion_y + 20
            )


# ===================================
# MOSTRAR PILA
# ===================================

def mostrar_pila_mundo(
    ventana,
    pila_mundo
):

    fondo = pygame.Rect(
        735,
        110,
        245,
        190
    )


    pygame.draw.rect(
        ventana,
        NEGRO,
        fondo
    )


    pygame.draw.rect(
        ventana,
        AMARILLO,
        fondo,
        2
    )


    fuente_titulo = pygame.font.SysFont(
        "Arial",
        16
    )


    titulo = fuente_titulo.render(
        "PILA DEL MUNDO",
        True,
        AMARILLO
    )


    ventana.blit(
        titulo,
        (760, 120)
    )


    fuente_operacion = pygame.font.SysFont(
        "Arial",
        13
    )


    texto_operacion = (
        fuente_operacion.render(
            "Operacion: "
            + pila_mundo.ultima_operacion,
            True,
            BLANCO
        )
    )


    ventana.blit(
        texto_operacion,
        (750, 145)
    )


    # Pila vacía.
    if len(
        pila_mundo.elementos
    ) == 0:

        fuente = pygame.font.SysFont(
            "Arial",
            16
        )


        texto = fuente.render(
            "Pila vacia",
            True,
            GRIS_CLARO
        )


        ventana.blit(
            texto,
            (815, 205)
        )


    # Pila con elementos.
    else:

        fuente_tope = pygame.font.SysFont(
            "Arial",
            13
        )


        texto_tope = fuente_tope.render(
            "TOPE",
            True,
            VERDE
        )


        ventana.blit(
            texto_tope,
            (755, 175)
        )


        posicion_y = 195


        for posicion in range(
            len(pila_mundo.elementos) - 1,
            -1,
            -1
        ):

            lugar = (
                pila_mundo.elementos[
                    posicion
                ]
            )


            caja = pygame.Rect(
                770,
                posicion_y,
                175,
                32
            )


            pygame.draw.rect(
                ventana,
                GRIS,
                caja
            )


            pygame.draw.rect(
                ventana,
                BLANCO,
                caja,
                2
            )


            fuente = pygame.font.SysFont(
                "Arial",
                14
            )


            texto = fuente.render(
                lugar,
                True,
                BLANCO
            )


            ventana.blit(
                texto,
                (
                    790,
                    posicion_y + 7
                )
            )


            posicion_y = (
                posicion_y + 36
            )


# ===================================
# MOSTRAR COMBATE
# ===================================

def mostrar_combate(
    ventana,
    combate,
    jugador,
    inventario
):

    fondo = pygame.Rect(
        130,
        100,
        740,
        450
    )


    pygame.draw.rect(
        ventana,
        NEGRO,
        fondo
    )


    pygame.draw.rect(
        ventana,
        ROJO,
        fondo,
        3
    )


    fuente_titulo = pygame.font.SysFont(
        "Arial",
        28
    )


    titulo = fuente_titulo.render(
        "COMBATE",
        True,
        ROJO
    )


    ventana.blit(
        titulo,
        (430, 120)
    )


    fuente = pygame.font.SysFont(
        "Arial",
        20
    )


    enemigo = combate.enemigo


    texto_enemigo = fuente.render(
        enemigo.nombre
        + " - VIDA: "
        + str(enemigo.vida)
        + "/"
        + str(enemigo.vida_maxima),
        True,
        BLANCO
    )


    ventana.blit(
        texto_enemigo,
        (190, 175)
    )


    texto_jugador = fuente.render(
        "Jugador - VIDA: "
        + str(jugador.vida)
        + "/"
        + str(jugador.vida_maxima),
        True,
        VERDE
    )


    ventana.blit(
        texto_jugador,
        (190, 215)
    )


    cantidad_balas = (
        inventario.obtener_cantidad(
            "Balas"
        )
    )


    texto_balas = fuente.render(
        "Balas: "
        + str(cantidad_balas),
        True,
        AMARILLO
    )


    ventana.blit(
        texto_balas,
        (580, 215)
    )


    texto_estado = fuente.render(
        "Estado: "
        + combate.estado,
        True,
        AMARILLO
    )


    ventana.blit(
        texto_estado,
        (190, 265)
    )


    fuente_mensaje = pygame.font.SysFont(
        "Arial",
        17
    )


    mensaje = fuente_mensaje.render(
        combate.mensaje,
        True,
        BLANCO
    )


    ventana.blit(
        mensaje,
        (190, 305)
    )


    fuente_pequena = pygame.font.SysFont(
        "Arial",
        13
    )


    texto_transicion = (
        fuente_pequena.render(
            "Transicion: "
            + combate.transicion,
            True,
            VERDE
        )
    )


    ventana.blit(
        texto_transicion,
        (160, 350)
    )


    if combate.estado == "ELEGIR_ACCION":

        opcion1 = fuente.render(
            "1 - GOLPEAR",
            True,
            BLANCO
        )


        ventana.blit(
            opcion1,
            (180, 410)
        )


        if (
            inventario.tiene(
                "Pistola"
            )
            and
            inventario.tiene(
                "Balas"
            )
        ):

            color_disparo = BLANCO

        else:

            color_disparo = ROJO


        opcion2 = fuente.render(
            "2 - DISPARAR",
            True,
            color_disparo
        )


        ventana.blit(
            opcion2,
            (390, 410)
        )


        opcion3 = fuente.render(
            "3 - DEFENDER",
            True,
            BLANCO
        )


        ventana.blit(
            opcion3,
            (600, 410)
        )


    elif combate.estado == "VICTORIA":

        texto = fuente.render(
            "Presiona ENTER para continuar",
            True,
            VERDE
        )


        ventana.blit(
            texto,
            (335, 430)
        )


    elif combate.estado == "DERROTA":

        texto = fuente.render(
            "Presiona ENTER para reiniciar",
            True,
            ROJO
        )


        ventana.blit(
            texto,
            (335, 430)
        )


# ===================================
# MOSTRAR GLC Y BNF
# ===================================

def mostrar_gramatica(
    ventana,
    gramatica
):

    # -----------------------------------
    # FONDO
    # -----------------------------------

    fondo = pygame.Rect(
        50,
        45,
        900,
        560
    )


    pygame.draw.rect(
        ventana,
        NEGRO,
        fondo
    )


    pygame.draw.rect(
        ventana,
        AMARILLO,
        fondo,
        3
    )


    # -----------------------------------
    # TÍTULO
    # -----------------------------------

    fuente_titulo = pygame.font.SysFont(
        "Arial",
        24
    )


    titulo = fuente_titulo.render(
        "GRAMATICA LIBRE DE CONTEXTO - BNF",
        True,
        AMARILLO
    )


    ventana.blit(
        titulo,
        (260, 65)
    )


    # ===================================
    # REGLAS BNF
    # ===================================

    fuente_subtitulo = pygame.font.SysFont(
        "Arial",
        17
    )


    subtitulo = fuente_subtitulo.render(
        "Reglas de produccion:",
        True,
        VERDE
    )


    ventana.blit(
        subtitulo,
        (80, 105)
    )


    fuente = pygame.font.SysFont(
        "Consolas",
        14
    )


    reglas = (
        gramatica.obtener_bnf()
    )


    posicion_y = 135


    for regla in reglas:

        texto = fuente.render(
            regla,
            True,
            BLANCO
        )


        ventana.blit(
            texto,
            (90, posicion_y)
        )


        posicion_y = (
            posicion_y + 20
        )


    # ===================================
    # DERIVACIÓN
    # ===================================

    posicion_y = (
        posicion_y + 10
    )


    subtitulo = fuente_subtitulo.render(
        "Derivacion por la izquierda:",
        True,
        VERDE
    )


    ventana.blit(
        subtitulo,
        (80, posicion_y)
    )


    posicion_y = (
        posicion_y + 28
    )


    derivacion = (
        gramatica.obtener_derivacion(
            "<DIALOGO_INICIO>"
        )
    )


    numero_paso = 1


    for paso in derivacion:

        texto = fuente.render(
            str(numero_paso)
            + ". "
            + paso,
            True,
            BLANCO
        )


        ventana.blit(
            texto,
            (90, posicion_y)
        )


        posicion_y = (
            posicion_y + 18
        )


        numero_paso = (
            numero_paso + 1
        )


    # -----------------------------------
    # CERRAR
    # -----------------------------------

    fuente_cerrar = pygame.font.SysFont(
        "Arial",
        15
    )


    texto_cerrar = fuente_cerrar.render(
        "Presiona G nuevamente para cerrar",
        True,
        AMARILLO
    )


    ventana.blit(
        texto_cerrar,
        (690, 575)
    )