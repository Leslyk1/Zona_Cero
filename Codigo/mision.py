# -----------------------------------
# CLASE MISIÓN
# -----------------------------------

class Mision:

    # Esta función se ejecuta cuando
    # creamos una nueva misión.
    def __init__(self, nombre, descripcion):

        # Nombre de la misión.
        self.nombre = nombre

        # Descripción de la misión.
        self.descripcion = descripcion

        # Al principio la misión
        # todavía no está activa.
        self.activa = False

        # Al principio tampoco
        # está completada.
        self.completada = False


    # -----------------------------------
    # ACTIVAR MISIÓN
    # -----------------------------------

    def activar(self):

        # Activamos la misión.
        self.activa = True


    # -----------------------------------
    # COMPLETAR MISIÓN
    # -----------------------------------

    def completar(self):

        # La misión deja de estar activa.
        self.activa = False

        # La marcamos como completada.
        self.completada = True