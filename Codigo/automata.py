# -----------------------------------
# AUTÓMATA NARRATIVO DEL JUEGO
# -----------------------------------

class AutomataNarrativo:

    def __init__(self):

        # Estado inicial.
        self.estado_actual = "REFUGIO"


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


                nuevo_estado = (
                    posibles_estados[0]
                )


                self.estado_actual = (
                    nuevo_estado
                )


                return True


        return False


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