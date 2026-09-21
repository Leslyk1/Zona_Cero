# Importamos random
# para utilizar probabilidades.
import random


# -----------------------------------
# CLASE COMBATE
# -----------------------------------

class Combate:

    def __init__(self):

        # Indica si actualmente
        # existe un combate.
        self.activo = False

        # Estado actual del
        # autómata de combate.
        self.estado = "SIN_COMBATE"

        # Aquí guardaremos al enemigo.
        self.enemigo = None

        # Mensaje que aparecerá
        # durante el combate.
        self.mensaje = ""

        # Aquí mostraremos la transición
        # que realizó el autómata.
        self.transicion = ""


    # -----------------------------------
    # INICIAR COMBATE
    # -----------------------------------

    def iniciar(self, enemigo):

        # Solamente iniciamos el combate
        # si el enemigo sigue vivo.
        if enemigo.vivo == True:

            self.activo = True

            self.enemigo = enemigo

            self.estado = "ELEGIR_ACCION"

            self.mensaje = (
                "El combate ha comenzado."
            )

            self.transicion = (
                "INICIO -> ELEGIR_ACCION"
            )


    # ===================================
    # ATAQUE CUERPO A CUERPO
    # ===================================

    def golpear(
        self,
        jugador
    ):

        # Solo podemos atacar cuando
        # estamos en ELEGIR_ACCION.
        if self.estado != "ELEGIR_ACCION":

            return


        # Cambiamos de estado.
        self.estado = "ATACANDO"


        # Número aleatorio entre 1 y 100.
        numero = random.randint(
            1,
            100
        )


        # -----------------------------------
        # CRÍTICO
        # -----------------------------------

        # 20% de probabilidad.
        if numero <= 20:

            dano = 20

            resultado = "CRITICO"


            self.enemigo.recibir_dano(
                dano
            )


            self.mensaje = (
                "Golpe critico. "
                "Causaste 20 de dano."
            )


        # -----------------------------------
        # GOLPE NORMAL
        # -----------------------------------

        # 65% de probabilidad.
        elif numero <= 85:

            dano = 10

            resultado = "GOLPE_NORMAL"


            self.enemigo.recibir_dano(
                dano
            )


            self.mensaje = (
                "Golpe normal. "
                "Causaste 10 de dano."
            )


        # -----------------------------------
        # FALLO
        # -----------------------------------

        # 15% de probabilidad.
        else:

            dano = 0

            resultado = "FALLO"


            self.mensaje = (
                "Tu golpe ha fallado."
            )


        # Revisamos si derrotamos
        # al enemigo.
        if self.enemigo.vivo == False:

            self.estado = "VICTORIA"

            self.transicion = (
                "ELEGIR_ACCION -> "
                "GOLPEAR -> "
                + resultado
                + " -> VICTORIA"
            )


            self.mensaje = (
                "Has derrotado al zombi."
            )


            return


        # Si sigue vivo,
        # juega el enemigo.
        self.turno_enemigo(
            jugador,
            "GOLPEAR",
            resultado
        )


    # ===================================
    # DISPARAR
    # ===================================

    def disparar(
        self,
        jugador,
        inventario
    ):

        # Solamente podemos disparar
        # en este estado.
        if self.estado != "ELEGIR_ACCION":

            return


        # -----------------------------------
        # REVISAR PISTOLA
        # -----------------------------------

        if inventario.tiene(
            "Pistola"
        ) == False:

            self.mensaje = (
                "No tienes una pistola."
            )

            return


        # -----------------------------------
        # REVISAR MUNICIÓN
        # -----------------------------------

        if inventario.tiene(
            "Balas"
        ) == False:

            self.mensaje = (
                "No tienes balas."
            )

            return


        # -----------------------------------
        # GASTAR UNA BALA
        # -----------------------------------

        inventario.usar(
            "Balas",
            1
        )


        # Cambiamos de estado.
        self.estado = "DISPARANDO"


        # Número aleatorio.
        numero = random.randint(
            1,
            100
        )


        # -----------------------------------
        # DISPARO CRÍTICO
        # -----------------------------------

        # 30% de probabilidad.
        if numero <= 30:

            dano = 30

            resultado = "CRITICO"


            self.enemigo.recibir_dano(
                dano
            )


            self.mensaje = (
                "Disparo critico. "
                "Causaste 30 de dano."
            )


        # -----------------------------------
        # DISPARO NORMAL
        # -----------------------------------

        # 60% de probabilidad.
        elif numero <= 90:

            dano = 20

            resultado = "IMPACTO"


            self.enemigo.recibir_dano(
                dano
            )


            self.mensaje = (
                "El disparo impacto. "
                "Causaste 20 de dano."
            )


        # -----------------------------------
        # DISPARO FALLIDO
        # -----------------------------------

        # 10% de probabilidad.
        else:

            dano = 0

            resultado = "FALLO"


            self.mensaje = (
                "El disparo ha fallado."
            )


        # -----------------------------------
        # REVISAR VICTORIA
        # -----------------------------------

        if self.enemigo.vivo == False:

            self.estado = "VICTORIA"


            self.transicion = (
                "ELEGIR_ACCION -> "
                "DISPARAR -> "
                + resultado
                + " -> VICTORIA"
            )


            self.mensaje = (
                "Has derrotado al zombi."
            )


            return


        # Turno del enemigo.
        self.turno_enemigo(
            jugador,
            "DISPARAR",
            resultado
        )


    # ===================================
    # DEFENDER
    # ===================================

    def defender(
        self,
        jugador
    ):

        if self.estado != "ELEGIR_ACCION":

            return


        # Cambiamos de estado.
        self.estado = "DEFENDIENDO"


        # Número aleatorio.
        numero = random.randint(
            1,
            100
        )


        # -----------------------------------
        # ESQUIVE
        # -----------------------------------

        # 30% de probabilidad.
        if numero <= 30:

            self.mensaje = (
                "Esquivaste completamente "
                "el ataque."
            )


            self.transicion = (
                "ELEGIR_ACCION -> "
                "DEFENDER -> "
                "ESQUIVE -> "
                "ELEGIR_ACCION"
            )


        # -----------------------------------
        # BLOQUEO
        # -----------------------------------

        else:

            # Al defendernos solamente
            # recibimos la mitad del daño.
            dano_reducido = int(
                self.enemigo.danio / 2
            )


            jugador.recibir_dano(
                dano_reducido
            )


            self.mensaje = (
                "Bloqueaste parte del ataque. "
                "Recibiste "
                + str(dano_reducido)
                + " de dano."
            )


            self.transicion = (
                "ELEGIR_ACCION -> "
                "DEFENDER -> "
                "BLOQUEO -> "
                "ELEGIR_ACCION"
            )


        # -----------------------------------
        # REVISAR DERROTA
        # -----------------------------------

        if jugador.esta_vivo() == False:

            self.estado = "DERROTA"


            self.transicion = (
                "DEFENDER -> DERROTA"
            )


            self.mensaje = (
                "Has sido derrotado."
            )


        else:

            self.estado = "ELEGIR_ACCION"


    # ===================================
    # TURNO DEL ENEMIGO
    # ===================================

    def turno_enemigo(
        self,
        jugador,
        accion_jugador,
        resultado_jugador
    ):

        # Cambiamos de estado.
        self.estado = "TURNO_ENEMIGO"


        # Generamos probabilidad.
        numero = random.randint(
            1,
            100
        )


        # -----------------------------------
        # JUGADOR ESQUIVA
        # -----------------------------------

        # 30% de probabilidad.
        if numero <= 30:

            self.mensaje = (
                self.mensaje
                + " El zombi ataco, "
                + "pero lograste esquivar."
            )


            self.transicion = (
                "ELEGIR_ACCION -> "
                + accion_jugador
                + " -> "
                + resultado_jugador
                + " -> TURNO_ENEMIGO"
                + " -> ESQUIVE"
                + " -> ELEGIR_ACCION"
            )


        # -----------------------------------
        # ZOMBI GOLPEA
        # -----------------------------------

        else:

            jugador.recibir_dano(
                self.enemigo.danio
            )


            self.mensaje = (
                self.mensaje
                + " El zombi te golpeo. "
                + "Recibiste "
                + str(self.enemigo.danio)
                + " de dano."
            )


            self.transicion = (
                "ELEGIR_ACCION -> "
                + accion_jugador
                + " -> "
                + resultado_jugador
                + " -> TURNO_ENEMIGO"
                + " -> GOLPE_ENEMIGO"
            )


        # -----------------------------------
        # DERROTA
        # -----------------------------------

        if jugador.esta_vivo() == False:

            self.estado = "DERROTA"


            self.transicion = (
                self.transicion
                + " -> DERROTA"
            )


            self.mensaje = (
                "Has sido derrotado."
            )


        else:

            self.estado = "ELEGIR_ACCION"


    # ===================================
    # TERMINAR COMBATE
    # ===================================

    def terminar(self):

        self.activo = False

        self.estado = "SIN_COMBATE"

        self.enemigo = None

        self.mensaje = ""

        self.transicion = ""