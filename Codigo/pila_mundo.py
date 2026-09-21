# -----------------------------------
# PILA DEL MUNDO
# -----------------------------------

class PilaMundo:

    # Esta función se ejecuta
    # cuando creamos la pila.
    def __init__(self):

        # Lista que funcionará
        # como nuestra pila.
        self.elementos = []


        # Guardamos la última operación
        # realizada sobre la pila.
        #
        # Al comenzar todavía
        # no hemos hecho ninguna.
        self.ultima_operacion = "NINGUNA"


    # -----------------------------------
    # APILAR
    # -----------------------------------

    def apilar(self, lugar):

        # Agregamos el lugar
        # en la parte superior
        # de la pila.
        self.elementos.append(
            lugar
        )


        # Guardamos qué operación
        # acabamos de realizar.
        self.ultima_operacion = (
            "PUSH " + lugar
        )


        # También mostramos
        # información en la terminal.
        print(
            "Operacion:",
            self.ultima_operacion
        )


        print(
            "Pila actual:",
            self.elementos
        )


    # -----------------------------------
    # DESAPILAR
    # -----------------------------------

    def desapilar(self):

        # Revisamos que la pila
        # tenga algún elemento.
        if len(self.elementos) > 0:

            # Sacamos el elemento
            # que se encuentra arriba.
            lugar = self.elementos.pop()


            # Guardamos la operación.
            self.ultima_operacion = (
                "POP " + lugar
            )


            # Mostramos información
            # en la terminal.
            print(
                "Operacion:",
                self.ultima_operacion
            )


            print(
                "Pila actual:",
                self.elementos
            )


            # Devolvemos el lugar
            # que acabamos de sacar.
            return lugar


        # Si intentamos sacar algo
        # pero la pila está vacía.
        self.ultima_operacion = (
            "POP FALLIDO"
        )


        return None


    # -----------------------------------
    # VER EL TOPE
    # -----------------------------------

    def ver_tope(self):

        # Si existen elementos...
        if len(self.elementos) > 0:

            # Regresamos el último.
            return self.elementos[-1]


        return None


    # -----------------------------------
    # VACIAR PILA
    # -----------------------------------

    def vaciar(self):

        # Dejamos la pila vacía.
        self.elementos = []


        # Guardamos la operación.
        self.ultima_operacion = (
            "VACIAR PILA"
        )


        print(
            "Operacion:",
            self.ultima_operacion
        )


        print(
            "Pila actual:",
            self.elementos
        )