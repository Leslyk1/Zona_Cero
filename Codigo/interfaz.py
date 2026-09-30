import pygame


# ===================================
# TEMA VISUAL
# ===================================

FONDO_PANEL = (3, 13, 13)
FONDO_INTERNO = (5, 17, 18)
VERDE_NEON = (45, 255, 85)
VERDE_SUAVE = (26, 145, 70)
AMARILLO_NEON = (255, 214, 0)
ROJO_VIDA = (190, 45, 55)
ROJO_COMBATE = (255, 65, 65)
BLANCO = (235, 240, 238)
GRIS_TEXTO = (155, 165, 165)
GRIS_BORDE = (70, 88, 88)


def _fuente(tamano, negrita=False):

    return pygame.font.SysFont(
        "Consolas",
        tamano + 2,
        bold=negrita
    )


def _panel(
    ventana,
    rectangulo,
    color_borde,
    grosor=2,
    recorte=10
):

    x = rectangulo.x
    y = rectangulo.y
    ancho = rectangulo.width
    alto = rectangulo.height


    puntos = [
        (x + recorte, y),
        (x + ancho - recorte, y),
        (x + ancho, y + recorte),
        (x + ancho, y + alto - recorte),
        (x + ancho - recorte, y + alto),
        (x + recorte, y + alto),
        (x, y + alto - recorte),
        (x, y + recorte)
    ]


    sombra = [
        (punto_x + 3, punto_y + 3)
        for punto_x, punto_y in puntos
    ]


    pygame.draw.polygon(
        ventana,
        (0, 5, 5),
        sombra
    )


    pygame.draw.polygon(
        ventana,
        FONDO_PANEL,
        puntos
    )


    pygame.draw.lines(
        ventana,
        color_borde,
        True,
        puntos,
        grosor
    )


    # Detalles cortos de las esquinas.
    pygame.draw.line(
        ventana,
        color_borde,
        (x + 4, y + 16),
        (x + 4, y + 35),
        3
    )


    pygame.draw.line(
        ventana,
        color_borde,
        (x + ancho - 28, y + alto - 5),
        (x + ancho - 10, y + alto - 5),
        3
    )


def _caja_interna(
    ventana,
    rectangulo,
    color=GRIS_BORDE
):

    pygame.draw.rect(
        ventana,
        FONDO_INTERNO,
        rectangulo,
        border_radius=4
    )


    pygame.draw.rect(
        ventana,
        color,
        rectangulo,
        1,
        border_radius=4
    )


def _texto_limitado(
    fuente,
    mensaje,
    ancho_maximo
):

    if fuente.size(mensaje)[0] <= ancho_maximo:

        return mensaje


    mensaje_corto = mensaje


    while (
        len(mensaje_corto) > 3
        and
        fuente.size(mensaje_corto + "...")[0]
        > ancho_maximo
    ):

        mensaje_corto = mensaje_corto[:-1]


    return mensaje_corto.rstrip() + "..."


def _icono_informacion(
    ventana,
    centro,
    color
):

    pygame.draw.circle(
        ventana,
        color,
        centro,
        17,
        2
    )


    fuente = _fuente(21, True)

    texto = fuente.render(
        "i",
        True,
        color
    )


    ventana.blit(
        texto,
        texto.get_rect(center=centro)
    )


def _icono_mochila(
    ventana,
    x,
    y
):

    pygame.draw.rect(
        ventana,
        VERDE_NEON,
        (x, y + 7, 22, 25),
        2,
        border_radius=4
    )


    pygame.draw.arc(
        ventana,
        VERDE_NEON,
        (x + 5, y, 12, 15),
        3.1,
        6.3,
        2
    )


    pygame.draw.line(
        ventana,
        VERDE_NEON,
        (x + 5, y + 20),
        (x + 17, y + 20),
        2
    )


def _icono_corazon(
    ventana,
    x,
    y
):

    pygame.draw.circle(
        ventana,
        VERDE_NEON,
        (x + 7, y + 7),
        7
    )


    pygame.draw.circle(
        ventana,
        VERDE_NEON,
        (x + 18, y + 7),
        7
    )


    pygame.draw.polygon(
        ventana,
        VERDE_NEON,
        [
            (x + 1, y + 8),
            (x + 24, y + 8),
            (x + 12, y + 23)
        ]
    )


