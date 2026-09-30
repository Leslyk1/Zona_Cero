from arte import fuente as fuente_arte
from batalla import dibujar_batalla, BOTONES_COMBATE
import pygame


# ===================================
# TEMA VISUAL
# ===================================

# Diego: azul oscuro, verde menta y ámbar unifican mapas, diario y combate.
FONDO_PANEL = (17, 30, 39)
FONDO_INTERNO = (12, 23, 32)
VERDE_NEON = (98, 225, 176)
VERDE_SUAVE = (53, 121, 110)
AMARILLO_NEON = (232, 190, 111)
ROJO_VIDA = (224, 113, 101)
ROJO_COMBATE = (255, 65, 65)
BLANCO = (235, 240, 238)
GRIS_TEXTO = (149, 174, 183)
GRIS_BORDE = (70, 88, 88)


def _fuente(tamano, negrita=False):
    # Diego: tipografía más legible y almacenada en caché para toda la interfaz.
    return fuente_arte(tamano + 2, negrita)


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

def mostrar_interaccion(ventana, mensaje):
    # Diego: esta función dibuja en la franja inferior, fuera del mapa.
    fondo = pygame.Rect(620, 10, 370, 60)
    _panel(ventana, fondo, VERDE_NEON, 2, 9)
    tiene_tecla = mensaje.startswith("E -")
    if tiene_tecla:
        _tecla(ventana, "E", 632, 20, VERDE_NEON)
        mensaje = mensaje[3:].strip()
    else:
        _icono_informacion(ventana, (654, 40), AMARILLO_NEON)
    _texto_en_lineas(ventana, mensaje, 690, 23, 280, 2, _fuente(13, True))


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
        ventana.get_width() - 20,
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
        (180, 21)
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

        fuente_historial = _fuente(11, True)

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
            ventana.get_width() - 675
        )


        texto_transicion = fuente_historial.render(
            transicion,
            True,
            VERDE_NEON
        )


        ventana.blit(
            texto_transicion,
            (660, 17)
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
                (660, 38)
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
            (ventana.get_width() - 145, 38)
        )


# ===================================
# MOSTRAR VIDA
# ===================================

def mostrar_vida(ventana, jugador):
    # Diego: coordenadas de la columna lateral; la vida ya no tapa al jugador.
    fondo = pygame.Rect(10, 145, 230, 80)
    _panel(ventana, fondo, VERDE_SUAVE, 2, 8)
    _icono_corazon(ventana, 23, 159)
    fuente = _fuente(14, True)
    texto = fuente.render(f"VIDA: {jugador.vida}/{jugador.vida_maxima}", True, BLANCO)
    ventana.blit(texto, (55, 160))
    porcentaje = max(0, min(1, jugador.vida / jugador.vida_maxima))
    barra = pygame.Rect(23, 192, 204, 18)
    pygame.draw.rect(ventana, (30, 35, 35), barra, border_radius=3)
    relleno = pygame.Rect(barra.x + 3, barra.y + 3,
                         int((barra.width - 6) * porcentaje), barra.height - 6)
    pygame.draw.rect(ventana, ROJO_VIDA, relleno, border_radius=2)
    pygame.draw.rect(ventana, BLANCO, barra, 2, border_radius=3)


# ===================================
# MOSTRAR DIÁLOGO
# ===================================

def mostrar_dialogo(ventana, mensaje):
    # Diego: los diálogos comparten la franja inferior con la interacción,
    # pero ocupan su propio espacio y pueden mostrar dos líneas.
    _panel(ventana, pygame.Rect(10, 10, 600, 60), VERDE_NEON, 2, 8)
    _icono_informacion(ventana, (35, 40), VERDE_NEON)
    _texto_en_lineas(ventana, mensaje, 65, 22, 530, 2, _fuente(13))


# ===================================
# MOSTRAR MISIÓN
# ===================================

def mostrar_mision(ventana, mision):
    if not mision.activa and not mision.completada:
        return
    # Conservamos los cuatro segundos del aviso incorporado por Darvin.
    if mision.completada:
        tiempo_completada = getattr(mision, "tiempo_completada", 0)
        if tiempo_completada == 0:
            tiempo_completada = pygame.time.get_ticks()
            mision.tiempo_completada = tiempo_completada
        if pygame.time.get_ticks() - tiempo_completada >= 4000:
            return
    # Diego: la misión ocupa la parte inferior de la columna lateral.
    color = AMARILLO_NEON if mision.activa else VERDE_NEON
    titulo = "MISION ACTUAL" if mision.activa else "MISION COMPLETADA"
    _panel(ventana, pygame.Rect(10, 425, 230, 140), color, 2, 8)
    ventana.blit(_fuente(14, True).render(titulo, True, color), (23, 440))
    pygame.draw.line(ventana, color, (23, 466), (227, 466), 1)
    _texto_en_lineas(ventana, mision.descripcion, 23, 477, 204, 4, _fuente(12))


