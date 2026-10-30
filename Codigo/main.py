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

from cinematicas import CinematicasFinales











# ===================================



# NPC



# ===================================







from npc import (

    Elena,

    Marcos

)











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



    Municion,



    Radio,

    ArchivoMilitar



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



    dibujar_comisaria,

    crear_entrada_base_militar,

    crear_paredes_base_militar,

    crear_salida_base_militar,

    dibujar_base_militar



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



    mostrar_gramatica,



    cambiar_pagina_gramatica



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



    ),
    pygame.RESIZABLE



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







# Una sola escala para ambos ejes conserva el mapa y las coordenadas lógicas.
def recalcular_interfaz():
    ancho_actual, alto_actual = pantalla.get_size()
    escala = min(ancho_actual / ANCHO_INTERFAZ, alto_actual / ALTO_INTERFAZ)
    tamano = (
        max(1, round(ANCHO_INTERFAZ * escala)),
        max(1, round(ALTO_INTERFAZ * escala))
    )
    posicion = (
        (ancho_actual - tamano[0]) // 2,
        (alto_actual - tamano[1]) // 2
    )
    return escala, tamano, pygame.Surface(tamano), posicion


escala_interfaz, tamano_interfaz, interfaz_escalada, posicion_interfaz = recalcular_interfaz()


pygame.display.set_caption(



    "Zona Cero: Ultimo Refugio"



)











from inicio import mostrar_inicio

if not mostrar_inicio(pantalla):
    pygame.quit()
    raise SystemExit

# El menú puede haber cambiado el tamaño de la ventana.
escala_interfaz, tamano_interfaz, interfaz_escalada, posicion_interfaz = recalcular_interfaz()


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

cinematicas_finales = CinematicasFinales()











# ===================================



# INVENTARIO



# ===================================







inventario = Inventario()











# ===================================



# NPC



# ===================================







elena = Elena()



marcos = Marcos()











# ===================================



# OBJETOS



# ===================================







medicamento = Medicamento()







pistola = Pistola()







municion = Municion()



radio = Radio()


archivo_militar = ArchivoMilitar()











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







# Misión secundaria de Marcos.



