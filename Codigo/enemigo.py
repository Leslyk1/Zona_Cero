from arte import personaje, etiqueta

# Importamos pygame
import pygame

# Para calcular distancia entre jugador y enemigo.
import math


# Importamos colores
from configuracion import (
    ROJO,
    BLANCO
)


# -----------------------------------
# CLASE ENEMIGO
# -----------------------------------

class Enemigo:

    def __init__(
        self,
        nombre,
        x,
        y,
        vida,
        danio,
        velocidad=1.0,
        radio_deteccion=260
    ):

        # Nombre del enemigo.
        self.nombre = nombre

        # Guardamos la posición inicial.
        # Sirve cuando el enemigo se reinicia.
        self.x_inicial = x
        self.y_inicial = y

        # Posición con decimales para que
        # el movimiento sea más suave.
        self.posicion_x = float(x)
        self.posicion_y = float(y)

        # Rectángulo del enemigo.
        self.rectangulo = pygame.Rect(
            x,
            y,
            40,
            40
        )

        # Zona utilizada para iniciar
        # el combate.
        self.zona_interaccion = pygame.Rect(
            x - 45,
            y - 45,
            130,
            130
        )

        # Zona pequena que representa contacto real
        # para iniciar el combate automaticamente.
        self.zona_ataque = pygame.Rect(
            0,
            0,
            64,
            64
        )

        self.zona_ataque.center = (
            self.rectangulo.centerx,
            self.rectangulo.centery
        )

        # Vida máxima.
        self.vida_maxima = vida

        # Vida actual.
        self.vida = vida

        # Daño.
        self.danio = danio

        # El enemigo comienza vivo.
        self.vivo = True

        # Velocidad con la que persigue.
        self.velocidad = velocidad

        # Distancia desde la que detecta
        # al jugador.
        self.radio_deteccion = radio_deteccion

        # Nos permite saber si actualmente
        # está persiguiendo.
        self.detectando = False


    # -----------------------------------
    # ACTUALIZAR ZONA DE INTERACCIÓN
    # -----------------------------------

    def actualizar_zona_interaccion(self):

        self.zona_interaccion.center = (
            self.rectangulo.centerx,
            self.rectangulo.centery
        )

        self.zona_ataque.center = (
            self.rectangulo.centerx,
            self.rectangulo.centery
        )


    # -----------------------------------
    # DETECTAR JUGADOR
    # -----------------------------------

    def detectar_jugador(
        self,
        jugador
    ):

        if self.vivo == False:
            self.detectando = False
            return False

        diferencia_x = (
            jugador.rectangulo.centerx
            -
            self.rectangulo.centerx
        )

        diferencia_y = (
            jugador.rectangulo.centery
            -
            self.rectangulo.centery
        )

        distancia = math.sqrt(
            diferencia_x ** 2
            +
            diferencia_y ** 2
        )

        if distancia <= self.radio_deteccion:
            self.detectando = True
            return True

        self.detectando = False
        return False


    # -----------------------------------
    # REVISAR COLISIÓN CON PAREDES
    # -----------------------------------

    def choca_con_pared(
        self,
        paredes
    ):

        for pared in paredes:

            if self.rectangulo.colliderect(
                pared
            ):

                return True

        return False


    # -----------------------------------
    # PERSEGUIR JUGADOR
    # -----------------------------------

    def perseguir(
        self,
        jugador,
        paredes
    ):

        # Solo perseguimos mientras esté vivo.
        if self.vivo == False:
            return

        # Primero revisamos si el jugador
        # está dentro del radio de detección.
        if self.detectar_jugador(
            jugador
        ) == False:

            return

        diferencia_x = (
            jugador.rectangulo.centerx
            -
            self.rectangulo.centerx
        )

        diferencia_y = (
            jugador.rectangulo.centery
            -
            self.rectangulo.centery
        )

        distancia = math.sqrt(
            diferencia_x ** 2
            +
            diferencia_y ** 2
        )

        # Si ya está muy cerca, no necesita
        # seguir avanzando.
        if distancia <= 38:

            self.actualizar_zona_interaccion()

            return

        # Normalizamos la dirección.
        if distancia != 0:

            movimiento_x = (
                diferencia_x
                /
                distancia
                *
                self.velocidad
            )

            movimiento_y = (
                diferencia_y
                /
                distancia
                *
                self.velocidad
            )

        else:

            movimiento_x = 0
            movimiento_y = 0

        # -----------------------------------
        # MOVER EN X
        # -----------------------------------

        posicion_anterior_x = (
            self.posicion_x
        )

        self.posicion_x += movimiento_x

        self.rectangulo.x = round(
            self.posicion_x
        )

        if self.choca_con_pared(
            paredes
        ):

            self.posicion_x = (
                posicion_anterior_x
            )

            self.rectangulo.x = round(
                self.posicion_x
            )

        # -----------------------------------
        # MOVER EN Y
        # -----------------------------------

        posicion_anterior_y = (
            self.posicion_y
        )

        self.posicion_y += movimiento_y

        self.rectangulo.y = round(
            self.posicion_y
        )

        if self.choca_con_pared(
            paredes
        ):

            self.posicion_y = (
                posicion_anterior_y
            )

            self.rectangulo.y = round(
                self.posicion_y
            )

        # La zona de interacción debe moverse
        # junto con el enemigo.
        self.actualizar_zona_interaccion()


    # -----------------------------------
    # CONTACTO PARA COMBATE AUTOMATICO
    # -----------------------------------

    def puede_iniciar_combate(
        self,
        jugador
    ):

        if self.vivo == False:
            return False

        return self.zona_ataque.colliderect(
            jugador.rectangulo
        )


    # -----------------------------------
    # RECIBIR DAÑO
    # -----------------------------------

    def recibir_dano(
        self,
        cantidad
    ):

        # Restamos vida.
        self.vida = (
            self.vida - cantidad
        )

        # Evitamos valores negativos.
        if self.vida < 0:

            self.vida = 0

        # Si llega a cero...
        if self.vida == 0:

            self.vivo = False
            self.detectando = False


    # -----------------------------------
    # REINICIAR
    # -----------------------------------

    def reiniciar(self):

        # Recuperamos toda la vida.
        self.vida = (
            self.vida_maxima
        )

        # Volvemos a marcararlo
        # como vivo.
        self.vivo = True

        self.detectando = False

        # Regresamos al punto donde
        # comenzó originalmente.
        self.posicion_x = float(
            self.x_inicial
        )

        self.posicion_y = float(
            self.y_inicial
        )

        self.rectangulo.x = (
            self.x_inicial
        )

        self.rectangulo.y = (
            self.y_inicial
        )

        self.actualizar_zona_interaccion()


    # -----------------------------------
    # DIBUJAR
    # -----------------------------------

    def dibujar(
        self,
        ventana
    ):

        if self.vivo:

            # Diego: cada enemigo tiene una
            # apariencia distinta.
            tipo = (
                "policia"
                if "Policia" in self.nombre
                else "corredor"
            )

            personaje(
                ventana,
                self.rectangulo,
                tipo
            )

            etiqueta(
                ventana,
                self.nombre,
                (
                    self.rectangulo.centerx,
                    self.rectangulo.top - 30
                ),
                (
                    235,
                    145,
                    123
                )
            )


# ===================================
# ZOMBI POLICÍA
# ===================================

class ZombiPolicia(Enemigo):

    def __init__(self):

        super().__init__(
            "Zombi Policia",
            700,
            420,
            40,
            10,

            # Más lento que el corredor.
            velocidad=1.15,

            # Con este radio detecta al jugador
            # al entrar a la zona de la comisaría.
            radio_deteccion=285
        )


# ===================================
# ZOMBI CORREDOR
# ===================================

class ZombiCorredor(Enemigo):

    def __init__(self):

        # El corredor será más fuerte
        # y también más rápido.
        #
        # Vida: 70
        # Daño: 15
        super().__init__(
            "Zombi Corredor",
            700,
            400,
            70,
            15,

            velocidad=1.75,

            # Detecta desde un poco más lejos.
            radio_deteccion=360
        )
