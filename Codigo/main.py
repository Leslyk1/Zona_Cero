# Importamos pygame
import pygame


# ===================================
# CONFIGURACIONES
# ===================================

from configuracion import (
    ANCHO,
    ALTO,
    ANCHO_VENTANA,
    ALTO_VENTANA,
    FPS
)


# ===================================
# JUGADOR
# ===================================

from jugador import Jugador


# ===================================
# AUTÓMATA NARRATIVO
# ===================================

from automata import AutomataNarrativo


# ===================================
# PILA DEL MUNDO
# ===================================

from pila_mundo import PilaMundo


# ===================================
# GRAMÁTICA
# ===================================

from gramatica import GramaticaDialogos


# ===================================
# SISTEMA DE FINALES
# ===================================

from finales import SistemaFinales


# ===================================
# NPC
# ===================================

from npc import Elena


# ===================================
# MISIÓN
# ===================================

from mision import Mision


# ===================================
# INVENTARIO
# ===================================

from inventario import Inventario


# ===================================
# OBJETOS
# ===================================

from objeto import (
    Medicamento,
    Pistola,
    Municion
)


# ===================================
# ENEMIGOS
# ===================================

from enemigo import (
    ZombiPolicia,
    ZombiCorredor
)


# ===================================
# COMBATE
# ===================================

from combate import Combate


# ===================================
# MAPAS
# ===================================

from mapa import (

    # Refugio
    crear_paredes_refugio,
    crear_salida_refugio,
    dibujar_refugio,

    # Calle
    crear_paredes_calle,
    crear_entrada_refugio,
    crear_entrada_hospital,
    crear_entrada_comisaria,
    dibujar_calle,

    # Hospital
    crear_paredes_hospital,
    crear_salida_hospital,
    crear_entrada_sotano_hospital,
    dibujar_hospital,

    # Sótano
    crear_paredes_sotano,
    crear_salida_sotano,
    dibujar_sotano,

    # Comisaría
    crear_paredes_comisaria,
    crear_salida_comisaria,
    dibujar_comisaria
)


# ===================================
# INTERFAZ
# ===================================

from interfaz import (
    mostrar_interaccion,
    mostrar_estado_afn,
    mostrar_dialogo,
    mostrar_mision,
    mostrar_inventario,
    mostrar_vida,
    mostrar_pila_mundo,
    mostrar_combate,
    mostrar_gramatica
)


# ===================================
# INICIAMOS PYGAME
# ===================================

pygame.init()


# ===================================
# VENTANA
# ===================================

pantalla = pygame.display.set_mode(
    (
        ANCHO_VENTANA,
        ALTO_VENTANA
    )
)


# Dibujamos siempre sobre una superficie lógica
# de 1000 x 650 para conservar todas las posiciones.
ventana = pygame.Surface(
    (
        ANCHO,
        ALTO
    )
)


pygame.display.set_caption(
    "Zona Cero: Ultimo Refugio"
)


# ===================================
# RELOJ
# ===================================

reloj = pygame.time.Clock()


# ===================================
# JUGADOR
# ===================================

jugador = Jugador()


# ===================================
# AUTÓMATA NARRATIVO
# ===================================

automata = AutomataNarrativo()


# ===================================
# PILA
# ===================================

pila_mundo = PilaMundo()


# ===================================
# GRAMÁTICA
# ===================================

gramatica = GramaticaDialogos()


# ===================================
# SISTEMA DE FINALES
# ===================================

sistema_finales = SistemaFinales()


# ===================================
# INVENTARIO
# ===================================

inventario = Inventario()


# ===================================
# NPC
# ===================================

elena = Elena()


# ===================================
# OBJETOS
# ===================================

medicamento = Medicamento()

pistola = Pistola()

municion = Municion()


# ===================================
# ENEMIGOS
# ===================================

zombi_comisaria = ZombiPolicia()

zombi_sotano = ZombiCorredor()


# ===================================
# COMBATE
# ===================================

combate = Combate()


# ===================================
# MISIÓN
# ===================================

mision_medicamentos = Mision(

    "Medicinas perdidas",

    gramatica.generar(
        "<MISION>"
    )
)


