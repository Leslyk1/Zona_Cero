# -----------------------------------
# AUTÓMATA NARRATIVO DEL JUEGO
# -----------------------------------

import random

class AutomataNarrativo:

    def __init__(self):

        # Estado inicial.
        self.estado_actual = "REFUGIO"

        # Datos de la última transición.
        # Se muestran en la interfaz para
        # poder explicar el recorrido del AFN.
        self.estado_anterior = None

        self.ultima_accion = ""

        self.ultimos_posibles = []


        # -----------------------------------
        # ESTADOS DE ACEPTACIÓN
        # -----------------------------------

        self.estados_aceptacion = [

            "FINAL_EVACUACION",

            "FINAL_SACRIFICIO",

            "FINAL_INFECTADO"
        ]


        # -----------------------------------
        # TRANSICIONES
        # -----------------------------------

        self.transiciones = {


            # ===================================
            # REFUGIO
            # ===================================

            "REFUGIO": {

                "SALIR": [
                    "CALLE"
                ]
            },


            # ===================================
            # CALLE
            # ===================================

            "CALLE": {

                "ENTRAR_REFUGIO": [
                    "REFUGIO"
                ],

                "ENTRAR_HOSPITAL": [
                    "HOSPITAL"
                ],

                "ENTRAR_COMISARIA": [
                    "COMISARIA"
                ],

                # Una misma acción puede conducir
                # a dos estados diferentes.
                "EXPLORAR": [
                    "HOSPITAL",
                    "COMISARIA"
                ],

                "ENTRAR_PUNTO_EVACUACION": [
                    "PUNTO_EVACUACION"
                ]
            },


            # ===================================
            # HOSPITAL
            # ===================================

            "HOSPITAL": {

                "SALIR_HOSPITAL": [
                    "CALLE"
                ],

                "BAJAR_SOTANO": [
                    "SOTANO_HOSPITAL"
                ]
            },


            # ===================================
            # SÓTANO
            # ===================================

            "SOTANO_HOSPITAL": {

                "SUBIR_HOSPITAL": [
                    "HOSPITAL"
                ]
            },


            # ===================================
            # COMISARÍA
            # ===================================

            "COMISARIA": {

                "SALIR_COMISARIA": [
                    "CALLE"
                ]
            },


            # ===================================
            # PUNTO DE EVACUACIÓN
            # ===================================

            "PUNTO_EVACUACION": {

                "ELEGIR_EVACUACION": [
                    "FINAL_EVACUACION"
                ],

                "ELEGIR_SACRIFICIO": [
                    "FINAL_SACRIFICIO"
                ],

                "ELEGIR_INFECTADO": [
                    "FINAL_INFECTADO"
                ],

                "REGRESAR_CALLE": [
                    "CALLE"
                ]
            },


            # ===================================
            # ESTADOS FINALES
            # ===================================

            "FINAL_EVACUACION": {},

            "FINAL_SACRIFICIO": {},

            "FINAL_INFECTADO": {}
        }


    # ===================================
    # CAMBIAR ESTADO
    # ===================================

    def cambiar_estado(
        self,
        accion
    ):

        # Revisamos si existe
        # el estado actual.
        if self.estado_actual in self.transiciones:

            acciones = self.transiciones[
                self.estado_actual
            ]


            # Revisamos si la acción existe.
            if accion in acciones:

                posibles_estados = acciones[
                    accion
                ]


                # Si existe más de un destino,
                # simulamos una ejecución del AFN
                # eligiendo uno de los posibles.
                nuevo_estado = random.choice(
                    posibles_estados
                )


                self.estado_anterior = (
                    self.estado_actual
                )


                self.ultima_accion = accion


                self.ultimos_posibles = list(
                    posibles_estados
                )


                self.estado_actual = (
                    nuevo_estado
                )


                return True


        return False


    # ===================================
    # CAMBIO DIRECTO DEL JUEGO
    # ===================================

    def forzar_estado(
        self,
        nuevo_estado,
        accion
    ):

        # Se utiliza al reiniciar después
        # de una derrota o desde un final.
        self.estado_anterior = (
            self.estado_actual
        )

        self.ultima_accion = accion

        self.ultimos_posibles = [
            nuevo_estado
        ]

        self.estado_actual = nuevo_estado


    # ===================================
    # REVISAR ESTADO DE ACEPTACIÓN
    # ===================================

    def es_estado_aceptacion(
        self
    ):

        if (
            self.estado_actual
            in
            self.estados_aceptacion
        ):

            return True


        return False
