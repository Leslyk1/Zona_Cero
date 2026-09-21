# -----------------------------------
# CLASE INVENTARIO
# -----------------------------------

class Inventario:

    # Esta función se ejecuta cuando
    # creamos el inventario.
    def __init__(self):

        # Ahora utilizaremos un diccionario.
        #
        # El diccionario nos permitirá guardar:
        #
        # Nombre del objeto
        # Cantidad del objeto
        #
        # Ejemplo:
        #
        # {
        #     "Pistola": 1,
        #     "Balas": 12
        # }

        self.objetos = {}


    # -----------------------------------
    # AGREGAR OBJETO
    # -----------------------------------

    def agregar(
        self,
        nombre_objeto,
        cantidad=1
    ):

        # Revisamos si el objeto
        # ya existe en el inventario.
        if nombre_objeto in self.objetos:

            # Si ya existe,
            # aumentamos su cantidad.
            self.objetos[nombre_objeto] = (
                self.objetos[nombre_objeto]
                + cantidad
            )

        else:

            # Si todavía no existe,
            # lo agregamos.
            self.objetos[nombre_objeto] = cantidad


        # Indicamos que se agregó correctamente.
        return True


    # -----------------------------------
    # REVISAR SI TENEMOS UN OBJETO
    # -----------------------------------

    def tiene(
        self,
        nombre_objeto
    ):

        # Si el objeto existe...
        if nombre_objeto in self.objetos:

            # Y además tenemos al menos uno...
            if self.objetos[nombre_objeto] > 0:

                return True


        return False


    # -----------------------------------
    # OBTENER CANTIDAD
    # -----------------------------------

    def obtener_cantidad(
        self,
        nombre_objeto
    ):

        # Si existe el objeto...
        if nombre_objeto in self.objetos:

            # Devolvemos su cantidad.
            return self.objetos[nombre_objeto]


        # Si no existe,
        # devolvemos cero.
        return 0


    # -----------------------------------
    # USAR OBJETO
    # -----------------------------------

    def usar(
        self,
        nombre_objeto,
        cantidad=1
    ):

        # Revisamos que el objeto exista.
        if nombre_objeto in self.objetos:

            # Revisamos que tengamos
            # suficiente cantidad.
            if self.objetos[nombre_objeto] >= cantidad:

                # Restamos la cantidad.
                self.objetos[nombre_objeto] = (
                    self.objetos[nombre_objeto]
                    - cantidad
                )


                # Si la cantidad llega a cero...
                if self.objetos[nombre_objeto] == 0:

                    # Eliminamos el objeto.
                    del self.objetos[nombre_objeto]


                return True


        return False