# ===================================
# DIÁLOGO
# ===================================

dialogo_actual = ""


# ===================================
# MOSTRAR GRAMÁTICA
# ===================================

mostrar_gramatica_activa = False


# ===================================
# REFUGIO
# ===================================

paredes_refugio = (
    crear_paredes_refugio()
)

salida_refugio = (
    crear_salida_refugio()
)


# ===================================
# CALLE
# ===================================

paredes_calle = (
    crear_paredes_calle()
)

entrada_refugio = (
    crear_entrada_refugio()
)

entrada_hospital = (
    crear_entrada_hospital()
)

entrada_comisaria = (
    crear_entrada_comisaria()
)


# ===================================
# HOSPITAL
# ===================================

paredes_hospital = (
    crear_paredes_hospital()
)

salida_hospital = (
    crear_salida_hospital()
)

entrada_sotano = (
    crear_entrada_sotano_hospital()
)


# ===================================
# SÓTANO
# ===================================

paredes_sotano = (
    crear_paredes_sotano()
)

salida_sotano = (
    crear_salida_sotano()
)


# ===================================
# COMISARÍA
# ===================================

paredes_comisaria = (
    crear_paredes_comisaria()
)

salida_comisaria = (
    crear_salida_comisaria()
)


# ===================================
# CONTROL PRINCIPAL
# ===================================

juego_activo = True


# ===================================
# CICLO PRINCIPAL
# ===================================

