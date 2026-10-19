# DIAGRAMA DEL AFN NARRATIVO
## Zona Cero: Último Refugio

Este documento representa formalmente el Autómata Finito No Determinista
utilizado para controlar los estados narrativos principales del videojuego.

---

# 1. Estado inicial

El estado inicial del autómata es:

q0 = REFUGIO

---

# 2. Conjunto de estados

Q = {

REFUGIO,

CALLE,

HOSPITAL,

SOTANO_HOSPITAL,

COMISARIA,

BASE_MILITAR,

PUNTO_EVACUACION,

FINAL_EVACUACION,

FINAL_SACRIFICIO,

FINAL_INFECTADO

}

---

# 3. Estados de aceptación

Los estados de aceptación representan los posibles finales del videojuego.

F = {

FINAL_EVACUACION,

FINAL_SACRIFICIO,

FINAL_INFECTADO

}

BASE_MILITAR no pertenece al conjunto de estados de aceptación.

---

# 4. Transiciones del AFN

## REFUGIO

REFUGIO --SALIR--> CALLE


## CALLE

CALLE --ENTRAR_REFUGIO--> REFUGIO

CALLE --ENTRAR_HOSPITAL--> HOSPITAL

CALLE --ENTRAR_COMISARIA--> COMISARIA

CALLE --ENTRAR_BASE_MILITAR--> BASE_MILITAR

CALLE --ENTRAR_PUNTO_EVACUACION--> PUNTO_EVACUACION


## Transición no determinista

Desde CALLE existe la acción:

EXPLORAR

Esta misma entrada puede conducir a dos estados distintos:

δ(CALLE, EXPLORAR) = {
    HOSPITAL,
    COMISARIA
}

Por esta razón el autómata es no determinista.

Formalmente:

CALLE --EXPLORAR--> HOSPITAL

CALLE --EXPLORAR--> COMISARIA


## HOSPITAL

HOSPITAL --SALIR_HOSPITAL--> CALLE

HOSPITAL --BAJAR_SOTANO--> SOTANO_HOSPITAL


## SOTANO_HOSPITAL

SOTANO_HOSPITAL --SUBIR_HOSPITAL--> HOSPITAL


## COMISARIA

COMISARIA --SALIR_COMISARIA--> CALLE


## BASE_MILITAR

BASE_MILITAR --SALIR_BASE_MILITAR--> CALLE


## PUNTO DE EVACUACION

PUNTO_EVACUACION --ELEGIR_EVACUACION--> FINAL_EVACUACION

PUNTO_EVACUACION --ELEGIR_SACRIFICIO--> FINAL_SACRIFICIO

PUNTO_EVACUACION --ELEGIR_INFECTADO--> FINAL_INFECTADO

PUNTO_EVACUACION --REGRESAR_CALLE--> CALLE

---

# 5. Diagrama general

```text

                              ┌───────────────┐
                              │    REFUGIO    │
                              └───────┬───────┘
                                      │
                                    SALIR
                                      │
                                      ▼
                              ┌───────────────┐
                    ┌─────────│     CALLE     │─────────┐
                    │         └───────────────┘         │
                    │                 │                 │
                    │                 │                 │
          ENTRAR_HOSPITAL     ENTRAR_COMISARIA   ENTRAR_BASE_MILITAR
                    │                 │                 │
                    ▼                 ▼                 ▼
             ┌────────────┐    ┌────────────┐    ┌──────────────┐
             │  HOSPITAL  │    │ COMISARIA  │    │ BASE_MILITAR │
             └─────┬──────┘    └─────┬──────┘    └──────┬───────┘
                   │                 │                   │
             BAJAR_SOTANO       SALIR_COMISARIA    SALIR_BASE_MILITAR
                   │                 │                   │
                   ▼                 └──────► CALLE ◄────┘
        ┌───────────────────┐
        │ SOTANO_HOSPITAL   │
        └─────────┬─────────┘
                  │
            SUBIR_HOSPITAL
                  │
                  ▼
              HOSPITAL


CALLE --ENTRAR_REFUGIO--> REFUGIO


CALLE --EXPLORAR--> HOSPITAL
       \
        └---------> COMISARIA


CALLE
  │
  │ ENTRAR_PUNTO_EVACUACION
  ▼
┌─────────────────────┐
│ PUNTO_EVACUACION    │
└─────────┬───────────┘
          │
          ├── ELEGIR_EVACUACION
          │          │
          │          ▼
          │   FINAL_EVACUACION
          │
          ├── ELEGIR_SACRIFICIO
          │          │
          │          ▼
          │   FINAL_SACRIFICIO
          │
          └── ELEGIR_INFECTADO
                     │
                     ▼
              FINAL_INFECTADO
