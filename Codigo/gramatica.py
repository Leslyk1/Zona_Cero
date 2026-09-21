# -----------------------------------
# GRAMÁTICA LIBRE DE CONTEXTO
# PARA DIÁLOGOS Y MISIONES
# -----------------------------------

class GramaticaDialogos:

    def __init__(self):

        # -----------------------------------
        # REGLAS DE PRODUCCIÓN
        # -----------------------------------
        #
        # Cada elemento representa
        # una regla de nuestra GLC.
        #
        # Ejemplo:
        #
        # <MISION> ->
        # <ACCION> <OBJETO> <LUGAR>
        #
        # Utilizamos listas porque
        # algunos símbolos pueden tener
        # varias producciones posibles.

        self.reglas = {


            # ===================================
            # DIÁLOGO INICIAL
            # ===================================

            "<DIALOGO_INICIO>": [

                [
                    "<NPC>",
                    "<PETICION>"
                ]
            ],


            # ===================================
            # DIÁLOGO DE RECORDATORIO
            # ===================================

            "<DIALOGO_RECORDATORIO>": [

                [
                    "<NPC>",
                    "<RECORDATORIO>"
                ]
            ],


            # ===================================
            # DIÁLOGO FINAL
            # ===================================

            "<DIALOGO_FINAL>": [

                [
                    "<NPC>",
                    "<AGRADECIMIENTO>"
                ]
            ],


            # ===================================
            # NPC
            # ===================================

            "<NPC>": [

                [
                    "Elena:"
                ]
            ],


            # ===================================
            # PETICIÓN
            # ===================================

            "<PETICION>": [

                [
                    "Necesito tu ayuda.",
                    "<MISION>"
                ]
            ],


            # ===================================
            # MISIÓN
            # ===================================

            "<MISION>": [

                [
                    "<ACCION>",
                    "<OBJETO>",
                    "<LUGAR>"
                ]
            ],


            # ===================================
            # ACCIONES POSIBLES
            # ===================================

            "<ACCION>": [

                [
                    "Busca"
                ],

                [
                    "Encuentra"
                ]
            ],


            # ===================================
            # OBJETOS
            # ===================================

            "<OBJETO>": [

                [
                    "medicamentos"
                ]
            ],


            # ===================================
            # LUGARES
            # ===================================

            "<LUGAR>": [

                [
                    "en la farmacia."
                ],

                [
                    "en el sotano."
                ]
            ],


            # ===================================
            # RECORDATORIO
            # ===================================

            "<RECORDATORIO>": [

                [
                    "Todavia necesito los medicamentos."
                ]
            ],


            # ===================================
            # AGRADECIMIENTO
            # ===================================

            "<AGRADECIMIENTO>": [

                [
                    "Gracias por traer los medicamentos."
                ]
            ]
        }


    # ===================================
    # GENERAR UNA CADENA
    # ===================================

    def generar(self, simbolo):

        # Si el símbolo NO pertenece
        # a las reglas, significa que
        # ya es un terminal.
        if simbolo not in self.reglas:

            return simbolo


        # Por ahora utilizaremos
        # la primera producción.
        #
        # Ejemplo:
        #
        # <ACCION> tiene:
        #
        # Busca
        # Encuentra
        #
        # Nosotros usaremos "Busca".
        produccion = self.reglas[
            simbolo
        ][0]


        # Aquí guardaremos las
        # palabras generadas.
        resultado = []


        # Recorremos la producción.
        for parte in produccion:

            # Generamos cada parte.
            texto = self.generar(
                parte
            )


            # La agregamos.
            resultado.append(
                texto
            )


        # Unimos todo utilizando espacios.
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

        # Comenzamos solamente
        # con el símbolo inicial.
        actual = [
            simbolo_inicial
        ]


        # Aquí guardaremos todos
        # los pasos realizados.
        pasos = []


        # Guardamos el primer paso.
        pasos.append(
            " ".join(actual)
        )


        # Seguimos mientras existan
        # símbolos no terminales.
        continuar = True


        while continuar:

            continuar = False


            # Recorremos la cadena.
            for posicion in range(
                len(actual)
            ):

                simbolo = actual[
                    posicion
                ]


                # Si pertenece a las reglas,
                # es un no terminal.
                if simbolo in self.reglas:

                    # Elegimos la primera
                    # producción.
                    produccion = (
                        self.reglas[
                            simbolo
                        ][0]
                    )


                    # Reemplazamos el símbolo
                    # por su producción.
                    actual = (
                        actual[:posicion]
                        +
                        produccion
                        +
                        actual[posicion + 1:]
                    )


                    # Guardamos el nuevo paso.
                    pasos.append(
                        " ".join(actual)
                    )


                    continuar = True


                    # Solo reemplazamos
                    # un símbolo por vuelta.
                    #
                    # Esto produce una
                    # derivación por la izquierda.
                    break


        return pasos


    # ===================================
    # OBTENER BNF
    # ===================================

    def obtener_bnf(self):

        # Estas son las reglas escritas
        # formalmente utilizando BNF.
        reglas_bnf = [

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

            '<AGRADECIMIENTO> ::= "Gracias por traer los medicamentos."'
        ]


        return reglas_bnf