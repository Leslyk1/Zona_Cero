"""Presentación de batalla RPG: personajes enfrentados y menú por turnos."""
import math
import pygame
from arte import sprite, fondo_batalla
from arte_inicio import fuente, panel, MENTA, ORO, MARFIL

# Diego: estos rectángulos se comparten con main para que el clic coincida
# exactamente con el menú incluso cuando la ventana está escalada.
BOTONES_COMBATE = tuple(pygame.Rect(592 + i * 127, 478, 117, 108) for i in range(3))
ROJO = (238, 125, 111)
APAGADO = (172, 190, 192)


def tarjeta(ventana, rect, borde=MENTA):
    panel(ventana, rect, (16, 29, 35), borde)


def texto(ventana, mensaje, posicion, tamano=16, color=MARFIL, negrita=False):
    ventana.blit(fuente(tamano, negrita).render(mensaje, True, color), posicion)


def lineas(ventana, mensaje, rect, tamano=19, color=MARFIL):
    f = fuente(tamano)
    palabras = mensaje.split()
    y = rect.y
    while palabras and y + f.get_linesize() <= rect.bottom:
        linea = palabras.pop(0)
        while palabras and f.size(linea + " " + palabras[0])[0] <= rect.width:
            linea += " " + palabras.pop(0)
        texto(ventana, linea, (rect.x, y), tamano, color)
        y += f.get_linesize()


def estado_vida(ventana, rect, nombre, subtitulo, vida, maxima, visible, color):
    tarjeta(ventana, rect, color)
    texto(ventana, nombre, (rect.x+18, rect.y+12), 22, MARFIL, True)
    texto(ventana, subtitulo, (rect.x+18, rect.y+41), 12, APAGADO, True)
    barra = pygame.Rect(rect.x+49, rect.y+66, rect.width-68, 11)
    texto(ventana, "PS", (rect.x+18, rect.y+60), 13, ORO, True)
    pygame.draw.rect(ventana, (10, 21, 29), barra)
    porcentaje = max(0, min(1, visible/maxima))
    tono = MENTA if porcentaje > .5 else ORO if porcentaje > .2 else ROJO
    relleno = barra.copy()
    relleno.width = round(barra.width * porcentaje)
    if relleno.width:
        pygame.draw.rect(ventana, tono, relleno)
    for x in range(barra.x + 24, barra.right, 24):
        pygame.draw.line(ventana, (10, 21, 29), (x, barra.top), (x, barra.bottom), 2)
    texto(ventana, f"{vida} / {maxima}", (rect.right-85, rect.y+81), 12, MARFIL)


def _destello(imagen, tiempo, recibe_dano):
    # Se aclara una copia; nunca se altera el sprite compartido ni el mapa.
    if recibe_dano and 45 <= tiempo < 180:
        imagen = imagen.copy()
        imagen.fill((65, 54, 40), special_flags=pygame.BLEND_RGB_ADD)
    return imagen


def _efectos(ventana, combate, anim, px, py, ex, ey):
    objetivo = combate.objetivo_animacion
    bloqueo = combate.estado == "TURNO_ENEMIGO" and combate.transicion.endswith("BLOQUEO")
    if objetivo == "escudo" or (bloqueo and anim < 600):
        # Escudo escalonado en el lado del ataque, sin tapar al superviviente.
        puntos = [(px+65, py-175), (px+97, py-175), (px+97, py-147),
                  (px+105, py-147), (px+105, py-105), (px+97, py-105),
                  (px+97, py-81), (px+81, py-65), (px+65, py-81)]
        pygame.draw.polygon(ventana, MENTA, puntos, 3)
        if objetivo == "escudo":
            texto(ventana, "GUARDIA", (px-36, py-212), 17, MENTA, True)
    if combate.estado == "DISPARANDO" and anim < 125:
        boca = (px+55, py-120)
        pygame.draw.rect(ventana, ORO, (boca[0], boca[1]-6, 18, 12))
        pygame.draw.rect(ventana, MARFIL, (boca[0]+6, boca[1]-3, 8, 6))
        pygame.draw.line(ventana, ORO, (boca[0]+25, boca[1]), (ex-40, ey-90), 2)
    if objetivo not in ("jugador", "enemigo") or anim >= 750:
        return
    tx, ty = (ex, ey-100) if objetivo == "enemigo" else (px, py-130)
    dano = combate.dano_animacion
    critico = objetivo == "enemigo" and combate.resultado_actual == "CRITICO"
    color = MENTA if bloqueo or not dano else ORO if critico else ROJO
    if dano and anim < 360:
        progreso = anim / 360
        for i in range(8):
            angulo = i * math.tau / 8 + .3
            radio = 12 + progreso * (29 + i % 3 * 9)
            x = tx + round(math.cos(angulo) * radio)
            y = ty + round(math.sin(angulo) * radio + progreso * progreso * 12)
            lado = 4 if i % 2 else 6
            pygame.draw.rect(ventana, color if i % 2 else ORO, (x, y, lado, lado))
    elif not dano and anim < 400:
        for i in range(3):
            x = tx - 48 - i*7
            pygame.draw.line(ventana, GRIS_ESQUIVE, (x, ty+i*10), (x+20, ty+i*10), 2)
    rotulo = ("BLOQUEO " if bloqueo else "CRÍTICO " if critico else "") + f"-{dano}" if dano else "ESQUIVE"
    dibujo = fuente(23, True).render(rotulo, True, color)
    ventana.blit(dibujo, dibujo.get_rect(center=(tx, ty-82-int(anim/32))))


GRIS_ESQUIVE = (146, 166, 163)