def _icono_pila(
    ventana,
    x,
    y
):

    for desplazamiento in [0, 6, 12]:

        pygame.draw.ellipse(
            ventana,
            AMARILLO_NEON,
            (x, y + desplazamiento, 24, 9),
            2
        )


def _tecla(
    ventana,
    letra,
    x,
    y,
    color
):

    caja = pygame.Rect(
        x,
        y,
        45,
        40
    )


    pygame.draw.rect(
        ventana,
        FONDO_INTERNO,
        caja,
        border_radius=6
    )


    pygame.draw.rect(
        ventana,
        color,
        caja,
        2,
        border_radius=6
    )


    fuente = _fuente(25, True)

    texto = fuente.render(
        letra,
        True,
        BLANCO
    )


    ventana.blit(
        texto,
        texto.get_rect(center=caja.center)
    )


# ===================================
# MOSTRAR INTERACCIÓN
# ===================================

def mostrar_interaccion(
    ventana,
    mensaje
):

    fondo = pygame.Rect(
        300,
        580,
        400,
        58
    )


    _panel(
        ventana,
        fondo,
        VERDE_NEON,
        2,
        9
    )


    tiene_tecla = mensaje.startswith("E -")


    if tiene_tecla:

        _tecla(
            ventana,
            "E",
            325,
            589,
            VERDE_NEON
        )


        mensaje_visible = mensaje[3:].strip()
        x_texto = 390

    else:

        _icono_informacion(
            ventana,
            (340, 609),
            AMARILLO_NEON
        )


        mensaje_visible = mensaje
        x_texto = 375


    fuente = _fuente(17, True)

    mensaje_visible = _texto_limitado(
        fuente,
        mensaje_visible,
        290
    )


    texto = fuente.render(
        mensaje_visible,
        True,
        BLANCO
    )


    ventana.blit(
        texto,
        (x_texto, 600)
    )


# ===================================
# MOSTRAR ESTADO DEL AFN
# ===================================

def mostrar_estado_afn(
    ventana,
    automata
):

    estado = automata.estado_actual

    fondo = pygame.Rect(
        10,
        8,
        980,
        52
    )


    _panel(
        ventana,
        fondo,
        VERDE_SUAVE,
        1,
        7
    )


    pygame.draw.circle(
        ventana,
        VERDE_NEON,
        (35, 34),
        12,
        2
    )


    pygame.draw.circle(
        ventana,
        VERDE_NEON,
        (35, 34),
        4
    )


    fuente_etiqueta = _fuente(15, True)

    etiqueta = fuente_etiqueta.render(
        "ESTADO AFN:",
        True,
        BLANCO
    )


    ventana.blit(
        etiqueta,
        (55, 25)
    )


    fuente_estado = _fuente(20, True)

    texto_estado = fuente_estado.render(
        estado,
        True,
        VERDE_NEON
    )


    ventana.blit(
        texto_estado,
        (165, 21)
    )


    boton_gramatica = pygame.Rect(
        405,
        17,
        190,
        34
    )


    _caja_interna(
        ventana,
        boton_gramatica,
        VERDE_SUAVE
    )


    fuente_ayuda = _fuente(14, True)

    ayuda = fuente_ayuda.render(
        "G = Ver GLC / BNF",
        True,
        BLANCO
    )


    ventana.blit(
        ayuda,
        ayuda.get_rect(center=boton_gramatica.center)
    )


    # Mostramos la última transición realizada.
    if automata.estado_anterior is not None:

        fuente_historial = _fuente(9, True)

        transicion = (
            automata.estado_anterior
            + " --"
            + automata.ultima_accion
            + "--> "
            + automata.estado_actual
        )


        transicion = _texto_limitado(
            fuente_historial,
            transicion,
            365
        )


        texto_transicion = fuente_historial.render(
            transicion,
            True,
            VERDE_NEON
        )


        ventana.blit(
            texto_transicion,
            (615, 17)
        )


        # En una transición no determinista
        # mostramos todos los destinos posibles.
        if len(automata.ultimos_posibles) > 1:

            posibles = (
                "POSIBLES: {"
                + ", ".join(
                    automata.ultimos_posibles
                )
                + "}"
            )


            texto_posibles = fuente_historial.render(
                posibles,
                True,
                AMARILLO_NEON
            )


            ventana.blit(
                texto_posibles,
                (615, 38)
            )


    if estado == "CALLE":

        fuente_explorar = _fuente(10, True)

        texto_explorar = fuente_explorar.render(
            "X = EXPLORAR",
            True,
            AMARILLO_NEON
        )


        ventana.blit(
            texto_explorar,
            (850, 38)
        )


