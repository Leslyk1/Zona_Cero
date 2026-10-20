# ===================================
# GRAMÁTICA LIBRE DE CONTEXTO
# PARA DIÁLOGOS Y MISIONES
# ===================================

# Importamos random para poder escoger
# distintas producciones de la gramática.
import random


class GramaticaDialogos:

    def __init__(self):

        self.reglas = {

            # ===================================
            # ELENA
            # ===================================

            "<DIALOGO_INICIO>": [
                [
                    "<NPC>",
                    "<PETICION>"
                ]
            ],

            "<DIALOGO_RECORDATORIO>": [
                [
                    "<NPC>",
                    "<RECORDATORIO>"
                ]
            ],

            "<DIALOGO_FINAL>": [
                [
                    "<NPC>",
                    "<AGRADECIMIENTO>"
                ]
            ],

            "<NPC>": [
                [
                    "Elena:"
                ]
            ],

            "<PETICION>": [
                [
                    "Necesito tu ayuda.",
                    "<MISION>"
                ],
                [
                    "Tenemos un problema.",
                    "<MISION>"
                ]
            ],

            "<MISION>": [
                [
                    "<ACCION>",
                    "<OBJETO>",
                    "<LUGAR>"
                ]
            ],

            "<ACCION>": [
                [
                    "Busca"
                ],
                [
                    "Encuentra"
                ],
                [
                    "Localiza"
                ]
            ],

            "<OBJETO>": [
                [
                    "medicamentos"
                ]
            ],

            # Las dos opciones siguen siendo
            # correctas para el mapa del Hospital.
            "<LUGAR>": [
                [
                    "en el hospital."
                ],
                [
                    "dentro del hospital."
                ]
            ],

            "<RECORDATORIO>": [
                [
                    "Todavia necesito los medicamentos."
                ],
                [
                    "No olvides traer los medicamentos."
                ]
            ],

            "<AGRADECIMIENTO>": [
                [
                    "Gracias por traer los medicamentos."
                ],
                [
                    "Lo lograste. Gracias por los medicamentos."
                ]
            ],


            # ===================================
            # MARCOS
            # ===================================

            "<DIALOGO_MARCOS_INICIO>": [
                [
                    "<NPC_MARCOS>",
                    "<PETICION_MARCOS>"
                ]
            ],

            "<DIALOGO_MARCOS_RECORDATORIO>": [
                [
                    "<NPC_MARCOS>",
                    "<RECORDATORIO_MARCOS>"
                ]
            ],

            "<DIALOGO_MARCOS_FINAL>": [
                [
                    "<NPC_MARCOS>",
                    "<AGRADECIMIENTO_MARCOS>"
                ]
            ],

            "<NPC_MARCOS>": [
                [
                    "Marcos:"
                ]
            ],

            "<PETICION_MARCOS>": [
                [
                    "Necesito una radio para contactar a los militares.",
                    "<MISION_MARCOS>"
                ],
                [
                    "Debemos recuperar una radio para pedir ayuda.",
                    "<MISION_MARCOS>"
                ]
            ],

            "<MISION_MARCOS>": [
                [
                    "<ACCION_MARCOS>",
                    "<OBJETO_MARCOS>",
                    "<LUGAR_MARCOS>"
                ]
            ],

            "<ACCION_MARCOS>": [
                [
                    "Busca"
                ],
                [
                    "Encuentra"
                ],
                [
                    "Localiza"
                ]
            ],

            "<OBJETO_MARCOS>": [
                [
                    "la radio"
                ]
            ],

            "<LUGAR_MARCOS>": [
                [
                    "en el archivo de la comisaria."
                ]
            ],

            "<RECORDATORIO_MARCOS>": [
                [
                    "Todavia necesito la radio."
                ],
                [
                    "Recuerda que necesitamos recuperar la radio."
                ]
            ],

            "<AGRADECIMIENTO_MARCOS>": [
                [
                    "Gracias por traer la radio. Toma esta tarjeta militar."
                ],
                [
                    "La radio funciona. Toma esta tarjeta militar como recompensa."
                ]
            ]
        }


    # ===================================
    # GENERAR CADENA
    # ===================================

    def generar(
        self,
        simbolo
    ):

        # Si el símbolo no está dentro
        # de las reglas, significa que
        # es un símbolo terminal.
        if simbolo not in self.reglas:

            return simbolo


        # Antes siempre utilizábamos:
        #
        # self.reglas[simbolo][0]
        #
        # Eso hacía que siempre se
        # escogiera la primera opción.
        #
        # Ahora escogemos una producción
        # de manera aleatoria.

        produccion = random.choice(
            self.reglas[
                simbolo
            ]
        )


        resultado = []


        # Recorremos cada parte
        # de la producción.
        for parte in produccion:

            texto = self.generar(
                parte
            )

            resultado.append(
                texto
            )


        return " ".join(
            resultado
        )


    # ===================================
    # DERIVACIÓN POR LA IZQUIERDA
    # ===================================

    def obtener_derivacion(
        self,
        simbolo_inicial
    ):

        # Para mostrar la derivación
        # formal utilizamos siempre
        # la primera producción.
        #
        # Así la derivación que aparece
        # en pantalla es estable y fácil
        # de explicar durante la defensa.

        actual = [
            simbolo_inicial
        ]

        pasos = []

        pasos.append(
            " ".join(actual)
        )

        continuar = True


        while continuar:

            continuar = False

            # Recorremos de izquierda
            # a derecha.
            for posicion in range(
                len(actual)
            ):

                simbolo = actual[
                    posicion
                ]


                # Encontramos el primer
                # no terminal.
                if simbolo in self.reglas:

                    # Para la demostración
                    # formal usamos la
                    # primera producción.
                    produccion = (
                        self.reglas[
                            simbolo
                        ][0]
                    )

                    actual = (
                        actual[:posicion]
                        +
                        produccion
                        +
                        actual[posicion + 1:]
                    )

                    pasos.append(
                        " ".join(actual)
                    )

                    continuar = True

                    # break hace que siempre
                    # reemplacemos primero
                    # el símbolo que se encuentra
                    # más a la izquierda.
                    break


        return pasos


    # ===================================
    # OBTENER BNF
    # ===================================

    def obtener_bnf(self):

        reglas_bnf = [

            # ===================================
            # ELENA
            # ===================================

            "<DIALOGO_INICIO> ::= <NPC> <PETICION>",

            "<DIALOGO_RECORDATORIO> ::= <NPC> <RECORDATORIO>",

            "<DIALOGO_FINAL> ::= <NPC> <AGRADECIMIENTO>",

            '<NPC> ::= "Elena:"',

            (
                '<PETICION> ::= '
                '"Necesito tu ayuda." <MISION> '
                '| "Tenemos un problema." <MISION>'
            ),

            "<MISION> ::= <ACCION> <OBJETO> <LUGAR>",

            (
                '<ACCION> ::= '
                '"Busca" | "Encuentra" | "Localiza"'
            ),

            '<OBJETO> ::= "medicamentos"',

            (
                '<LUGAR> ::= '
                '"en el hospital." '
                '| "dentro del hospital."'
            ),

            (
                '<RECORDATORIO> ::= '
                '"Todavia necesito los medicamentos." '
                '| "No olvides traer los medicamentos."'
            ),

            (
                '<AGRADECIMIENTO> ::= '
                '"Gracias por traer los medicamentos." '
                '| "Lo lograste. Gracias por los medicamentos."'
            ),


            # ===================================
            # MARCOS
            # ===================================

            "<DIALOGO_MARCOS_INICIO> ::= "
            "<NPC_MARCOS> <PETICION_MARCOS>",

            "<DIALOGO_MARCOS_RECORDATORIO> ::= "
            "<NPC_MARCOS> <RECORDATORIO_MARCOS>",

            "<DIALOGO_MARCOS_FINAL> ::= "
            "<NPC_MARCOS> <AGRADECIMIENTO_MARCOS>",

            '<NPC_MARCOS> ::= "Marcos:"',

            (
                '<PETICION_MARCOS> ::= '
                '"Necesito una radio para contactar a los militares." '
                '<MISION_MARCOS> '
                '| "Debemos recuperar una radio para pedir ayuda." '
                '<MISION_MARCOS>'
            ),

            "<MISION_MARCOS> ::= "
            "<ACCION_MARCOS> "
            "<OBJETO_MARCOS> "
            "<LUGAR_MARCOS>",

            (
                '<ACCION_MARCOS> ::= '
                '"Busca" | "Encuentra" | "Localiza"'
            ),

            '<OBJETO_MARCOS> ::= "la radio"',

            (
                '<LUGAR_MARCOS> ::= '
                '"en el archivo de la comisaria."'
            ),

            (
                '<RECORDATORIO_MARCOS> ::= '
                '"Todavia necesito la radio." '
                '| "Recuerda que necesitamos recuperar la radio."'
            ),

            (
                '<AGRADECIMIENTO_MARCOS> ::= '
                '"Gracias por traer la radio. '
                'Toma esta tarjeta militar." '
                '| "La radio funciona. '
                'Toma esta tarjeta militar como recompensa."'
            )
        ]


        return reglas_bnf