while juego_activo:


    # ===================================
    # EVENTOS
    # ===================================

    for evento in pygame.event.get():


        # -----------------------------------
        # CERRAR JUEGO
        # -----------------------------------

        if evento.type == pygame.QUIT:

            juego_activo = False


        # -----------------------------------
        # TECLAS
        # -----------------------------------

        if evento.type == pygame.KEYDOWN:


            # ===================================
            # COMBATE ACTIVO
            # ===================================

            if combate.activo == True:


                # -----------------------------------
                # ELEGIR ACCIÓN
                # -----------------------------------

                if combate.estado == "ELEGIR_ACCION":


                    # 1 = Golpear
                    if evento.key == pygame.K_1:

                        combate.golpear(
                            jugador
                        )


                    # 2 = Disparar
                    elif evento.key == pygame.K_2:

                        combate.disparar(
                            jugador,
                            inventario
                        )


                    # 3 = Defender
                    elif evento.key == pygame.K_3:

                        combate.defender(
                            jugador
                        )


                # -----------------------------------
                # VICTORIA
                # -----------------------------------

                elif combate.estado == "VICTORIA":

                    if evento.key == pygame.K_RETURN:

                        combate.terminar()


                        dialogo_actual = (
                            "Has derrotado al enemigo."
                        )


                # -----------------------------------
                # DERROTA
                # -----------------------------------

                elif combate.estado == "DERROTA":

                    if evento.key == pygame.K_RETURN:


                        # Guardamos cuál enemigo
                        # derrotó al jugador.
                        enemigo_actual = (
                            combate.enemigo
                        )


                        # Reiniciamos ese enemigo.
                        enemigo_actual.reiniciar()


                        # Recuperamos toda la vida.
                        jugador.vida = (
                            jugador.vida_maxima
                        )


                        # Regresamos al refugio.
                        automata.estado_actual = (
                            "REFUGIO"
                        )


                        jugador.cambiar_posicion(
                            150,
                            150
                        )


                        # Vaciamos la pila.
                        pila_mundo.vaciar()


                        # Terminamos el combate.
                        combate.terminar()


                        dialogo_actual = ""


            # ===================================
            # SIN COMBATE
            # ===================================

            else:


                # ===================================
                # PUNTO DE EVACUACIÓN
                # ===================================

                if (
                    automata.estado_actual
                    == "PUNTO_EVACUACION"
                ):


                    # -----------------------------------
                    # FINAL EVACUACIÓN
                    # -----------------------------------

                    if evento.key == pygame.K_1:

                        automata.cambiar_estado(
                            "ELEGIR_EVACUACION"
                        )


                    # -----------------------------------
                    # FINAL SACRIFICIO
                    # -----------------------------------

                    elif evento.key == pygame.K_2:

                        automata.cambiar_estado(
                            "ELEGIR_SACRIFICIO"
                        )


                    # -----------------------------------
                    # FINAL INFECTADO
                    # -----------------------------------

                    elif evento.key == pygame.K_3:

                        automata.cambiar_estado(
                            "ELEGIR_INFECTADO"
                        )


                    # -----------------------------------
                    # REGRESAR A LA CALLE
                    # -----------------------------------

                    elif evento.key == pygame.K_ESCAPE:

                        automata.cambiar_estado(
                            "REGRESAR_CALLE"
                        )


                        jugador.cambiar_posicion(
                            780,
                            300
                        )


                # ===================================
                # ESTADO DE ACEPTACIÓN
                # ===================================

                elif automata.es_estado_aceptacion():


                    # La tecla R nos permite
                    # regresar para probar
                    # los otros finales.
                    if evento.key == pygame.K_r:

                        automata.estado_actual = (
                            "CALLE"
                        )


                        jugador.cambiar_posicion(
                            780,
                            300
                        )


                # ===================================
                # MOSTRAR / CERRAR GLC
                # ===================================

                elif evento.key == pygame.K_g:

                    mostrar_gramatica_activa = (
                        not mostrar_gramatica_activa
                    )


                # ===================================
                # EXPLORAR CON EL AFN
                # ===================================

                elif (
                    evento.key == pygame.K_x
                    and
                    automata.estado_actual == "CALLE"
                    and
                    mostrar_gramatica_activa == False
                ):

                    automata.cambiar_estado(
                        "EXPLORAR"
                    )


                    destino_elegido = (
                        automata.estado_actual
                    )


                    # Ambos escenarios utilizan
                    # esta posición de entrada.
                    jugador.cambiar_posicion(
                        480,
                        500
                    )


                    dialogo_actual = (
                        "EXPLORAR eligio "
                        + destino_elegido
                        + " entre 2 destinos."
                    )


                    print()
                    print(
                        "AFN: EXPLORAR desde CALLE "
                        "puede ir a HOSPITAL o COMISARIA."
                    )
                    print(
                        "Destino elegido:",
                        destino_elegido
                    )


                # ===================================
                # INTERACCIONES CON E
                # ===================================

                elif (
                    evento.key == pygame.K_e
                    and
                    mostrar_gramatica_activa == False
                ):


                    # ===================================
                    # REFUGIO
                    # ===================================

                    if (
                        automata.estado_actual
                        == "REFUGIO"
                    ):


                        if jugador.rectangulo.colliderect(
                            salida_refugio
                        ):

                            automata.cambiar_estado(
                                "SALIR"
                            )


                            jugador.cambiar_posicion(
                                150,
                                300
                            )


                            dialogo_actual = ""


                    # ===================================
                    # CALLE
                    # ===================================

                    elif (
                        automata.estado_actual
                        == "CALLE"
                    ):


                        # -----------------------------------
                        # PUNTO DE EVACUACIÓN
                        # -----------------------------------

                        if jugador.rectangulo.colliderect(
                            sistema_finales.zona_entrada
                        ):


                            desbloqueado = (
                                sistema_finales.requisitos_completos(
                                    mision_medicamentos,
                                    zombi_comisaria,
                                    zombi_sotano
                                )
                            )


                            # Solo entramos si
                            # completamos los requisitos.
                            if desbloqueado == True:

                                automata.cambiar_estado(
                                    "ENTRAR_PUNTO_EVACUACION"
                                )


                                dialogo_actual = ""


                        # -----------------------------------
                        # REFUGIO
                        # -----------------------------------

                        elif jugador.rectangulo.colliderect(
                            entrada_refugio
                        ):

                            automata.cambiar_estado(
                                "ENTRAR_REFUGIO"
                            )


                            jugador.cambiar_posicion(
                                820,
                                310
                            )


                            dialogo_actual = ""


                        # -----------------------------------
                        # HOSPITAL
                        # -----------------------------------

                        elif jugador.rectangulo.colliderect(
                            entrada_hospital
                        ):

                            automata.cambiar_estado(
                                "ENTRAR_HOSPITAL"
                            )


                            jugador.cambiar_posicion(
                                480,
                                500
                            )


                            dialogo_actual = ""


                        # -----------------------------------
                        # COMISARÍA
                        # -----------------------------------

                        elif jugador.rectangulo.colliderect(
                            entrada_comisaria
                        ):

                            automata.cambiar_estado(
                                "ENTRAR_COMISARIA"
                            )


                            jugador.cambiar_posicion(
                                480,
                                500
                            )


                            dialogo_actual = ""


                    # ===================================
                    # HOSPITAL
                    # ===================================

                    elif (
                        automata.estado_actual
                        == "HOSPITAL"
                    ):


                        # -----------------------------------
                        # ELENA
                        # -----------------------------------

                        if jugador.rectangulo.colliderect(
                            elena.zona_interaccion
                        ):

                            dialogo_actual = elena.hablar(
                                mision_medicamentos,
                                inventario,
                                gramatica
                            )


                        # -----------------------------------
                        # MEDICAMENTO
                        # -----------------------------------

                        elif (
                            medicamento.recogido == False
                            and
                            jugador.rectangulo.colliderect(
                                medicamento.zona_interaccion
                            )
                        ):

                            medicamento.recoger(
                                inventario
                            )


                            dialogo_actual = (
                                "Has recogido el medicamento."
                            )


                            if (
                                mision_medicamentos.activa
                                == True
                            ):

                                mision_medicamentos.descripcion = (
                                    "Regresa con Elena."
                                )


                        # -----------------------------------
                        # BAJAR AL SÓTANO
                        # -----------------------------------

                        elif jugador.rectangulo.colliderect(
                            entrada_sotano
                        ):

                            # PUSH HOSPITAL
                            pila_mundo.apilar(
                                "HOSPITAL"
                            )


                            automata.cambiar_estado(
                                "BAJAR_SOTANO"
                            )


                            jugador.cambiar_posicion(
                                480,
                                160
                            )


                            dialogo_actual = ""


                        # -----------------------------------
                        # SALIR DEL HOSPITAL
                        # -----------------------------------

                        elif jugador.rectangulo.colliderect(
                            salida_hospital
                        ):

                            automata.cambiar_estado(
                                "SALIR_HOSPITAL"
                            )


                            jugador.cambiar_posicion(
                                820,
                                240
                            )


                            dialogo_actual = ""


                    # ===================================
                    # SÓTANO DEL HOSPITAL
                    # ===================================

                    elif (
                        automata.estado_actual
                        == "SOTANO_HOSPITAL"
                    ):


                        # -----------------------------------
                        # ZOMBI CORREDOR
                        # -----------------------------------

                        if (
                            zombi_sotano.vivo == True
                            and
                            jugador.rectangulo.colliderect(
                                zombi_sotano.zona_interaccion
                            )
                        ):

                            combate.iniciar(
                                zombi_sotano
                            )


                        # -----------------------------------
                        # SUBIR AL HOSPITAL
                        # -----------------------------------

                        elif jugador.rectangulo.colliderect(
                            salida_sotano
                        ):


                            # POP
                            lugar_anterior = (
                                pila_mundo.desapilar()
                            )


                            if (
                                lugar_anterior
                                == "HOSPITAL"
                            ):

                                automata.cambiar_estado(
                                    "SUBIR_HOSPITAL"
                                )


                                jugador.cambiar_posicion(
                                    170,
                                    310
                                )


                                dialogo_actual = ""


                    # ===================================
                    # COMISARÍA
                    # ===================================

                    elif (
                        automata.estado_actual
                        == "COMISARIA"
                    ):


                        # -----------------------------------
                        # ZOMBI POLICÍA
                        # -----------------------------------

                        if (
                            zombi_comisaria.vivo == True
                            and
                            jugador.rectangulo.colliderect(
                                zombi_comisaria.zona_interaccion
                            )
                        ):

                            combate.iniciar(
                                zombi_comisaria
                            )


                        # -----------------------------------
                        # PISTOLA
                        # -----------------------------------

                        elif (
                            zombi_comisaria.vivo == False
                            and
                            pistola.recogido == False
                            and
                            jugador.rectangulo.colliderect(
                                pistola.zona_interaccion
                            )
                        ):

                            pistola.recoger(
                                inventario
                            )


                            dialogo_actual = (
                                "Has encontrado una pistola."
                            )


                        # -----------------------------------
                        # MUNICIÓN
                        # -----------------------------------

                        elif (
                            zombi_comisaria.vivo == False
                            and
                            municion.recogido == False
                            and
                            jugador.rectangulo.colliderect(
                                municion.zona_interaccion
                            )
                        ):

                            municion.recoger(
                                inventario
                            )


                            dialogo_actual = (
                                "Has encontrado 12 balas."
                            )


                        # -----------------------------------
                        # SALIR DE LA COMISARÍA
                        # -----------------------------------

                        elif jugador.rectangulo.colliderect(
                            salida_comisaria
                        ):

                            automata.cambiar_estado(
                                "SALIR_COMISARIA"
                            )


                            jugador.cambiar_posicion(
                                150,
                                380
                            )


                            dialogo_actual = ""


    # ===================================
    # DIBUJAR REFUGIO
    # ===================================

    if automata.estado_actual == "REFUGIO":


        if mostrar_gramatica_activa == False:

            jugador.mover(
                paredes_refugio
            )


        dibujar_refugio(
            ventana,
            paredes_refugio
        )


        jugador.dibujar(
            ventana
        )


        if jugador.rectangulo.colliderect(
            salida_refugio
        ):

            mostrar_interaccion(
                ventana,
                "E - Salir del refugio"
            )


    # ===================================
    # DIBUJAR CALLE
    # ===================================

    elif automata.estado_actual == "CALLE":


        if mostrar_gramatica_activa == False:

            jugador.mover(
                paredes_calle
            )


        # Dibujamos calle.
        dibujar_calle(
            ventana,
            paredes_calle
        )


        # -----------------------------------
        # REVISAR SI EVACUACIÓN
        # ESTÁ DESBLOQUEADA
        # -----------------------------------

        desbloqueado = (
            sistema_finales.requisitos_completos(
                mision_medicamentos,
                zombi_comisaria,
                zombi_sotano
            )
        )


        # Dibujamos entrada de evacuación.
        sistema_finales.dibujar_entrada_calle(
            ventana,
            desbloqueado
        )


        # Dibujamos jugador.
        jugador.dibujar(
            ventana
        )


        # -----------------------------------
        # PUNTO DE EVACUACIÓN
        # -----------------------------------

        if jugador.rectangulo.colliderect(
            sistema_finales.zona_entrada
        ):


            if desbloqueado == True:

                mostrar_interaccion(
                    ventana,
                    "E - Ir al punto de evacuacion"
                )


            else:

                mostrar_interaccion(
                    ventana,
                    "Completa los objetivos principales"
                )


        # -----------------------------------
        # REFUGIO
        # -----------------------------------

        elif jugador.rectangulo.colliderect(
            entrada_refugio
        ):

            mostrar_interaccion(
                ventana,
                "E - Entrar al refugio"
            )


        # -----------------------------------
        # HOSPITAL
        # -----------------------------------

        elif jugador.rectangulo.colliderect(
            entrada_hospital
        ):

            mostrar_interaccion(
                ventana,
                "E - Entrar al hospital"
            )


        # -----------------------------------
        # COMISARÍA
        # -----------------------------------

        elif jugador.rectangulo.colliderect(
            entrada_comisaria
        ):

            mostrar_interaccion(
                ventana,
                "E - Entrar a la comisaria"
            )


    # ===================================
    # DIBUJAR HOSPITAL
    # ===================================

    elif automata.estado_actual == "HOSPITAL":


        # Elena se utiliza
        # también como obstáculo.
        paredes_hospital_actuales = (
            paredes_hospital
            +
            [elena.rectangulo]
        )


        if mostrar_gramatica_activa == False:

            jugador.mover(
                paredes_hospital_actuales
            )


        dibujar_hospital(
            ventana,
            paredes_hospital
        )


        # Medicamento.
        medicamento.dibujar(
            ventana
        )


        # Elena.
        elena.dibujar(
            ventana
        )


        # Jugador.
        jugador.dibujar(
            ventana
        )


        # -----------------------------------
        # ELENA
        # -----------------------------------

        if jugador.rectangulo.colliderect(
            elena.zona_interaccion
        ):

            mostrar_interaccion(
                ventana,
                "E - Hablar con Elena"
            )


        # -----------------------------------
        # MEDICAMENTO
        # -----------------------------------

        elif (
            medicamento.recogido == False
            and
            jugador.rectangulo.colliderect(
                medicamento.zona_interaccion
            )
        ):

            mostrar_interaccion(
                ventana,
                "E - Recoger medicamento"
            )


        # -----------------------------------
        # SÓTANO
        # -----------------------------------

        elif jugador.rectangulo.colliderect(
            entrada_sotano
        ):

            mostrar_interaccion(
                ventana,
                "E - Bajar al sotano"
            )


        # -----------------------------------
        # SALIDA
        # -----------------------------------

        elif jugador.rectangulo.colliderect(
            salida_hospital
        ):

            mostrar_interaccion(
                ventana,
                "E - Salir del hospital"
            )


        # -----------------------------------
        # DIÁLOGO
        # -----------------------------------

        if dialogo_actual != "":

            mostrar_dialogo(
                ventana,
                dialogo_actual
            )


    # ===================================
    # DIBUJAR SÓTANO
    # ===================================

    elif (
        automata.estado_actual
        == "SOTANO_HOSPITAL"
    ):


        # Si el zombi sigue vivo,
        # también funciona como obstáculo.
        if zombi_sotano.vivo == True:

            paredes_sotano_actuales = (
                paredes_sotano
                +
                [zombi_sotano.rectangulo]
            )

        else:

            paredes_sotano_actuales = (
                paredes_sotano
            )


        # Movimiento.
        if (
            combate.activo == False
            and
            mostrar_gramatica_activa == False
        ):

            jugador.mover(
                paredes_sotano_actuales
            )


        # Mapa.
        dibujar_sotano(
            ventana,
            paredes_sotano
        )


        # Enemigo.
        zombi_sotano.dibujar(
            ventana
        )


        # Jugador.
        jugador.dibujar(
            ventana
        )


        # -----------------------------------
        # ZOMBI CORREDOR
        # -----------------------------------

        if (
            combate.activo == False
            and
            zombi_sotano.vivo == True
            and
            jugador.rectangulo.colliderect(
                zombi_sotano.zona_interaccion
            )
        ):

            mostrar_interaccion(
                ventana,
                "E - Enfrentar zombi corredor"
            )


        # -----------------------------------
        # ESCALERAS
        # -----------------------------------

        elif (
            combate.activo == False
            and
            jugador.rectangulo.colliderect(
                salida_sotano
            )
        ):

            mostrar_interaccion(
                ventana,
                "E - Subir al hospital"
            )


        # -----------------------------------
        # DIÁLOGO
        # -----------------------------------

        if (
            dialogo_actual != ""
            and
            combate.activo == False
        ):

            mostrar_dialogo(
                ventana,
                dialogo_actual
            )


    # ===================================
    # DIBUJAR COMISARÍA
    # ===================================

    elif automata.estado_actual == "COMISARIA":


        # Si el zombi sigue vivo,
        # se utiliza como obstáculo.
        if zombi_comisaria.vivo == True:

            paredes_comisaria_actuales = (
                paredes_comisaria
                +
                [zombi_comisaria.rectangulo]
            )

        else:

            paredes_comisaria_actuales = (
                paredes_comisaria
            )


        # Movimiento.
        if (
            combate.activo == False
            and
            mostrar_gramatica_activa == False
        ):

            jugador.mover(
                paredes_comisaria_actuales
            )


        # Mapa.
        dibujar_comisaria(
            ventana,
            paredes_comisaria
        )


        # Zombi.
        zombi_comisaria.dibujar(
            ventana
        )


        # -----------------------------------
        # RECOMPENSAS
        # -----------------------------------

        if zombi_comisaria.vivo == False:

            pistola.dibujar(
                ventana
            )


            municion.dibujar(
                ventana
            )


        # Jugador.
        jugador.dibujar(
            ventana
        )


        # -----------------------------------
        # ZOMBI
        # -----------------------------------

        if (
            combate.activo == False
            and
            zombi_comisaria.vivo == True
            and
            jugador.rectangulo.colliderect(
                zombi_comisaria.zona_interaccion
            )
        ):

            mostrar_interaccion(
                ventana,
                "E - Enfrentar zombi"
            )


        # -----------------------------------
        # PISTOLA
        # -----------------------------------

        elif (
            combate.activo == False
            and
            zombi_comisaria.vivo == False
            and
            pistola.recogido == False
            and
            jugador.rectangulo.colliderect(
                pistola.zona_interaccion
            )
        ):

            mostrar_interaccion(
                ventana,
                "E - Recoger pistola"
            )


        # -----------------------------------
        # BALAS
        # -----------------------------------

        elif (
            combate.activo == False
            and
            zombi_comisaria.vivo == False
            and
            municion.recogido == False
            and
            jugador.rectangulo.colliderect(
                municion.zona_interaccion
            )
        ):

            mostrar_interaccion(
                ventana,
                "E - Recoger 12 balas"
            )


        # -----------------------------------
        # SALIDA
        # -----------------------------------

        elif (
            combate.activo == False
            and
            jugador.rectangulo.colliderect(
                salida_comisaria
            )
        ):

            mostrar_interaccion(
                ventana,
                "E - Salir de la comisaria"
            )


        # -----------------------------------
        # DIÁLOGO
        # -----------------------------------

        if (
            dialogo_actual != ""
            and
            combate.activo == False
        ):

            mostrar_dialogo(
                ventana,
                dialogo_actual
            )


    # ===================================
    # INTERFAZ GENERAL
    # ===================================

    # No mostramos la interfaz normal
    # encima de los finales.
    if (
        automata.estado_actual
        != "PUNTO_EVACUACION"
        and
        automata.es_estado_aceptacion()
        == False
    ):


        # Estado AFN.
        mostrar_estado_afn(
            ventana,
            automata.estado_actual
        )


        # Inventario.
        mostrar_inventario(
            ventana,
            inventario
        )


        # Vida.
        mostrar_vida(
            ventana,
            jugador
        )


        # Misión.
        mostrar_mision(
            ventana,
            mision_medicamentos
        )


        # Pila.
        mostrar_pila_mundo(
            ventana,
            pila_mundo
        )


    # ===================================
    # COMBATE
    # ===================================

    if combate.activo == True:

        mostrar_combate(
            ventana,
            combate,
            jugador,
            inventario
        )


    # ===================================
    # GRAMÁTICA
    # ===================================

    if mostrar_gramatica_activa == True:

        mostrar_gramatica(
            ventana,
            gramatica
        )


    # ===================================
    # PUNTO DE EVACUACIÓN
    # ===================================

    if (
        automata.estado_actual
        == "PUNTO_EVACUACION"
    ):

        sistema_finales.dibujar_menu_final(
            ventana
        )


    # ===================================
    # FINAL
    # ===================================

    elif automata.es_estado_aceptacion():

        sistema_finales.dibujar_final(
            ventana,
            automata.estado_actual
        )


    # ===================================
    # ACTUALIZAR PANTALLA
    # ===================================

    # Ampliamos la imagen completa sin cambiar
    # las colisiones ni las coordenadas del juego.
    pygame.transform.smoothscale(
        ventana,
        (
            ANCHO_VENTANA,
            ALTO_VENTANA
        ),
        pantalla
    )


    pygame.display.update()


    # ===================================
    # FPS
    # ===================================

    reloj.tick(
        FPS
    )


# ===================================
# CERRAR PYGAME
# ===================================

pygame.quit()
