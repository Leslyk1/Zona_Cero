"""Menú e introducción previos a la partida, sin actualizar el mundo."""

import pygame

from audio_menu import AudioMenu
from arte_inicio import BOTONES, VOLVER, BOTONES_CONFIRMAR, dibujar_inicio
from configuracion import ANCHO_INTERFAZ, ALTO_INTERFAZ, FPS


FONDO = (7, 16, 23)


def mostrar_inicio(pantalla, pausa=False, partida_activa=False, confirmar=False):
    """Devuelve True para jugar, False para cerrar o 'menu' desde la pausa."""
    lienzo = pygame.Surface((ANCHO_INTERFAZ, ALTO_INTERFAZ))
    reloj = pygame.time.Clock()
    vista = "confirmar" if confirmar else "menu"
    origen_confirmacion = "menu"
    destino = "salir"
    audio = AudioMenu()
    fundido = None

    def terminar(resultado):
        return resultado

    seleccion = 0
    while True:
        # La misma transformación se utiliza para dibujar y detectar el mouse.
        ancho, alto = pantalla.get_size()
        escala = min(ancho / ANCHO_INTERFAZ, alto / ALTO_INTERFAZ)
        tamano = (max(1, round(ANCHO_INTERFAZ * escala)), max(1, round(ALTO_INTERFAZ * escala)))
        posicion = ((ancho - tamano[0]) // 2, (alto - tamano[1]) // 2)
        for evento in pygame.event.get():
            seleccion_anterior = seleccion
            if evento.type == pygame.QUIT:
                fundido = None
                vista, seleccion, destino = "confirmar", 0, "salir"
            if evento.type in (pygame.VIDEORESIZE, pygame.WINDOWSIZECHANGED):
                ancho, alto = pantalla.get_size()
                escala = min(ancho / ANCHO_INTERFAZ, alto / ALTO_INTERFAZ)
                tamano = (max(1, round(ANCHO_INTERFAZ * escala)), max(1, round(ALTO_INTERFAZ * escala)))
                posicion = ((ancho - tamano[0]) // 2, (alto - tamano[1]) // 2)
            activar = False
            if evento.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):
                punto = ((evento.pos[0] - posicion[0]) / escala,
                         (evento.pos[1] - posicion[1]) / escala)
                rectangulos = BOTONES if vista == "menu" else BOTONES_CONFIRMAR if vista == "confirmar" else (VOLVER,)
                for indice, rect in enumerate(rectangulos):
                    if rect.collidepoint(punto):
                        seleccion = indice
                        activar = evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1
                        break
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    audio.sonar(confirmar=True)
                    fundido = None
                    if vista == "menu" and pausa:
                        return terminar(True)
                    vista, seleccion = "menu", 0
                elif vista in ("menu", "confirmar") and evento.key in (pygame.K_UP, pygame.K_w):
                    seleccion = (seleccion - 1) % (2 if vista == "confirmar" else 3)
                elif vista in ("menu", "confirmar") and evento.key in (pygame.K_DOWN, pygame.K_s):
                    seleccion = (seleccion + 1) % (2 if vista == "confirmar" else 3)
                elif evento.key in (pygame.K_RETURN, pygame.K_SPACE):
                    activar = True
            if seleccion != seleccion_anterior and not activar:
                audio.sonar()
            if activar and fundido is None:
                audio.sonar(confirmar=True)
                if vista == "confirmar":
                    if seleccion == 0:
                        vista, seleccion = origen_confirmacion, 0
                    else:
                        return terminar("menu" if destino == "menu" else False)
                elif vista == "introduccion":
                    fundido = pygame.time.get_ticks()
                elif vista == "controles":
                    vista, seleccion = "menu", 0
                elif seleccion == 0:
                    if pausa or partida_activa:
                        return terminar(True)
                    vista, seleccion = "introduccion", 0
                elif seleccion == 1:
                    vista, seleccion = "controles", 0
                else:
                    origen_confirmacion = "menu"
                    destino = "menu" if pausa else "salir"
                    vista, seleccion = "confirmar", 0

        dibujar_inicio(lienzo, vista, seleccion, pausa, partida_activa, destino,
                       pygame.time.get_ticks())

        pantalla.fill(FONDO)
        pantalla.blit(pygame.transform.scale(lienzo, tamano), posicion)
        if fundido is not None:
            transcurrido = pygame.time.get_ticks() - fundido
            velo = pygame.Surface(pantalla.get_size())
            velo.fill((0, 0, 0))
            velo.set_alpha(min(255, round(transcurrido * 255 / 450)))
            pantalla.blit(velo, (0, 0))
            if transcurrido >= 450:
                return terminar(True)
        pygame.display.update()
        reloj.tick(FPS)
