"""Autómata del combate por turnos, independiente de los dibujos."""
import random
import pygame


class Combate:
    # Diego: cada acción y respuesta ocupa una fase visible, en lugar de resolver
    # todo en una pulsación. Esto permite seguir el autómata durante la batalla.
    DURACION_ACCION = 850
    DURACION_RESPUESTA = 1000

    def __init__(self):
        self.activo = False
        self.estado = "SIN_COMBATE"
        self.enemigo = None
        self.mensaje = ""
        self.transicion = ""
        self.historial = []
        self.opcion = 0
        self.turno = 1
        self.inicio_fase = 0
        self.accion_actual = ""
        self.resultado_actual = ""
        self.objetivo_animacion = ""
        self.dano_animacion = 0
        self.vida_visible_jugador = 100.0
        self.vida_visible_enemigo = 0.0

    def _registrar(self, texto):
        self.transicion = texto
        self.historial.append(texto)
        self.historial = self.historial[-12:]

    def iniciar(self, enemigo, jugador=None):
        if self.activo or not enemigo.vivo:
            return
        self.enemigo = enemigo
        self.activo = True
        self.estado = "ELEGIR_ACCION"
        self.opcion = 0
        self.turno = 1
        self.historial = []
        self.objetivo_animacion = ""
        self.dano_animacion = 0
        self.vida_visible_enemigo = float(enemigo.vida)
        self.vida_visible_jugador = float(jugador.vida if jugador else 100)
        self.inicio_fase = pygame.time.get_ticks()
        self.mensaje = f"¡{enemigo.nombre} bloquea el paso! Elige tu acción."
        self._registrar("INICIO -> ELEGIR_ACCION")

    def elegir_accion(self, opcion, jugador, inventario):
        if self.estado != "ELEGIR_ACCION":
            return
        self.opcion = opcion
        if opcion == 0:
            self.golpear(jugador)
        elif opcion == 1:
            self.disparar(jugador, inventario)
        elif opcion == 2:
            self.defender(jugador)

    def _iniciar_accion(self, accion, estado, resultado, dano, mensaje):
        self.accion_actual = accion
        self.resultado_actual = resultado
        self.estado = estado
        self.inicio_fase = pygame.time.get_ticks()
        self.objetivo_animacion = "enemigo" if accion != "DEFENDER" else "escudo"
        self.dano_animacion = dano
        self.mensaje = mensaje
        self._registrar(f"ELEGIR_ACCION -> {estado} -> {resultado}")

    def golpear(self, jugador):
        if self.estado != "ELEGIR_ACCION":
            return
        numero = random.randint(1, 100)
        # Conservamos las probabilidades originales: 20% crítico, 65% normal.
        if numero <= 20:
            dano, resultado = 20, "CRITICO"
            mensaje = "¡Golpe crítico! Causaste 20 de daño."
        elif numero <= 85:
            dano, resultado = 10, "GOLPE_NORMAL"
            mensaje = "Tu golpe causa 10 de daño."
        else:
            dano, resultado = 0, "FALLO"
            mensaje = "El enemigo evitó tu golpe."
        self.enemigo.recibir_dano(dano)
        self._iniciar_accion("GOLPEAR", "ATACANDO", resultado, dano, mensaje)

    def disparar(self, jugador, inventario):
        if self.estado != "ELEGIR_ACCION":
            return
        # Diego: intentar disparar sin recursos no consume turno ni munición.
        if not inventario.tiene("Pistola"):
            self.mensaje = "Necesitas una pistola. Puedes golpear o defenderte."
            return
        if not inventario.tiene("Balas"):
            self.mensaje = "No quedan balas. Puedes golpear o defenderte."
            return
        inventario.usar("Balas", 1)
        numero = random.randint(1, 100)
        if numero <= 30:
            dano, resultado = 30, "CRITICO"
            mensaje = "¡Disparo crítico! Causaste 30 de daño."
        elif numero <= 90:
            dano, resultado = 20, "IMPACTO"
            mensaje = "El disparo impacta. Causaste 20 de daño."
        else:
            dano, resultado = 0, "FALLO"
            mensaje = "El disparo falló. Perdiste una bala."
        self.enemigo.recibir_dano(dano)
        self._iniciar_accion("DISPARAR", "DISPARANDO", resultado, dano, mensaje)

    def defender(self, jugador):
        if self.estado == "ELEGIR_ACCION":
            self._iniciar_accion("DEFENDER", "DEFENDIENDO", "GUARDIA", 0,
                                "Te pones en guardia. El próximo golpe hará menos daño.")

    def turno_enemigo(self, jugador, accion_jugador, resultado_jugador):
        self.estado = "TURNO_ENEMIGO"
        self.inicio_fase = pygame.time.get_ticks()
        self.objetivo_animacion = "jugador"
        if random.randint(1, 100) <= 30:
            dano, resultado = 0, "ESQUIVE"
            self.mensaje = "¡Esquivaste el ataque enemigo!"
        else:
            defendiendo = accion_jugador == "DEFENDER"
            dano = self.enemigo.danio // 2 if defendiendo else self.enemigo.danio
            resultado = "BLOQUEO" if defendiendo else "GOLPE_ENEMIGO"
            self.mensaje = (f"Bloqueaste parte del ataque. Recibiste {dano} de daño."
                            if defendiendo else f"{self.enemigo.nombre} ataca: recibes {dano} de daño.")
            jugador.recibir_dano(dano)
        self.dano_animacion = dano
        self._registrar(f"{accion_jugador} / {resultado_jugador} -> TURNO_ENEMIGO -> {resultado}")

    def actualizar(self, jugador):
        if not self.activo:
            return
        # Diego: las barras se acercan a la vida real sin alterar el daño.
        for atributo, objetivo in (("vida_visible_jugador", jugador.vida),
                                   ("vida_visible_enemigo", self.enemigo.vida)):
            actual = getattr(self, atributo)
            setattr(self, atributo, objetivo if abs(objetivo - actual) < .2
                    else actual + (objetivo - actual) * .18)
        transcurrido = pygame.time.get_ticks() - self.inicio_fase
        if self.estado in ("ATACANDO", "DISPARANDO", "DEFENDIENDO"):
            if transcurrido < self.DURACION_ACCION:
                return
            if not self.enemigo.vivo:
                self.estado = "VICTORIA"
                self.objetivo_animacion = ""
                self.mensaje = f"¡Victoria! Derrotaste a {self.enemigo.nombre}. Objetivo completado."
                self._registrar(self.transicion + " -> VICTORIA")
            else:
                self.turno_enemigo(jugador, self.accion_actual, self.resultado_actual)
        elif self.estado == "TURNO_ENEMIGO" and transcurrido >= self.DURACION_RESPUESTA:
            self.objetivo_animacion = ""
            if not jugador.esta_vivo():
                self.estado = "DERROTA"
                self.mensaje = "Has caído. Volverás al refugio con la vida recuperada."
                self._registrar(self.transicion + " -> DERROTA")
            else:
                self.estado = "ELEGIR_ACCION"
                self.turno += 1
                self._registrar(self.transicion + " -> ELEGIR_ACCION")

    def terminar(self):
        self.activo = False
        self.estado = "SIN_COMBATE"
        self.enemigo = None
        self.mensaje = ""
        self.transicion = ""
        self.objetivo_animacion = ""