mision_radio = Mision(



    "Señal perdida",



    gramatica.generar(



        "<MISION_MARCOS>"



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







entrada_base_militar = crear_entrada_base_militar()

paredes_base_militar = crear_paredes_base_militar()

salida_base_militar = crear_salida_base_militar()



juego_activo = True











# ===================================



# CICLO PRINCIPAL



# ===================================







from audio_juego import AudioJuego
from dialogos_ui import DialogoUI

audio_juego = AudioJuego()
dialogo_ui = DialogoUI()
inicio_fundido = pygame.time.get_ticks()

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







        # Esc cierra primero los paneles; después abre la pausa incluso en combate.
        solicitar_pausa = (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE)
        if solicitar_pausa and (mostrar_diario_activo or mostrar_gramatica_activa):
            mostrar_diario_activo = False
            mostrar_gramatica_activa = False
            continue
        if evento.type == pygame.QUIT or solicitar_pausa:
            inicio_pausa = pygame.time.get_ticks()
            dialogo_ui.visibilidad(False)
            audio_juego.suspender()
            resultado_pausa = mostrar_inicio(pantalla, pausa=True, confirmar=evento.type == pygame.QUIT)
            if resultado_pausa == "menu":
                resultado_pausa = mostrar_inicio(pantalla, partida_activa=True)
            audio_juego.reanudar()
            dialogo_ui.visibilidad(True)
            duracion_pausa = pygame.time.get_ticks() - inicio_pausa
            # Descontamos la pausa de los relojes existentes sin cambiar sus reglas.
            if combate.activo:
                combate.inicio_fase += duracion_pausa
            if cinematicas_finales.estado is not None:
                cinematicas_finales.inicio += duracion_pausa
            for mision_pausada in (mision_medicamentos, mision_radio):
                if mision_pausada.tiempo_completada:
                    mision_pausada.tiempo_completada += duracion_pausa
            escala_interfaz, tamano_interfaz, interfaz_escalada, posicion_interfaz = recalcular_interfaz()
            if not resultado_pausa:
                juego_activo = False
            # Descarta entradas capturadas antes de abrir el menú.
            break

        # Pygame 2 actualiza la superficie también al maximizar/restaurar.
        if evento.type in (pygame.VIDEORESIZE, pygame.WINDOWSIZECHANGED):
            escala_interfaz, tamano_interfaz, interfaz_escalada, posicion_interfaz = recalcular_interfaz()

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







        if (evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE
                and not combate.activo and not mostrar_diario_activo
                and not mostrar_gramatica_activa and dialogo_ui.escribiendo
                and dialogo_ui.mensaje == dialogo_actual):
            dialogo_ui.revelar()
            continue

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

                        cinematicas_finales.iniciar(
                            automata.estado_actual
                        )











                    # -----------------------------------



                    # FINAL SACRIFICIO



                    # -----------------------------------







                    elif evento.key == pygame.K_2:







                        automata.cambiar_estado(



                            "ELEGIR_SACRIFICIO"



                        )

                        cinematicas_finales.iniciar(
                            automata.estado_actual
                        )











                    # -----------------------------------



                    # FINAL INFECTADO



                    # -----------------------------------







                    elif evento.key == pygame.K_3:







                        automata.cambiar_estado(



                            "ELEGIR_INFECTADO"



                        )

                        cinematicas_finales.iniciar(
                            automata.estado_actual
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

                    # Mientras la cinemática está activa,
                    # ENTER o ESPACIO permite saltarla.
                    if cinematicas_finales.terminada == False:

                        if evento.key in (
                            pygame.K_RETURN,
                            pygame.K_SPACE
                        ):

                            cinematicas_finales.saltar()

                    # Cuando termina la cinemática,
                    # R permite probar otro final como antes.
                    elif evento.key == pygame.K_r:

                        automata.forzar_estado(
                            "CALLE",
                            "REGRESAR_PRUEBA"
                        )

                        cinematicas_finales.reiniciar()

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







                elif (

                    mostrar_gramatica_activa == True

                    and

                    evento.key == pygame.K_a

                ):

                    cambiar_pagina_gramatica(-1)



                elif (

                    mostrar_gramatica_activa == True

                    and

                    evento.key == pygame.K_d

                ):

                    cambiar_pagina_gramatica(1)



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







                        elif jugador.rectangulo.colliderect(entrada_base_militar):

                            # La tarjeta es una condición del mundo, fuera del AFN.

                            if inventario.tiene("Tarjeta Militar"):

                                automata.cambiar_estado("ENTRAR_BASE_MILITAR")

                                jugador.cambiar_posicion(480, 500)

                                dialogo_actual = ""

                            else:

                                dialogo_actual = "Acceso bloqueado. Necesitas la Tarjeta Militar."



                    elif automata.estado_actual == "BASE_MILITAR":

                        # -----------------------------------
                        # ARCHIVO MILITAR
                        # -----------------------------------

                        if (
                            archivo_militar.recogido == False
                            and
                            jugador.rectangulo.colliderect(
                                archivo_militar.zona_interaccion
                            )
                        ):

                            archivo_militar.recoger(
                                inventario
                            )

                            dialogo_actual = (
                                "Archivo confidencial recuperado: "
                                "el ultimo convoy saldra desde "
                                "el punto de evacuacion."
                            )

                        # -----------------------------------
                        # SALIR DE LA BASE MILITAR
                        # -----------------------------------

                        elif jugador.rectangulo.colliderect(
                            salida_base_militar
                        ):

                            automata.cambiar_estado(
                                "SALIR_BASE_MILITAR"
                            )

                            jugador.cambiar_posicion(
                                340,
                                150
                            )

                            dialogo_actual = ""

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
                            dialogo_ui.iniciar("elena", dialogo_actual)
                            audio_juego.dialogo("elena")











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

                        # SUBIR AL HOSPITAL

                        # -----------------------------------



                        if jugador.rectangulo.colliderect(



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



                        # MARCOS



                        # -----------------------------------







                        if jugador.rectangulo.colliderect(



                            marcos.zona_interaccion



                        ):







                            dialogo_actual = marcos.hablar(



                                mision_radio,



                                inventario,



                                gramatica



                            )
                            dialogo_ui.iniciar("marcos", dialogo_actual)
                            audio_juego.dialogo("marcos")







                        # -----------------------------------



                        # RADIO



                        # -----------------------------------







                        elif (



                            mision_radio.activa == True



                            and



                            mision_radio.completada == False



                            and



                            radio.recogido == False



                            and



                            jugador.rectangulo.colliderect(



                                radio.zona_interaccion



                            )



                        ):







                            radio.recoger(



                                inventario



                            )







                            mision_radio.descripcion = (



                                "Regresa con Marcos."



                            )







                            dialogo_actual = (



                                "Has encontrado la radio."



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



    if not juego_activo:
        break

    combate.actualizar(jugador)



    diario.actualizar(

        mision_medicamentos,

        mision_radio,

        inventario,

        zombi_comisaria,

        zombi_sotano

    )



    dialogo_ui.sincronizar(dialogo_actual, automata.estado_actual)
    dialogo_ui.visibilidad(not combate.activo and not mostrar_gramatica_activa
                           and not mostrar_diario_activo)
    if dialogo_ui.caducado:
        # Limpiamos también el mensaje para que no reaparezca como aviso genérico.
        dialogo_actual = ""
        dialogo_ui.sincronizar(dialogo_actual, automata.estado_actual)
    ventana_interaccion = (None if combate.activo or mostrar_gramatica_activa
                           or mostrar_diario_activo else ventana)
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



                "E - Salir del refugio", ventana_interaccion, jugador



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



                    "E - Ir al punto de evacuacion", ventana_interaccion, jugador



                )











            else:







                mostrar_interaccion(



                    mensajes,



                    "Completa los objetivos principales", ventana_interaccion, jugador



                )











        # -----------------------------------



        # REFUGIO



        # -----------------------------------







        elif jugador.rectangulo.colliderect(



            entrada_refugio



        ):







            mostrar_interaccion(



                mensajes,



                "E - Entrar al refugio", ventana_interaccion, jugador



            )











        # -----------------------------------



        # HOSPITAL



        # -----------------------------------







        elif jugador.rectangulo.colliderect(



            entrada_hospital



        ):







            mostrar_interaccion(



                mensajes,



                "E - Entrar al hospital", ventana_interaccion, jugador



            )











        # -----------------------------------



        # COMISARÍA



        # -----------------------------------







        elif jugador.rectangulo.colliderect(



            entrada_comisaria



        ):







            mostrar_interaccion(



                mensajes,



                "E - Entrar a la comisaria", ventana_interaccion, jugador



            )











    # ===================================



    # DIBUJAR HOSPITAL



    # ===================================







        elif jugador.rectangulo.colliderect(entrada_base_militar):

            mostrar_interaccion(mensajes,
                                "E - Entrar a la Base Militar" if inventario.tiene("Tarjeta Militar")
                                else "Necesitas la Tarjeta Militar", ventana_interaccion, jugador)

            if dialogo_actual:

                mostrar_dialogo(mensajes, dialogo_actual, dialogo_ui)



    elif automata.estado_actual == "BASE_MILITAR":

        if not mostrar_gramatica_activa and not mostrar_diario_activo:

            jugador.mover(
                paredes_base_militar
            )

        dibujar_base_militar(
            ventana,
            paredes_base_militar
        )

        # Documento confidencial.
        archivo_militar.dibujar(
            ventana
        )

        jugador.dibujar(
            ventana
        )

        # -----------------------------------
        # ARCHIVO MILITAR
        # -----------------------------------

        if (
            archivo_militar.recogido == False
            and
            jugador.rectangulo.colliderect(
                archivo_militar.zona_interaccion
            )
        ):

            mostrar_interaccion(
                mensajes,
                "E - Examinar archivo militar", ventana_interaccion, jugador
            )

        # -----------------------------------
        # SALIDA
        # -----------------------------------

        elif jugador.rectangulo.colliderect(
            salida_base_militar
        ):

            mostrar_interaccion(
                mensajes,
                "E - Salir a la calle", ventana_interaccion, jugador
            )

        # -----------------------------------
        # MENSAJE DEL ARCHIVO
        # -----------------------------------

        if dialogo_actual != "":

            mostrar_dialogo(
                mensajes,
                dialogo_actual, dialogo_ui
            )

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



                "E - Hablar con Elena", ventana_interaccion, jugador



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



                "E - Recoger medicamento", ventana_interaccion, jugador



            )











        # -----------------------------------



        # SÓTANO



        # -----------------------------------







        elif jugador.rectangulo.colliderect(



            entrada_sotano



        ):







            mostrar_interaccion(



                mensajes,



                "E - Bajar al sotano", ventana_interaccion, jugador



            )











        # -----------------------------------



        # SALIDA



        # -----------------------------------







        elif jugador.rectangulo.colliderect(



            salida_hospital



        ):







            mostrar_interaccion(



                mensajes,



                "E - Salir del hospital", ventana_interaccion, jugador



            )











        # -----------------------------------



        # DIÁLOGO



        # -----------------------------------







        if dialogo_actual != "":







            mostrar_dialogo(



                mensajes,



                dialogo_actual, dialogo_ui



            )











    # ===================================



    # DIBUJAR SÓTANO



    # ===================================







    elif (



        automata.estado_actual



        == "SOTANO_HOSPITAL"



    ):











                # -----------------------------------
        # PERSECUCIÓN DEL ZOMBI CORREDOR
        # -----------------------------------

        if (

            combate.activo == False

            and

            zombi_sotano.vivo == True

            and

            mostrar_gramatica_activa == False

            and

            not mostrar_diario_activo

        ):

            zombi_sotano.perseguir(

                jugador,

                paredes_sotano

            )


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


        # -----------------------------------
        # COMBATE AUTOMATICO
        # -----------------------------------

        if (

            combate.activo == False

            and

            zombi_sotano.vivo == True

            and

            zombi_sotano.puede_iniciar_combate(
                jugador
            )

        ):

            combate.iniciar(
                zombi_sotano,
                jugador
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



        # ESCALERAS



        # -----------------------------------







        if (



            combate.activo == False



            and



            jugador.rectangulo.colliderect(



                salida_sotano



            )



        ):







            mostrar_interaccion(



                mensajes,



                "E - Subir al hospital", ventana_interaccion, jugador



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



                dialogo_actual, dialogo_ui



            )











    # ===================================



    # DIBUJAR COMISARÍA



    # ===================================







    elif automata.estado_actual == "COMISARIA":







        # Marcos también funciona como obstáculo.



        paredes_comisaria_actuales = (



            paredes_comisaria



            +



            [marcos.rectangulo]



        )







                # -----------------------------------
        # PERSECUCIÓN DEL ZOMBI POLICÍA
        # -----------------------------------

        if (

            combate.activo == False

            and

            zombi_comisaria.vivo == True

            and

            mostrar_gramatica_activa == False

            and

            not mostrar_diario_activo

        ):

            # El zombi respeta las paredes
            # y tampoco atraviesa a Marcos.
            zombi_comisaria.perseguir(

                jugador,

                paredes_comisaria_actuales

            )


# Si el zombi sigue vivo, también funciona como obstáculo.



        if zombi_comisaria.vivo == True:







            paredes_comisaria_actuales = (



                paredes_comisaria_actuales



                +



                [zombi_comisaria.rectangulo]



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


        # -----------------------------------
        # COMBATE AUTOMATICO
        # -----------------------------------

        if (

            combate.activo == False

            and

            zombi_comisaria.vivo == True

            and

            zombi_comisaria.puede_iniciar_combate(
                jugador
            )

        ):

            combate.iniciar(
                zombi_comisaria,
                jugador
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







        # Radio: aparece solo mientras la misión de Marcos está activa.



        if (



            mision_radio.activa == True



            and



            mision_radio.completada == False



        ):







            radio.dibujar(



                ventana



            )







        # Marcos.



        marcos.dibujar(



            ventana



        )







        # Recompensas del zombi.



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



        # MARCOS



        # -----------------------------------







        if (



            combate.activo == False



            and



            jugador.rectangulo.colliderect(



                marcos.zona_interaccion



            )



        ):







            mostrar_interaccion(



                mensajes,



                "E - Hablar con Marcos", ventana_interaccion, jugador



            )







        # -----------------------------------



        # RADIO



        # -----------------------------------







        elif (



            combate.activo == False



            and



            mision_radio.activa == True



            and



            mision_radio.completada == False



            and



            radio.recogido == False



            and



            jugador.rectangulo.colliderect(



                radio.zona_interaccion



            )



        ):







            mostrar_interaccion(



                mensajes,



                "E - Recoger radio", ventana_interaccion, jugador



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



                "E - Recoger pistola", ventana_interaccion, jugador



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



                "E - Recoger 12 balas", ventana_interaccion, jugador



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



                "E - Salir de la comisaria", ventana_interaccion, jugador



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



                dialogo_actual, dialogo_ui



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

        # Primero mostramos la cinemática correspondiente.
        if cinematicas_finales.terminada == False:

            cinematicas_finales.dibujar(
                ventana,
                automata.estado_actual
            )

        # Después conservamos la pantalla final formal
        # que ya existía en finales.py.
        else:

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



        ancho_actual, alto_actual = pantalla.get_size()
        escala_final = min(ancho_actual / ANCHO, alto_actual / ALTO)
        tamano_final = (
            max(1, round(ANCHO * escala_final)),
            max(1, round(ALTO * escala_final))
        )
        posicion_final = (
            (ancho_actual - tamano_final[0]) // 2,
            (alto_actual - tamano_final[1]) // 2
        )
        pantalla.fill((10, 18, 26))
        pantalla.blit(pygame.transform.smoothscale(ventana, tamano_final), posicion_final)



    else:



        mostrar_controles(lateral)



        if combate.activo or mostrar_gramatica_activa or mostrar_diario_activo:
            mensajes.fill((10, 18, 26))
        composicion.blit(ventana, (0, ALTO_CABECERA))



        pygame.transform.scale(composicion, tamano_interfaz, interfaz_escalada)



        pantalla.fill((10, 18, 26))



        pantalla.blit(interfaz_escalada, posicion_interfaz)











    # Fundido de entrada: la escena ya usa el tamaño actual de la ventana.
    tiempo_fundido = pygame.time.get_ticks() - inicio_fundido
    if tiempo_fundido < 650:
        velo_entrada = pygame.Surface(pantalla.get_size())
        velo_entrada.fill((0, 0, 0))
        velo_entrada.set_alpha(round(255 * (1 - tiempo_fundido / 650)))
        pantalla.blit(velo_entrada, (0, 0))

    dialogo_visible = (not combate.activo and not mostrar_diario_activo
                       and not mostrar_gramatica_activa)
    dialogo_ui.visibilidad(dialogo_visible)
    audio_juego.actualizar_dialogo(dialogo_ui.personaje, dialogo_visible and dialogo_ui.escribiendo)
    audio_juego.actualizar(combate)
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







audio_juego.detener()
pygame.quit()
