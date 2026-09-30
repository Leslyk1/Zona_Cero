# ==========================================
# PRUEBAS DE ALCANZABILIDAD
# ZONA CERO: ULTIMO REFUGIO
# ==========================================

# Importamos nuestro automata narrativo
from automata import AutomataNarrativo


# ==========================================
# PROBAR NO DETERMINISMO
# ==========================================

def probar_no_determinismo(
    automata
):

    destinos = (
        automata.transiciones
        .get("CALLE", {})
        .get("EXPLORAR", [])
    )


    print()
    print(
        "=========================================="
    )
    print(
        "PRUEBA DE NO DETERMINISMO"
    )
    print(
        "=========================================="
    )
    print()
    print(
        "delta(CALLE, EXPLORAR) =",
        destinos
    )


    destinos_esperados = {
        "HOSPITAL",
        "COMISARIA"
    }


    if (
        len(destinos) > 1
        and
        set(destinos) == destinos_esperados
    ):

        print(
            "RESULTADO: TRANSICION NO DETERMINISTA VALIDA"
        )


        # Ejecutamos EXPLORAR y comprobamos
        # que el historial guarde la acción,
        # el origen y todos los destinos.
        automata.estado_actual = "CALLE"

        automata.cambiar_estado(
            "EXPLORAR"
        )


        assert automata.estado_anterior == "CALLE"

        assert automata.ultima_accion == "EXPLORAR"

        assert set(
            automata.ultimos_posibles
        ) == destinos_esperados


        print(
            "RESULTADO: HISTORIAL DE TRANSICION VALIDO"
        )

    else:

        raise AssertionError(
            "EXPLORAR debe tener HOSPITAL y COMISARIA "
            "como destinos posibles."
        )


# ==========================================
# BUSCAR RUTA MINIMA
# ==========================================

def buscar_ruta_minima(
    automata,
    estado_inicial,
    estado_final
):

    # ------------------------------------------
    # COLA DE BUSQUEDA
    # ------------------------------------------
    #
    # Cada elemento contiene:
    #
    # 1. Estado actual
    # 2. Estados recorridos
    # 3. Acciones realizadas

    cola = [

        (
            estado_inicial,
            [estado_inicial],
            []
        )

    ]


    # Aquí guardaremos los estados
    # que ya fueron revisados.
    visitados = []


    # ==========================================
    # RECORRER EL AUTOMATA
    # ==========================================

    while len(cola) > 0:


        # Sacamos el primer elemento
        # de la cola.
        datos = cola.pop(0)


        estado_actual = datos[0]

        ruta_estados = datos[1]

        ruta_acciones = datos[2]


        # ------------------------------------------
        # ¿LLEGAMOS AL FINAL?
        # ------------------------------------------

        if estado_actual == estado_final:

            return (
                ruta_estados,
                ruta_acciones
            )


        # ------------------------------------------
        # MARCAR COMO VISITADO
        # ------------------------------------------

        if estado_actual not in visitados:

            visitados.append(
                estado_actual
            )


            # Obtenemos las transiciones
            # disponibles desde ese estado.
            transiciones = (
                automata.transiciones.get(
                    estado_actual,
                    {}
                )
            )


            # ------------------------------------------
            # REVISAR CADA ACCION
            # ------------------------------------------

            for accion in transiciones:


                estados_siguientes = (
                    transiciones[
                        accion
                    ]
                )


                # Puede existir más de un
                # estado siguiente.
                for siguiente in estados_siguientes:


                    # Evitamos repetir estados
                    # que ya revisamos.
                    if siguiente not in visitados:


                        # Creamos una nueva ruta.
                        nuevos_estados = (
                            ruta_estados
                            +
                            [siguiente]
                        )


                        nuevas_acciones = (
                            ruta_acciones
                            +
                            [accion]
                        )


                        # La agregamos a la cola.
                        cola.append(

                            (
                                siguiente,
                                nuevos_estados,
                                nuevas_acciones
                            )

                        )


    # Si terminamos la búsqueda
    # y no encontramos el final.
    return (
        None,
        None
    )


