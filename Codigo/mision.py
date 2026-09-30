# -----------------------------------
# CLASE MISIÓN
# -----------------------------------

import pygame

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

        # Momento en el que se completó.
        # Se usa para ocultar el aviso
        # después de unos segundos.
        self.tiempo_completada = 0


    # -----------------------------------
    # ACTIVAR MISIÓN
    # -----------------------------------

    def activar(self):

        # Activamos la misión.
        self.activa = True

        self.tiempo_completada = 0


    # -----------------------------------
    # COMPLETAR MISIÓN
    # -----------------------------------

    def completar(self):

        # La misión deja de estar activa.
        self.activa = False

        # La marcamos como completada.
        self.completada = True

        # Guardamos el momento exacto para
        # mostrar el aviso temporalmente.
        self.tiempo_completada = (
            pygame.time.get_ticks()
        )


class DiarioMisiones:
    """Vista del progreso real de la partida, sin duplicar sus condiciones."""

    def __init__(self):
        self.misiones = []
        self.completadas = 0
        self.pasos_completados = 0
        self.total_pasos = 5
        self.siguiente = "Habla con Elena en el hospital."

    def actualizar(self, mision, inventario, zombi_comisaria, zombi_sotano):
        # Diego: leemos los mismos flags que usa la evacuación. El diario no
        # concede victorias ni pierde objetivos cumplidos al volver al refugio.
        entregado = mision.completada
        medicina = inventario.tiene("Medicamento") or entregado
        self.misiones = [
            {"nombre": "Medicinas perdidas", "zona": "HOSPITAL", "completa": entregado,
             "descripcion": "Elena necesita suministros para los sobrevivientes.",
             "pasos": [("Habla con Elena", mision.activa or entregado),
                       ("Recoge el medicamento en la farmacia", medicina),
                       ("Regresa con Elena para entregarlo", entregado)]},
            {"nombre": "Despejar la comisaría", "zona": "COMISARIA",
             "completa": not zombi_comisaria.vivo,
             "descripcion": "Vence al policía infectado. Después podrás recoger el arma y las balas.",
             "pasos": [("Derrota al Zombi Policía", not zombi_comisaria.vivo)]},
            {"nombre": "Amenaza en el sótano", "zona": "SOTANO DEL HOSPITAL",
             "completa": not zombi_sotano.vivo,
             "descripcion": "Baja por las escaleras del hospital y elimina al corredor.",
             "pasos": [("Derrota al Zombi Corredor", not zombi_sotano.vivo)]},
        ]
        self.completadas = sum(m["completa"] for m in self.misiones)
        self.total_pasos = sum(len(m["pasos"]) for m in self.misiones)
        self.pasos_completados = sum(hecho for m in self.misiones for _, hecho in m["pasos"])
        pendientes = [texto for m in self.misiones for texto, hecho in m["pasos"] if not hecho]
        self.siguiente = pendientes[0] if pendientes else "Ve al punto de evacuación en la calle."

    @property
    def porcentaje(self):
        return round(100 * self.pasos_completados / self.total_pasos)
