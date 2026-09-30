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
    ANCHO_LATERAL,
    ALTO_CABECERA,
    ALTO_MENSAJES,
    ANCHO_INTERFAZ,
    ALTO_INTERFAZ,
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

from mision import Mision, DiarioMisiones


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
    mostrar_controles,
    mostrar_resumen_misiones,
    mostrar_diario,
    BOTONES_COMBATE,
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

# Diego: el mapa conserva su superficie original. La cabecera, la columna
# lateral y los mensajes tienen superficies separadas para no cubrirlo.
composicion = pygame.Surface((ANCHO_INTERFAZ, ALTO_INTERFAZ))
cabecera = composicion.subsurface((0, 0, ANCHO_INTERFAZ, ALTO_CABECERA))
lateral = composicion.subsurface((ANCHO, ALTO_CABECERA, ANCHO_LATERAL, ALTO))
mensajes = composicion.subsurface((0, ALTO_CABECERA + ALTO, ANCHO, ALTO_MENSAJES))

# Una sola escala para ambos ejes evita deformar el mapa al añadir la columna.
escala_interfaz = min(ANCHO_VENTANA / ANCHO_INTERFAZ, ALTO_VENTANA / ALTO_INTERFAZ)
tamano_interfaz = (
    round(ANCHO_INTERFAZ * escala_interfaz),
    round(ALTO_INTERFAZ * escala_interfaz)
)
interfaz_escalada = pygame.Surface(tamano_interfaz)
posicion_interfaz = (
    (ANCHO_VENTANA - tamano_interfaz[0]) // 2,
    (ALTO_VENTANA - tamano_interfaz[1]) // 2
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
mostrar_diario_activo = False
diario = DiarioMisiones()


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

    # Diego: limpiar también los mensajes evita que un aviso antiguo se quede
    # visible cuando el jugador deja de estar junto a un objeto o una puerta.
    composicion.fill((10, 18, 26))

    # ===================================
    # EVENTOS
    # ===================================

    for evento in pygame.event.get():


        # -----------------------------------
        # CERRAR JUEGO
        # -----------------------------------

        if evento.type == pygame.QUIT:

            juego_activo = False


        # Diego: el clic se traduce de la ventana ampliada al mapa lógico.
        # Los mismos rectángulos dibujan las acciones y detectan su selección.
        if (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1
                and combate.activo and combate.estado == "ELEGIR_ACCION"):
            punto = (
                (evento.pos[0] - posicion_interfaz[0]) / escala_interfaz,
                (evento.pos[1] - posicion_interfaz[1]) / escala_interfaz - ALTO_CABECERA
            )
            for indice, rect in enumerate(BOTONES_COMBATE):
                if rect.collidepoint(punto):
                    combate.elegir_accion(indice, jugador, inventario)
                    break


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


                    # Diego: selección de menú con flechas/Enter o atajos 1, 2 y 3.
                    if evento.key in (pygame.K_LEFT, pygame.K_UP):
                        combate.opcion = (combate.opcion - 1) % 3
                    elif evento.key in (pygame.K_RIGHT, pygame.K_DOWN):
                        combate.opcion = (combate.opcion + 1) % 3
                    elif evento.key == pygame.K_RETURN:
                        combate.elegir_accion(combate.opcion, jugador, inventario)
                    elif evento.key in (pygame.K_1, pygame.K_2, pygame.K_3):
                        combate.elegir_accion(evento.key - pygame.K_1, jugador, inventario)


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
                        automata.forzar_estado(
                            "REFUGIO",
                            "REINICIAR_DERROTA"
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

                        automata.forzar_estado(
                            "CALLE",
                            "REGRESAR_PRUEBA"
                        )


                        jugador.cambiar_posicion(
                            780,
                            300
                        )


                # ===================================
                # MOSTRAR / CERRAR GLC
                # ===================================

                elif evento.key == pygame.K_j:
                    # Diego: el diario pausa movimiento e interacciones del mundo.
                    mostrar_diario_activo = not mostrar_diario_activo
                    mostrar_gramatica_activa = False

                elif evento.key == pygame.K_ESCAPE:
                    mostrar_diario_activo = False
                    mostrar_gramatica_activa = False

                elif evento.key == pygame.K_g:
                    mostrar_diario_activo = False
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
                    mostrar_gramatica_activa == False and not mostrar_diario_activo
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
                    mostrar_gramatica_activa == False and not mostrar_diario_activo
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
                                zombi_sotano, jugador
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
                                zombi_comisaria, jugador
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

    # Diego: avanzar fases del combate y leer progreso antes de dibujar el HUD.
    combate.actualizar(jugador)
    diario.actualizar(mision_medicamentos, inventario, zombi_comisaria, zombi_sotano)
    jugador.moviendo = False

    if automata.estado_actual == "REFUGIO":


        if mostrar_gramatica_activa == False and not mostrar_diario_activo:

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
                mensajes,
                "E - Salir del refugio"
            )


    # ===================================
    # DIBUJAR CALLE
    # ===================================

    elif automata.estado_actual == "CALLE":


        if mostrar_gramatica_activa == False and not mostrar_diario_activo:

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
                    mensajes,
                    "E - Ir al punto de evacuacion"
                )


            else:

                mostrar_interaccion(
                    mensajes,
                    "Completa los objetivos principales"
                )


        # -----------------------------------
        # REFUGIO
        # -----------------------------------

        elif jugador.rectangulo.colliderect(
            entrada_refugio
        ):

            mostrar_interaccion(
                mensajes,
                "E - Entrar al refugio"
            )


        # -----------------------------------
        # HOSPITAL
        # -----------------------------------

        elif jugador.rectangulo.colliderect(
            entrada_hospital
        ):

            mostrar_interaccion(
                mensajes,
                "E - Entrar al hospital"
            )


        # -----------------------------------
        # COMISARÍA
        # -----------------------------------

        elif jugador.rectangulo.colliderect(
            entrada_comisaria
        ):

            mostrar_interaccion(
                mensajes,
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


        if mostrar_gramatica_activa == False and not mostrar_diario_activo:

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
                mensajes,
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
                mensajes,
                "E - Recoger medicamento"
            )


        # -----------------------------------
        # SÓTANO
        # -----------------------------------

        elif jugador.rectangulo.colliderect(
            entrada_sotano
        ):

            mostrar_interaccion(
                mensajes,
                "E - Bajar al sotano"
            )


        # -----------------------------------
        # SALIDA
        # -----------------------------------

        elif jugador.rectangulo.colliderect(
            salida_hospital
        ):

            mostrar_interaccion(
                mensajes,
                "E - Salir del hospital"
            )


        # -----------------------------------
        # DIÁLOGO
        # -----------------------------------

        if dialogo_actual != "":

            mostrar_dialogo(
                mensajes,
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
            mostrar_gramatica_activa == False and not mostrar_diario_activo
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
                mensajes,
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
                mensajes,
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
                mensajes,
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
            mostrar_gramatica_activa == False and not mostrar_diario_activo
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
                mensajes,
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
                mensajes,
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
                mensajes,
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
                mensajes,
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
                mensajes,
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
            cabecera,
            automata
        )


        # Inventario.
        mostrar_inventario(
            lateral,
            inventario
        )


        # Vida.
        mostrar_vida(
            lateral,
            jugador
        )


        # Misión.
        mostrar_resumen_misiones(lateral, diario, mision_medicamentos)


        # Pila.
        mostrar_pila_mundo(
            lateral,
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


    if mostrar_diario_activo and not combate.activo:
        mostrar_diario(ventana, diario)


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

    # Diego: durante la partida colocamos el mapa entre cabecera y mensajes.
    # Los finales conservan su presentación de pantalla completa.
    if automata.estado_actual == "PUNTO_EVACUACION" or automata.es_estado_aceptacion():
        pygame.transform.smoothscale(ventana, (ANCHO_VENTANA, ALTO_VENTANA), pantalla)
    else:
        mostrar_controles(lateral)
        composicion.blit(ventana, (0, ALTO_CABECERA))
        pygame.transform.smoothscale(composicion, tamano_interfaz, interfaz_escalada)
        pantalla.fill((10, 18, 26))
        pantalla.blit(interfaz_escalada, posicion_interfaz)


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
