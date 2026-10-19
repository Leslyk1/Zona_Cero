# AUTÓMATA DE COMBATE
## Zona Cero: Último Refugio

El videojuego utiliza un autómata independiente para controlar
el sistema de combate por turnos.

Este autómata es diferente al AFN narrativo.

El AFN narrativo controla los escenarios del videojuego, mientras
que el autómata de combate controla únicamente las fases de una batalla.

---

# 1. Estados del autómata de combate

Los estados utilizados en `combate.py` son:

Q = {

SIN_COMBATE,

ELEGIR_ACCION,

ATACANDO,

DISPARANDO,

DEFENDIENDO,

TURNO_ENEMIGO,

VICTORIA,

DERROTA

}

---

# 2. Estado inicial

Cuando no existe una batalla activa:

SIN_COMBATE

Cuando comienza una batalla se realiza:

SIN_COMBATE
      |
      | INICIAR_COMBATE
      v
ELEGIR_ACCION

En el código se registra:

INICIO -> ELEGIR_ACCION

---

# 3. Elección de acción

Desde:

ELEGIR_ACCION

el jugador puede seleccionar una de tres acciones:

1. GOLPEAR
2. DISPARAR
3. DEFENDER

El flujo general es:

                 ELEGIR_ACCION
                 /      |      \
                /       |       \
          GOLPEAR   DISPARAR   DEFENDER
              |         |          |
              v         v          v
         ATACANDO  DISPARANDO  DEFENDIENDO

---

# 4. Acción GOLPEAR

Cuando el jugador selecciona GOLPEAR, el sistema genera:

random.randint(1, 100)

Esto produce un número entre 1 y 100.

Las probabilidades son:

- 20 % CRITICO
- 65 % GOLPE_NORMAL
- 15 % FALLO

Formalmente:

Si numero <= 20:

CRITICO

Daño:

20

Si:

20 < numero <= 85

se produce:

GOLPE_NORMAL

Daño:

10

Si:

numero > 85

se produce:

FALLO

Daño:

0

Representación:

ELEGIR_ACCION
      |
      | GOLPEAR
      v
   ATACANDO
    /  |  \
   /   |   \
20%   65%   15%
 |     |      |
 v     v      v
CRITICO GOLPE_NORMAL FALLO

---

# 5. Acción DISPARAR

Para disparar se requieren dos elementos del inventario:

Pistola

y:

Balas

Si el jugador no posee Pistola, el disparo no se realiza.

Si no tiene Balas, tampoco se realiza.

En ninguno de esos dos casos se consume el turno.

Si existen ambos recursos:

inventario.usar("Balas", 1)

consume una bala.

Después se genera:

random.randint(1, 100)

Las probabilidades del disparo son:

- 30 % CRITICO
- 60 % IMPACTO
- 10 % FALLO

## CRITICO

Si:

numero <= 30

Daño:

30

## IMPACTO

Si:

30 < numero <= 90

Daño:

20

## FALLO

Si:

numero > 90

Daño:

0

Incluso cuando el disparo falla, la bala ya fue consumida.

Representación:

ELEGIR_ACCION
      |
      | DISPARAR
      v
  DISPARANDO
    /   |   \
   /    |    \
30%    60%   10%
 |      |      |
 v      v      v
CRITICO IMPACTO FALLO

---

# 6. Acción DEFENDER

La acción DEFENDER no utiliza una probabilidad propia.

Cuando el jugador selecciona esta opción:

ELEGIR_ACCION
      |
      | DEFENDER
      v
 DEFENDIENDO

El resultado se registra como:

GUARDIA

Después continúa el turno del enemigo.

Si el enemigo logra golpear mientras el jugador está defendiendo,
el daño se reduce a la mitad.

En el código:

dano = enemigo.danio // 2

---

# 7. Turno enemigo

Después de una acción del jugador, si el enemigo continúa vivo,
el sistema cambia a:

TURNO_ENEMIGO

El enemigo también utiliza una transición probabilística.

Se genera:

random.randint(1, 100)

Las probabilidades son:

- 30 % ESQUIVE
- 70 % ATAQUE DEL ENEMIGO

---

# 8. Esquive

Si:

