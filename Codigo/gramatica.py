# ===================================
# GRAMÁTICA LIBRE DE CONTEXTO
# PARA DIÁLOGOS Y MISIONES
# ===================================

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
                ]
            ],

            "<OBJETO>": [
                [
                    "medicamentos"
                ]
            ],

            "<LUGAR>": [
                [
                    "en la farmacia."
                ],
                [
                    "en el sotano."
                ]
            ],

            "<RECORDATORIO>": [
                [
                    "Todavia necesito los medicamentos."
                ]
            ],

            "<AGRADECIMIENTO>": [
                [
                    "Gracias por traer los medicamentos."
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
                ]
            ],

            "<AGRADECIMIENTO_MARCOS>": [
                [
                    "Gracias por traer la radio. Toma esta tarjeta militar."
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

        # Si no está en las reglas,
        # significa que es terminal.
        if simbolo not in self.reglas:

            return simbolo


        # Elegimos la primera producción.
        produccion = self.reglas[
            simbolo
        ][0]


        resultado = []


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

            for posicion in range(
                len(actual)
            ):

                simbolo = actual[
                    posicion
                ]


                if simbolo in self.reglas:

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

                    break


        return pasos


    # ===================================
    # OBTENER BNF
    # ===================================

    def obtener_bnf(self):

        reglas_bnf = [

            # Elena.
            "<DIALOGO_INICIO> ::= <NPC> <PETICION>",

            "<DIALOGO_RECORDATORIO> ::= <NPC> <RECORDATORIO>",

            "<DIALOGO_FINAL> ::= <NPC> <AGRADECIMIENTO>",

            '<NPC> ::= "Elena:"',

            '<PETICION> ::= "Necesito tu ayuda." <MISION>',

            "<MISION> ::= <ACCION> <OBJETO> <LUGAR>",

            '<ACCION> ::= "Busca" | "Encuentra"',

            '<OBJETO> ::= "medicamentos"',

            '<LUGAR> ::= "en la farmacia." | "en el sotano."',

            '<RECORDATORIO> ::= "Todavia necesito los medicamentos."',

            '<AGRADECIMIENTO> ::= "Gracias por traer los medicamentos."',


            # Marcos.
            "<DIALOGO_MARCOS_INICIO> ::= <NPC_MARCOS> <PETICION_MARCOS>",

            "<DIALOGO_MARCOS_RECORDATORIO> ::= <NPC_MARCOS> <RECORDATORIO_MARCOS>",

            "<DIALOGO_MARCOS_FINAL> ::= <NPC_MARCOS> <AGRADECIMIENTO_MARCOS>",

            '<NPC_MARCOS> ::= "Marcos:"',

            '<PETICION_MARCOS> ::= "Necesito una radio para contactar a los militares." <MISION_MARCOS>',

            "<MISION_MARCOS> ::= <ACCION_MARCOS> <OBJETO_MARCOS> <LUGAR_MARCOS>",

            '<ACCION_MARCOS> ::= "Busca" | "Encuentra"',

            '<OBJETO_MARCOS> ::= "la radio"',

            '<LUGAR_MARCOS> ::= "en el archivo de la comisaria."',

            '<RECORDATORIO_MARCOS> ::= "Todavia necesito la radio."',

            '<AGRADECIMIENTO_MARCOS> ::= "Gracias por traer la radio. Toma esta tarjeta militar."'
        ]


        return reglas_bnf