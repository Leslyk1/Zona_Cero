import pygame


# ===================================
# CLASE MISIÓN
# ===================================

class Mision:

    def __init__(
        self,
        nombre,
        descripcion
    ):

        self.nombre = nombre

        self.descripcion = descripcion

        self.activa = False

        self.completada = False

        self.tiempo_completada = 0


    # ===================================
    # ACTIVAR MISIÓN
    # ===================================

    def activar(self):

        self.activa = True

        self.tiempo_completada = 0


    # ===================================
    # COMPLETAR MISIÓN
    # ===================================

    def completar(self):

        self.activa = False

        self.completada = True

        self.tiempo_completada = (
            pygame.time.get_ticks()
        )


# ===================================
# DIARIO DE MISIONES
# ===================================

class DiarioMisiones:

    def __init__(self):

        self.misiones = []

        self.completadas = 0

        self.pasos_completados = 0

        self.total_pasos = 8

        self.siguiente = (
            "Habla con Elena en el hospital."
        )


    def actualizar(
        self,
        mision,
        mision_radio,
        inventario,
        zombi_comisaria,
        zombi_sotano
    ):

        # ===================================
        # MISIÓN DE ELENA
        # ===================================

        entregado = (
            mision.completada
        )

        medicina = (
            inventario.tiene(
                "Medicamento"
            )
            or
            entregado
        )


        # ===================================
        # MISIÓN DE MARCOS
        # ===================================

        radio_entregada = (
            mision_radio.completada
        )

        radio_encontrada = (
            inventario.tiene(
                "Radio"
            )
            or
            radio_entregada
        )

        hablo_marcos = (
            mision_radio.activa
            or
            mision_radio.completada
        )


        # ===================================
        # LISTA DE MISIONES
        # ===================================

        self.misiones = [

            {
                "nombre":
                    "Medicinas perdidas",

                "zona":
                    "HOSPITAL",

                "completa":
                    entregado,

                "descripcion":
                    "Elena necesita suministros para los sobrevivientes.",

                "pasos": [

                    (
                        "Habla con Elena",
                        mision.activa
                        or
                        entregado
                    ),

                    (
                        "Recoge el medicamento en la farmacia",
                        medicina
                    ),

                    (
                        "Regresa con Elena para entregarlo",
                        entregado
                    )
                ]
            },


            {
                "nombre":
                    "Despejar la comisaría",

                "zona":
                    "COMISARIA",

                "completa":
                    not zombi_comisaria.vivo,

                "descripcion":
                    "Vence al policía infectado. Después podrás recoger el arma y las balas.",

                "pasos": [

                    (
                        "Derrota al Zombi Policía",
                        not zombi_comisaria.vivo
                    )
                ]
            },


            {
                "nombre":
                    "Amenaza en el sótano",

                "zona":
                    "SOTANO DEL HOSPITAL",

                "completa":
                    not zombi_sotano.vivo,

                "descripcion":
                    "Baja por las escaleras del hospital y elimina al corredor.",

                "pasos": [

                    (
                        "Derrota al Zombi Corredor",
                        not zombi_sotano.vivo
                    )
                ]
            },


            {
                "nombre":
                    "Señal perdida",

                "zona":
                    "COMISARIA",

                "completa":
                    radio_entregada,

                "descripcion":
                    "Marcos necesita una radio para intentar contactar a los militares.",

                "pasos": [

                    (
                        "Habla con Marcos",
                        hablo_marcos
                    ),

                    (
                        "Encuentra la radio en el archivo",
                        radio_encontrada
                    ),

                    (
                        "Regresa con Marcos",
                        radio_entregada
                    )
                ]
            }
        ]


        self.completadas = sum(
            m["completa"]
            for m in self.misiones
        )


        self.total_pasos = sum(
            len(m["pasos"])
            for m in self.misiones
        )


        self.pasos_completados = sum(
            hecho
            for m in self.misiones
            for _, hecho in m["pasos"]
        )


        pendientes = [

            texto

            for m in self.misiones

            for texto, hecho
            in m["pasos"]

            if not hecho
        ]


        if pendientes:

            self.siguiente = (
                pendientes[0]
            )

        else:

            self.siguiente = (
                "Ve al punto de evacuación en la calle."
            )


    @property
    def porcentaje(self):

        if self.total_pasos == 0:

            return 0

        return round(
            100
            *
            self.pasos_completados
            /
            self.total_pasos
        )