def dibujar_batalla(ventana, combate, jugador, inventario):
    # Diego: la escena ocupa el mapa, mientras la columna lateral sigue mostrando
    # el inventario y el progreso. El motor de combate decide todo el daño.
    corredor = "Corredor" in combate.enemigo.nombre
    ventana.blit(fondo_batalla(corredor), (0, 0))
    pygame.draw.rect(ventana, (14, 25, 35), (0, 0, 1000, 56))
    texto(ventana, "ZONA CERO  /  ENCUENTRO", (30, 17), 15, ORO, True)
    texto(ventana, "SÓTANO DEL HOSPITAL" if corredor else "COMISARÍA", (465, 18), 13, APAGADO)
    texto(ventana, f"TURNO {combate.turno:02d}", (876, 17), 16, MENTA, True)

    ahora = pygame.time.get_ticks()
    anim = ahora - combate.inicio_fase
    onda = math.sin(min(1, anim/480) * math.pi)
    retroceso = int(math.sin(anim/35)*5) if anim < 500 and combate.dano_animacion else 0
    px, py, ex, ey = 267, 429, 748, 303
    if combate.estado in ("ATACANDO", "DISPARANDO"):
        px += round(22*onda)
        ex += retroceso
    if combate.estado == "TURNO_ENEMIGO":
        ex -= round(22*onda)
        px += retroceso
    if not combate.dano_animacion:
        if combate.objetivo_animacion == "jugador":
            px -= round(18*onda)
        elif combate.objetivo_animacion == "enemigo":
            ex += round(18*onda)
    tipo = "corredor" if corredor else "policia"
    enemigo = pygame.transform.scale(sprite(tipo), (132, 176))
    heroe = pygame.transform.scale(sprite("superviviente", True), (174, 232))
    enemigo = _destello(enemigo, anim, combate.objetivo_animacion == "enemigo" and combate.dano_animacion)
    heroe = _destello(heroe, anim, combate.objetivo_animacion == "jugador" and combate.dano_animacion)
    if combate.estado == "VICTORIA":
        enemigo.set_alpha(75)
    ventana.blit(enemigo, (ex-66, ey-176 + round(math.sin(ahora/380)*2)))
    ventana.blit(heroe, (px-87, py-232))

    estado_vida(ventana, pygame.Rect(30, 83, 370, 107), combate.enemigo.nombre,
                "INFECTADO / AMENAZA RÁPIDA" if corredor else "INFECTADO / GUARDIA",
                combate.enemigo.vida, combate.enemigo.vida_maxima,
                combate.vida_visible_enemigo, ROJO)
    estado_vida(ventana, pygame.Rect(609, 336, 361, 107), "Superviviente", "ÚLTIMO REFUGIO",
                jugador.vida, jugador.vida_maxima, combate.vida_visible_jugador, MENTA)

    _efectos(ventana, combate, anim, px, py, ex, ey)

    # Caja de diálogo y tres movimientos, como en los RPG clásicos de criaturas.
    tarjeta(ventana, pygame.Rect(30, 470, 542, 116), (77, 111, 121))
    etiqueta = "¿QUÉ HARÁS?" if combate.estado == "ELEGIR_ACCION" else {
        "TURNO_ENEMIGO": "RESPUESTA ENEMIGA", "VICTORIA": "ZONA DESPEJADA",
        "DERROTA": "VUELVE A INTENTARLO"}.get(combate.estado, "TU ACCIÓN")
    texto(ventana, etiqueta, (48, 482), 12, ORO, True)
    lineas(ventana, combate.mensaje, pygame.Rect(48, 505, 505, 74), 19)

    if combate.estado in ("VICTORIA", "DERROTA"):
        color = MENTA if combate.estado == "VICTORIA" else ROJO
        tarjeta(ventana, pygame.Rect(592, 478, 371, 108), color)
        texto(ventana, "VICTORIA" if combate.estado == "VICTORIA" else "DERROTA", (612, 492), 25, color, True)
        texto(ventana, "ENTER  ·  Continuar" if combate.estado == "VICTORIA" else "ENTER  ·  Volver al refugio", (612, 537), 17)
    else:
        balas = inventario.obtener_cantidad("Balas")
        arma = inventario.tiene("Pistola")
        opciones = [("GOLPEAR", "Sin coste", "10 / 20 daño"),
                    ("DISPARAR", f"{balas} balas" if arma else "Sin pistola", "20 / 30 daño"),
                    ("DEFENDER", "Sin coste", "Reduce daño")]
        for i, (rect, (nombre, recurso, efecto)) in enumerate(zip(BOTONES_COMBATE, opciones)):
            habilitado = combate.estado == "ELEGIR_ACCION" and (i != 1 or (arma and balas))
            seleccionado = i == combate.opcion
            borde = ORO if seleccionado else (66, 93, 102)
            tarjeta(ventana, rect, borde)
            color = MARFIL if habilitado else APAGADO
            texto(ventana, str(i+1), (rect.x+12, rect.y+6), 17, borde, True)
            if seleccionado:
                # Triángulo dibujado: no depende de símbolos de la fuente instalada.
                pygame.draw.polygon(ventana, ORO, [(rect.right-15, rect.y+13),
                                                  (rect.right-24, rect.y+18),
                                                  (rect.right-15, rect.y+23)])
            texto(ventana, nombre, (rect.x+10, rect.y+34), 15, color, True)
            texto(ventana, recurso, (rect.x+10, rect.y+60), 13, APAGADO)
            texto(ventana, efecto, (rect.x+10, rect.y+81), 11, APAGADO)

    pygame.draw.rect(ventana, (12, 22, 31), (0, 601, 1000, 49))
    texto(ventana, "1 / 2 / 3 · Flechas + Enter · Clic en una acción", (30, 607), 13, MARFIL)
    texto(ventana, "AFN: " + combate.transicion, (30, 628), 12, MENTA)