# ===================================
# MOSTRAR INVENTARIO
# ===================================

def mostrar_inventario(ventana, inventario):
    # Diego: el inventario se dibuja exclusivamente en la columna lateral.
    _panel(ventana, pygame.Rect(10, 10, 230, 125), VERDE_SUAVE, 2, 8)
    _icono_mochila(ventana, 23, 20)
    ventana.blit(_fuente(14, True).render("INVENTARIO", True, BLANCO), (55, 26))
    pygame.draw.line(ventana, VERDE_NEON, (23, 55), (227, 55), 2)
    contenido = pygame.Rect(23, 63, 204, 64)
    _caja_interna(ventana, contenido)
    fuente = _fuente(12)
    if not inventario.objetos:
        texto = fuente.render("Vacio", True, GRIS_TEXTO)
        ventana.blit(texto, texto.get_rect(center=contenido.center))
    else:
        for fila, (nombre, cantidad) in enumerate(inventario.objetos.items()):
            texto = fuente.render(f"- {nombre} x{cantidad}", True, BLANCO)
            ventana.blit(texto, (30, 68 + fila * 18))


# ===================================
# MOSTRAR PILA
# ===================================

def mostrar_pila_mundo(ventana, pila_mundo):
    # Diego: mismo contenido LIFO, reubicado sin cubrir habitaciones ni puertas.
    _panel(ventana, pygame.Rect(10, 235, 230, 180), AMARILLO_NEON, 2, 10)
    _icono_pila(ventana, 23, 246)
    ventana.blit(_fuente(14, True).render("PILA DEL MUNDO", True, AMARILLO_NEON), (55, 250))
    pygame.draw.line(ventana, AMARILLO_NEON, (23, 278), (227, 278), 2)
    fuente = _fuente(11)
    operacion = _texto_limitado(fuente, "Operacion: " + pila_mundo.ultima_operacion, 204)
    ventana.blit(fuente.render(operacion, True, BLANCO), (23, 287))
    contenido = pygame.Rect(23, 312, 204, 90)
    _caja_interna(ventana, contenido)
    if not pila_mundo.elementos:
        texto = _fuente(12).render("Pila vacia", True, GRIS_TEXTO)
        ventana.blit(texto, texto.get_rect(center=contenido.center))
    else:
        ventana.blit(_fuente(12, True).render("TOPE", True, VERDE_NEON), (33, 317))
        for fila, lugar in enumerate(reversed(pila_mundo.elementos[-2:])):
            caja = pygame.Rect(33, 338 + fila * 28, 184, 25)
            pygame.draw.rect(ventana, (56, 65, 65), caja)
            pygame.draw.rect(ventana, BLANCO, caja, 1)
            texto = _fuente(11, True).render(lugar, True, BLANCO)
            ventana.blit(texto, texto.get_rect(center=caja.center))


# ===================================
# MOSTRAR COMBATE
# ===================================

def mostrar_combate(ventana, combate, jugador, inventario):
    # Diego: la vista de batalla está separada del autómata que calcula los turnos.
    dibujar_batalla(ventana, combate, jugador, inventario)


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


def _texto_en_lineas(ventana, mensaje, x, y, ancho, max_lineas, fuente):
    # Diego: ajustar el texto al ancho evita que los mensajes invadan otro panel.
    pendientes = mensaje.split()
    for fila in range(max_lineas):
        if not pendientes:
            break
        if fila == max_lineas - 1:
            linea = _texto_limitado(fuente, " ".join(pendientes), ancho)
            pendientes.clear()
        else:
            linea = pendientes.pop(0)
            while pendientes and fuente.size(linea + " " + pendientes[0])[0] <= ancho:
                linea += " " + pendientes.pop(0)
            linea = _texto_limitado(fuente, linea, ancho)
        ventana.blit(fuente.render(linea, True, BLANCO), (x, y + fila * fuente.get_linesize()))


def mostrar_controles(ventana):
    # Diego: el nuevo diario es accesible con J; ESC cierra los paneles de consulta.
    fuente = _fuente(12)
    for fila, texto in enumerate(("W A S D  Moverse", "E  Interactuar", "J  Misiones y progreso", "G  Gramática / BNF", "X  Explorar en la calle")):
        ventana.blit(fuente.render(texto, True, GRIS_TEXTO), (23, 563 + fila * 16))