# ===================================
# MOSTRAR VIDA
# ===================================

def mostrar_vida(
    ventana,
    jugador
):

    fondo = pygame.Rect(
        15,
        187,
        215,
        72
    )


    _panel(
        ventana,
        fondo,
        VERDE_SUAVE,
        2,
        8
    )


    _icono_corazon(
        ventana,
        28,
        198
    )


    fuente = _fuente(14, True)

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
        (58, 200)
    )


    porcentaje = max(
        0,
        min(
            1,
            jugador.vida / jugador.vida_maxima
        )
    )


    barra = pygame.Rect(
        28,
        229,
        189,
        18
    )


    pygame.draw.rect(
        ventana,
        (30, 35, 35),
        barra,
        border_radius=3
    )


    barra_vida = pygame.Rect(
        barra.x + 3,
        barra.y + 3,
        int((barra.width - 6) * porcentaje),
        barra.height - 6
    )


    pygame.draw.rect(
        ventana,
        ROJO_VIDA,
        barra_vida,
        border_radius=2
    )


    pygame.draw.rect(
        ventana,
        BLANCO,
        barra,
        2,
        border_radius=3
    )


# ===================================
# MOSTRAR DIÁLOGO
# ===================================

def mostrar_dialogo(
    ventana,
    mensaje
):

    fondo = pygame.Rect(
        230,
        510,
        540,
        58
    )


    _panel(
        ventana,
        fondo,
        VERDE_NEON,
        2,
        8
    )


    _icono_informacion(
        ventana,
        (265, 539),
        VERDE_NEON
    )


    fuente = _fuente(15)

    mensaje_visible = _texto_limitado(
        fuente,
        mensaje,
        445
    )


    texto = fuente.render(
        mensaje_visible,
        True,
        BLANCO
    )


    ventana.blit(
        texto,
        (295, 530)
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


    # El mensaje de misión completada solo
    # permanece visible durante 4 segundos.
    if mision.completada == True:

        tiempo_completada = getattr(
            mision,
            "tiempo_completada",
            0
        )


        if tiempo_completada == 0:

            tiempo_completada = (
                pygame.time.get_ticks()
            )

            mision.tiempo_completada = (
                tiempo_completada
            )


        tiempo_transcurrido = (
            pygame.time.get_ticks()
            - tiempo_completada
        )


        if tiempo_transcurrido >= 4000:

            return


    if mision.activa:

        color = AMARILLO_NEON
        titulo_mision = "MISION ACTUAL"

    else:

        color = VERDE_NEON
        titulo_mision = "MISION COMPLETADA"


    fondo = pygame.Rect(
        325,
        72,
        350,
        76
    )


    _panel(
        ventana,
        fondo,
        color,
        2,
        8
    )


    fuente_titulo = _fuente(15, True)

    titulo = fuente_titulo.render(
        titulo_mision,
        True,
        color
    )


    ventana.blit(
        titulo,
        (345, 84)
    )


    pygame.draw.line(
        ventana,
        color,
        (345, 108),
        (655, 108),
        1
    )


    fuente = _fuente(12)

    descripcion = _texto_limitado(
        fuente,
        mision.descripcion,
        305
    )


    texto = fuente.render(
        descripcion,
        True,
        BLANCO
    )


    ventana.blit(
        texto,
        (345, 119)
    )


# ===================================
# MOSTRAR INVENTARIO
# ===================================

def mostrar_inventario(
    ventana,
    inventario
):

    fondo = pygame.Rect(
        15,
        72,
        215,
        115
    )


    _panel(
        ventana,
        fondo,
        VERDE_SUAVE,
        2,
        8
    )


    _icono_mochila(
        ventana,
        28,
        81
    )


    fuente_titulo = _fuente(14, True)

    titulo = fuente_titulo.render(
        "INVENTARIO",
        True,
        BLANCO
    )


    ventana.blit(
        titulo,
        (60, 87)
    )


    pygame.draw.line(
        ventana,
        VERDE_NEON,
        (28, 115),
        (217, 115),
        2
    )


    contenido = pygame.Rect(
        28,
        123,
        189,
        56
    )


    _caja_interna(
        ventana,
        contenido
    )


    fuente = _fuente(12)


    if len(inventario.objetos) == 0:

        texto = fuente.render(
            "Vacio",
            True,
            GRIS_TEXTO
        )


        ventana.blit(
            texto,
            texto.get_rect(center=contenido.center)
        )

    else:

        posicion_y = 126


        for nombre in inventario.objetos:

            cantidad = inventario.objetos[nombre]

            texto = fuente.render(
                "- "
                + nombre
                + " x"
                + str(cantidad),
                True,
                BLANCO
            )


            ventana.blit(
                texto,
                (36, posicion_y)
            )


            posicion_y += 16


# ===================================
# MOSTRAR PILA
# ===================================

def mostrar_pila_mundo(
    ventana,
    pila_mundo
):

    fondo = pygame.Rect(
        760,
        72,
        225,
        185
    )


    _panel(
        ventana,
        fondo,
        AMARILLO_NEON,
        2,
        10
    )


    _icono_pila(
        ventana,
        775,
        83
    )


    fuente_titulo = _fuente(14, True)

    titulo = fuente_titulo.render(
        "PILA DEL MUNDO",
        True,
        AMARILLO_NEON
    )


    ventana.blit(
        titulo,
        (808, 86)
    )


    pygame.draw.line(
        ventana,
        AMARILLO_NEON,
        (775, 114),
        (970, 114),
        2
    )


    fuente_operacion = _fuente(11)

    operacion = _texto_limitado(
        fuente_operacion,
        "Operacion: " + pila_mundo.ultima_operacion,
        190
    )


    texto_operacion = fuente_operacion.render(
        operacion,
        True,
        BLANCO
    )


    ventana.blit(
        texto_operacion,
        (775, 125)
    )


    contenido = pygame.Rect(
        775,
        150,
        195,
        88
    )


    _caja_interna(
        ventana,
        contenido
    )


    if len(pila_mundo.elementos) == 0:

        fuente = _fuente(12)

        texto = fuente.render(
            "Pila vacia",
            True,
            GRIS_TEXTO
        )


        ventana.blit(
            texto,
            texto.get_rect(center=contenido.center)
        )

    else:

        fuente_tope = _fuente(12, True)

        texto_tope = fuente_tope.render(
            "TOPE",
            True,
            VERDE_NEON
        )


        ventana.blit(
            texto_tope,
            (785, 157)
        )


        posicion_y = 178


        for lugar in reversed(
            pila_mundo.elementos[-2:]
        ):

            caja = pygame.Rect(
                790,
                posicion_y,
                165,
                25
            )


            pygame.draw.rect(
                ventana,
                (56, 65, 65),
                caja
            )


            pygame.draw.rect(
                ventana,
                BLANCO,
                caja,
                1
            )


            fuente = _fuente(11, True)

            texto = fuente.render(
                lugar,
                True,
                BLANCO
            )


            ventana.blit(
                texto,
                texto.get_rect(center=caja.center)
            )


            posicion_y += 28


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
        120,
        82,
        760,
        470
    )


    _panel(
        ventana,
        fondo,
        ROJO_COMBATE,
        3,
        14
    )


    fuente_titulo = _fuente(26, True)

    titulo = fuente_titulo.render(
        "PROTOCOLO DE COMBATE",
        True,
        ROJO_COMBATE
    )


    ventana.blit(
        titulo,
        titulo.get_rect(center=(500, 120))
    )


    pygame.draw.line(
        ventana,
        ROJO_COMBATE,
        (155, 148),
        (845, 148),
        2
    )


    enemigo = combate.enemigo
    fuente = _fuente(16, True)

    texto_enemigo = fuente.render(
        enemigo.nombre
        + "  VIDA "
        + str(enemigo.vida)
        + "/"
        + str(enemigo.vida_maxima),
        True,
        ROJO_COMBATE
    )


    ventana.blit(
        texto_enemigo,
        (165, 170)
    )


    texto_jugador = fuente.render(
        "JUGADOR  VIDA "
        + str(jugador.vida)
        + "/"
        + str(jugador.vida_maxima),
        True,
        VERDE_NEON
    )


    ventana.blit(
        texto_jugador,
        (165, 208)
    )


    balas = inventario.obtener_cantidad(
        "Balas"
    )

    texto_balas = fuente.render(
        "BALAS: " + str(balas),
        True,
        AMARILLO_NEON
    )


    ventana.blit(
        texto_balas,
        (680, 208)
    )


    estado = _fuente(14, True).render(
        "ESTADO: " + combate.estado,
        True,
        AMARILLO_NEON
    )


    ventana.blit(
        estado,
        (165, 258)
    )


    caja_mensaje = pygame.Rect(
        155,
        288,
        690,
        72
    )


    _caja_interna(
        ventana,
        caja_mensaje
    )


    fuente_mensaje = _fuente(14)
    mensaje = _texto_limitado(
        fuente_mensaje,
        combate.mensaje,
        650
    )


    ventana.blit(
        fuente_mensaje.render(
            mensaje,
            True,
            BLANCO
        ),
        (175, 305)
    )


    fuente_transicion = _fuente(12)
    transicion = _texto_limitado(
        fuente_transicion,
        "Transicion: " + combate.transicion,
        650
    )


    ventana.blit(
        fuente_transicion.render(
            transicion,
            True,
            VERDE_NEON
        ),
        (175, 334)
    )


    if combate.estado == "ELEGIR_ACCION":

        opciones = [
            ("1", "GOLPEAR", BLANCO),
            (
                "2",
                "DISPARAR",
                BLANCO
                if inventario.tiene("Pistola")
                and inventario.tiene("Balas")
                else ROJO_COMBATE
            ),
            ("3", "DEFENDER", BLANCO)
        ]


        posicion_x = 175


        for tecla, accion, color in opciones:

            _tecla(
                ventana,
                tecla,
                posicion_x,
                405,
                VERDE_NEON
            )


            ventana.blit(
                _fuente(14, True).render(
                    accion,
                    True,
                    color
                ),
                (posicion_x + 55, 418)
            )


            posicion_x += 220

    else:

        if combate.estado == "VICTORIA":

            mensaje_final = "ENTER - CONTINUAR"
            color_final = VERDE_NEON

        else:

            mensaje_final = "ENTER - REINICIAR"
            color_final = ROJO_COMBATE


        texto_final = _fuente(17, True).render(
            mensaje_final,
            True,
            color_final
        )


        ventana.blit(
            texto_final,
            texto_final.get_rect(center=(500, 445))
        )