# ==========================================
# MOSTRAR UNA PRUEBA
# ==========================================

def mostrar_prueba(
    automata,
    estado_final
):

    print()
    print(
        "=========================================="
    )

    print(
        "PRUEBA DE ALCANZABILIDAD"
    )

    print(
        "Estado final:",
        estado_final
    )

    print(
        "=========================================="
    )


    # Buscamos la ruta mínima
    ruta_estados, ruta_acciones = (
        buscar_ruta_minima(

            automata,

            "REFUGIO",

            estado_final

        )
    )


    # ==========================================
    # SI EXISTE UNA RUTA
    # ==========================================

    if ruta_estados is not None:


        print()
        print(
            "RESULTADO: ALCANZABLE"
        )


        print()
        print(
            "Estado inicial:"
        )

        print(
            "REFUGIO"
        )


        print()
        print(
            "Secuencia minima:"
        )


        # ------------------------------------------
        # MOSTRAR LAS TRANSICIONES
        # ------------------------------------------

        for posicion in range(
            len(ruta_acciones)
        ):


            estado_actual = (
                ruta_estados[
                    posicion
                ]
            )


            accion = (
                ruta_acciones[
                    posicion
                ]
            )


            siguiente_estado = (
                ruta_estados[
                    posicion + 1
                ]
            )


            print(
                estado_actual
                + " --"
                + accion
                + "--> "
                + siguiente_estado
            )


        print()


        # ------------------------------------------
        # CANTIDAD DE TRANSICIONES
        # ------------------------------------------

        print(
            "Numero minimo de transiciones:",
            len(ruta_acciones)
        )


        # ------------------------------------------
        # ESTADO DE ACEPTACION
        # ------------------------------------------

        if (
            estado_final
            in
            automata.estados_aceptacion
        ):

            print(
                "El estado pertenece al conjunto "
                "de estados de aceptacion."
            )

        else:

            print(
                "El estado NO pertenece al conjunto "
                "de aceptacion."
            )


    # ==========================================
    # SI NO EXISTE RUTA
    # ==========================================

    else:

        print()
        print(
            "RESULTADO: NO ALCANZABLE"
        )


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

# Creamos nuestro automata.
automata = AutomataNarrativo()


# Comprobamos que una misma entrada tenga
# más de un estado siguiente posible.
probar_no_determinismo(
    automata
)


print()
print(
    "=========================================="
)

print(
    " ZONA CERO: ULTIMO REFUGIO"
)

print(
    " PRUEBAS FORMALES DE ALCANZABILIDAD"
)

print(
    "=========================================="
)


# ==========================================
# CONJUNTO DE ESTADOS DE ACEPTACION
# ==========================================

print()
print(
    "Estados de aceptacion:"
)


for estado in automata.estados_aceptacion:

    print(
        "-",
        estado
    )


# ==========================================
# FINAL EVACUACION
# ==========================================

mostrar_prueba(
    automata,
    "FINAL_EVACUACION"
)


# ==========================================
# FINAL SACRIFICIO
# ==========================================

mostrar_prueba(
    automata,
    "FINAL_SACRIFICIO"
)


# ==========================================
# FINAL INFECTADO
# ==========================================

mostrar_prueba(
    automata,
    "FINAL_INFECTADO"
)


# ==========================================
# REQUISITOS DEL JUEGO
# ==========================================

print()
print(
    "=========================================="
)

print(
    "CONDICIONES DEL MUNDO PARA DESBLOQUEAR"
)

print(
    "EL PUNTO DE EVACUACION"
)

print(
    "=========================================="
)

print()

print(
    "1. Completar la mision de Elena."
)

print(
    "2. Derrotar al Zombi Policia."
)

print(
    "3. Derrotar al Zombi Corredor."
)

print()

print(
    "Estas condiciones pertenecen al estado "
    "del mundo del juego."
)

print(
    "Una vez cumplidas, el AFN permite acceder "
    "al PUNTO_EVACUACION."
)

print()