def _marca_objetivo(ventana, centro, hecho):
    color = VERDE_NEON if hecho else GRIS_BORDE
    pygame.draw.circle(ventana, color, centro, 7, 2)
    if hecho:
        x, y = centro
        pygame.draw.lines(ventana, VERDE_NEON, False, [(x-3, y), (x-1, y+3), (x+4, y-3)], 2)


def mostrar_resumen_misiones(ventana, diario, mision):
    # Diego: resumen permanente; la misión no desaparece del diario cuando se
    # termina. Solo el aviso de celebración conserva su duración de cuatro segundos.
    _panel(ventana, pygame.Rect(10, 425, 230, 128), AMARILLO_NEON, 2, 8)
    aviso = mision.completada and pygame.time.get_ticks() - mision.tiempo_completada < 4000
    titulo = "¡MISIÓN COMPLETADA!" if aviso else "OBJETIVOS  " + str(diario.completadas) + "/3"
    ventana.blit(_fuente(13, True).render(titulo, True, VERDE_NEON if aviso else AMARILLO_NEON), (23, 437))
    abreviados = ("Ayudar a Elena", "Despejar comisaría", "Despejar el sótano")
    for i, (nombre, m) in enumerate(zip(abreviados, diario.misiones)):
        y = 470 + i*21
        _marca_objetivo(ventana, (30, y), m["completa"])
        color = VERDE_NEON if m["completa"] else BLANCO
        ventana.blit(_fuente(12).render(nombre, True, color), (44, y-9))
    barra = pygame.Rect(23, 538, 204, 4)
    pygame.draw.rect(ventana, GRIS_BORDE, barra, border_radius=2)
    if diario.porcentaje:
        pygame.draw.rect(ventana, VERDE_NEON, (barra.x, barra.y, round(barra.width*diario.porcentaje/100), 4), border_radius=2)


def mostrar_diario(ventana, diario):
    # Diego: el progreso se calcula a partir del mundo; abrir este panel nunca
    # cambia el inventario, concede una misión ni consume un turno de combate.
    ventana.fill((12, 22, 31))
    _panel(ventana, pygame.Rect(25, 25, 950, 598), VERDE_SUAVE, 2, 12)
    ventana.blit(_fuente(12, True).render("ZONA CERO / REGISTRO DEL SUPERVIVIENTE", True, AMARILLO_NEON), (48, 44))
    ventana.blit(_fuente(30, True).render("Diario de misiones", True, BLANCO), (48, 67))
    ventana.blit(_fuente(14).render("Tu camino hacia el último refugio.", True, GRIS_TEXTO), (49, 111))
    ventana.blit(_fuente(26, True).render(f"{diario.porcentaje}%", True, VERDE_NEON), (864, 68))
    ventana.blit(_fuente(12).render(f"{diario.pasos_completados}/{diario.total_pasos} pasos", True, GRIS_TEXTO), (864, 109))
    pygame.draw.rect(ventana, GRIS_BORDE, (48, 139, 900, 5), border_radius=2)
    if diario.porcentaje:
        pygame.draw.rect(ventana, VERDE_NEON, (48, 139, round(900*diario.porcentaje/100), 5), border_radius=2)

    for indice, m in enumerate(diario.misiones):
        y = (163, 335, 445)[indice]
        alto = 158 if indice == 0 else 98
        rect = pygame.Rect(48, y, 900, alto)
        color = VERDE_NEON if m["completa"] else GRIS_BORDE
        _caja_interna(ventana, rect, color)
        _marca_objetivo(ventana, (72, y+25), m["completa"])
        ventana.blit(_fuente(19, True).render(m["nombre"], True, BLANCO), (91, y+10))
        estado = "COMPLETADA" if m["completa"] else "EN CURSO" if any(h for _, h in m["pasos"]) else "PENDIENTE"
        texto_estado = _fuente(11, True).render(estado + "  /  " + m["zona"], True, color if m["completa"] else AMARILLO_NEON)
        ventana.blit(texto_estado, (rect.right-18-texto_estado.get_width(), y+17))
        ventana.blit(_fuente(12).render(m["descripcion"], True, GRIS_TEXTO), (72, y+43))
        for paso, (nombre, hecho) in enumerate(m["pasos"]):
            py = y+77+paso*26
            _marca_objetivo(ventana, (79, py), hecho)
            ventana.blit(_fuente(13).render(nombre, True, VERDE_NEON if hecho else BLANCO), (98, py-11))

    ventana.blit(_fuente(11, True).render("SIGUIENTE PASO", True, AMARILLO_NEON), (48, 559))
    ventana.blit(_fuente(14).render(diario.siguiente, True, BLANCO), (48, 579))
    cerrar = _fuente(12, True).render("J / ESC  ·  Volver al juego", True, GRIS_TEXTO)
    ventana.blit(cerrar, (948-cerrar.get_width(), 592))
