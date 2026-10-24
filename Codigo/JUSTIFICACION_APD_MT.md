# JUSTIFICACIÓN DEL USO DE AUTÓMATA DE PILA
## Proyecto R - Zona Cero: Último Refugio

---

## 1. Introducción

En el videojuego **Zona Cero: Último Refugio** se utilizan diferentes conceptos estudiados en el curso de Autómatas y Lenguajes Formales.

Uno de estos conceptos es el uso de una estructura tipo **pila**, utilizada para controlar determinadas transiciones entre escenarios del juego.

En nuestro proyecto, la pila se utiliza principalmente cuando el jugador entra y sale del sótano del hospital.

La función de la pila es recordar desde qué escenario llegó el jugador para poder regresar correctamente al escenario anterior.

---

# 2. ¿Qué es un Autómata de Pila?

Un Autómata de Pila, también llamado APD, es una extensión de un autómata finito que posee una memoria adicional organizada como una pila.

La pila trabaja siguiendo el principio:

**LIFO**

que significa:

**Last In, First Out**

o en español:

**Último en entrar, primero en salir.**

Las principales operaciones utilizadas en una pila son:

- PUSH: agregar un elemento a la pila.
- POP: retirar el elemento que se encuentra en la parte superior.
- TOP: consultar el elemento que se encuentra en la parte superior.

---

# 3. Uso de la pila en Zona Cero

En nuestro videojuego, la pila se utiliza para controlar la navegación entre el:

- Hospital.
- Sótano del Hospital.

Cuando el jugador se encuentra en el Hospital y decide bajar al sótano, el juego guarda el estado anterior dentro de la pila.

El estado guardado es:

```text
HOSPITAL