# ===================================
# MOSTRAR GLC Y BNF
# ===================================

def mostrar_gramatica(
    ventana,
    gramatica
):

    fondo = pygame.Rect(
        40,
        35,
        920,
        575
    )


    _panel(
        ventana,
        fondo,
        AMARILLO_NEON,
        3,
        14
    )


    fuente_titulo = _fuente(22, True)

    titulo = fuente_titulo.render(
        "GRAMATICA LIBRE DE CONTEXTO // BNF",
        True,
        AMARILLO_NEON
    )


    ventana.blit(
        titulo,
        titulo.get_rect(center=(500, 67))
    )


    pygame.draw.line(
        ventana,
        AMARILLO_NEON,
        (75, 92),
        (925, 92),
        2
    )


    fuente_subtitulo = _fuente(15, True)

    ventana.blit(
        fuente_subtitulo.render(
            "REGLAS DE PRODUCCION",
            True,
            VERDE_NEON
        ),
        (75, 108)
    )


    fuente = _fuente(12)
    posicion_y = 137


    for regla in gramatica.obtener_bnf():

        regla_visible = _texto_limitado(
            fuente,
            regla,
            820
        )


        ventana.blit(
            fuente.render(
                regla_visible,
                True,
                BLANCO
            ),
            (85, posicion_y)
        )


        posicion_y += 18


    posicion_y += 10


    ventana.blit(
        fuente_subtitulo.render(
            "DERIVACION POR LA IZQUIERDA",
            True,
            VERDE_NEON
        ),
        (75, posicion_y)
    )


    posicion_y += 28


    derivacion = gramatica.obtener_derivacion(
        "<DIALOGO_INICIO>"
    )


    for numero, paso in enumerate(
        derivacion,
        start=1
    ):

        paso_visible = _texto_limitado(
            fuente,
            str(numero) + ". " + paso,
            820
        )


        ventana.blit(
            fuente.render(
                paso_visible,
                True,
                BLANCO
            ),
            (85, posicion_y)
        )


        posicion_y += 18


    cerrar = _fuente(13, True).render(
        "G = CERRAR",
        True,
        AMARILLO_NEON
    )


    ventana.blit(
        cerrar,
        (815, 575)
    )