numero <= 30

el resultado es:

ESQUIVE

Daño recibido:

0

Representación:

TURNO_ENEMIGO
      |
      | 30 %
      v
   ESQUIVE

---

# 9. Golpe del enemigo

Si:

numero > 30

el enemigo logra atacar.

Probabilidad:

70 %

Si el jugador no estaba defendiendo:

resultado = GOLPE_ENEMIGO

y recibe:

enemigo.danio

Si el jugador había utilizado DEFENDER:

resultado = BLOQUEO

y recibe:

enemigo.danio // 2

Representación:

                   TURNO_ENEMIGO
                    /          \
                  30%          70%
                   |            |
                   v            v
               ESQUIVE        ATAQUE
                               /   \
                              /     \
                    DEFENDER         NORMAL
                       |               |
                       v               v
                    BLOQUEO      GOLPE_ENEMIGO

# 10. Victoria

Después de que termina la animación de:

ATACANDO

DISPARANDO

o:

DEFENDIENDO

el sistema verifica si el enemigo continúa vivo.

Si:

enemigo.vivo == False

el estado cambia a:

VICTORIA

Flujo:

ATACANDO / DISPARANDO
          |
          | vida enemigo <= 0
          v
       VICTORIA

En este caso el enemigo ya no obtiene turno.

---

# 11. Derrota

Después del turno enemigo se verifica la vida del jugador.

Si:

jugador.esta_vivo() == False

el estado se convierte en:

DERROTA

Representación:

TURNO_ENEMIGO
      |
      | vida jugador <= 0
      v
    DERROTA

Después de aceptar la derrota, el videojuego:

- reinicia al enemigo;
- recupera la vida del jugador;
- regresa al jugador al REFUGIO;
- vacía la pila del mundo;
- termina el combate.

---

# 12. Continuación de la batalla

Si después del turno enemigo el jugador continúa vivo:

TURNO_ENEMIGO
      |
      | jugador vivo
      v
ELEGIR_ACCION

También aumenta el número de turno:

turno += 1

Por lo tanto, el ciclo principal del combate es:

ELEGIR_ACCION
      |
      v
ACCION DEL JUGADOR
      |
      v
TURNO_ENEMIGO
      |
      v
ELEGIR_ACCION

Este ciclo continúa hasta llegar a:

VICTORIA

o:

DERROTA

---

# 13. Diagrama general

```text

                      ┌────────────────┐
                      │  SIN_COMBATE   │
                      └───────┬────────┘
                              │
                       iniciar combate
                              │
                              ▼
                     ┌──────────────────┐
                     │ ELEGIR_ACCION    │
                     └────┬─────┬───────┘
                          │     │
              ┌───────────┘     └────────────┐
              │                              │
           GOLPEAR                       DISPARAR
              │                              │
              ▼                              ▼
        ┌───────────┐                 ┌────────────┐
        │ ATACANDO  │                 │ DISPARANDO │
        └─────┬─────┘                 └─────┬──────┘
              │                              │
      ┌───────┼───────┐              ┌───────┼───────┐
      │       │       │              │       │       │
     20%     65%     15%            30%     60%     10%
      │       │       │              │       │       │
      ▼       ▼       ▼              ▼       ▼       ▼
   CRITICO NORMAL   FALLO         CRITICO IMPACTO  FALLO
      │       │       │              │       │       │
      └───────┴───────┘              └───────┴───────┘
              │                              │
              └──────────────┬───────────────┘
                             │
                     enemigo sigue vivo
                             │
                             ▼
                    ┌────────────────┐
                    │ TURNO_ENEMIGO  │
                    └───────┬────────┘
                            │
                     ┌──────┴──────┐
                     │             │
                    30%           70%
                     │             │
                     ▼             ▼
                  ESQUIVE        ATAQUE
                     │             │
                     │      ┌──────┴──────┐
                     │      │             │
                     │  defendiendo      normal
                     │      │             │
                     │      ▼             ▼
                     │   BLOQUEO    GOLPE_ENEMIGO
                     │      │             │
                     └──────┴──────┬──────┘
                                   │
                             jugador vivo
                                   │
                                   ▼
                            ELEGIR_ACCION