"""Presentación de batalla RPG: personajes enfrentados y menú por turnos."""
import math
import pygame
from arte import fuente, sprite, fondo_batalla, MENTA, ORO, MARFIL

# Diego: estos rectángulos se comparten con main para que el clic coincida
# exactamente con el menú incluso cuando la ventana está escalada.
BOTONES_COMBATE = tuple(pygame.Rect(592 + i * 127, 478, 117, 108) for i in range(3))
ROJO = (238, 125, 111)
APAGADO = (133, 158, 163)


def tarjeta(ventana, rect, borde=MENTA):
    pygame.draw.rect(ventana, (11, 20, 29), rect.move(0, 5), border_radius=10)
    pygame.draw.rect(ventana, (20, 35, 44), rect, border_radius=10)
    pygame.draw.rect(ventana, borde, rect, 2, border_radius=10)


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
    pygame.draw.rect(ventana, (10, 21, 29), barra, border_radius=5)
    porcentaje = max(0, min(1, visible/maxima))
    tono = MENTA if porcentaje > .5 else ORO if porcentaje > .2 else ROJO
    relleno = barra.copy()
    relleno.width = round(barra.width * porcentaje)
    if relleno.width:
        pygame.draw.rect(ventana, tono, relleno, border_radius=5)
    texto(ventana, f"{vida} / {maxima}", (rect.right-85, rect.y+81), 12, MARFIL)


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
    tipo = "corredor" if corredor else "policia"
    enemigo = pygame.transform.scale(sprite(tipo), (132, 176))
    heroe = pygame.transform.scale(sprite("superviviente", True), (174, 232))
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

    if combate.objetivo_animacion == "escudo":
        pygame.draw.arc(ventana, MENTA, (px-70, py-192, 150, 168), -.9, 1.0, 5)
        texto(ventana, "GUARDIA", (px-38, py-214), 15, MENTA, True)
    elif combate.objetivo_animacion and anim < 750:
        tx, ty = (ex, ey-160) if combate.objetivo_animacion == "enemigo" else (px, py-190)
        rotulo = f"-{combate.dano_animacion}" if combate.dano_animacion else "ESQUIVE"
        color = ORO if combate.resultado_actual == "CRITICO" and combate.objetivo_animacion == "enemigo" else ROJO
        dibujo = fuente(28, True).render(rotulo, True, color)
        ventana.blit(dibujo, dibujo.get_rect(center=(tx, ty-int(anim/28))))
        if combate.dano_animacion and anim < 350:
            for d in (-10, 10):
                pygame.draw.line(ventana, ORO, (tx-26+d, ty+48), (tx+15+d, ty+15), 4)

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
            texto(ventana, efecto, (rect.x+10, rect.y+81), 12, APAGADO)

    pygame.draw.rect(ventana, (12, 22, 31), (0, 601, 1000, 49))
    texto(ventana, "1 / 2 / 3 · Flechas + Enter · Clic en una acción", (30, 607), 13, MARFIL)
    texto(ventana, "AFN: " + combate.transicion, (30, 628), 12, MENTA)
