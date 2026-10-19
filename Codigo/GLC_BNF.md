# GRAMÁTICA LIBRE DE CONTEXTO
## Zona Cero: Último Refugio

La Gramática Libre de Contexto del videojuego se utiliza para generar
diálogos y textos de misiones de los NPC.

Actualmente existen reglas para:

- Elena, ubicada en el Hospital.
- Marcos, ubicado en la Comisaría.

La gramática está implementada en `gramatica.py`.

---

# 1. Definición formal

Una Gramática Libre de Contexto puede representarse mediante:

G = (V, Σ, P, S)

donde:

- V = conjunto de símbolos no terminales.
- Σ = conjunto de símbolos terminales.
- P = conjunto de producciones.
- S = símbolo inicial.

Las reglas son libres de contexto porque el lado izquierdo de cada
producción contiene un único símbolo no terminal.

Ejemplo:

<MISION> ::= <ACCION> <OBJETO> <LUGAR>

---

# 2. Gramática de Elena

## Símbolos no terminales

V Elena = {

<DIALOGO_INICIO>,

<DIALOGO_RECORDATORIO>,

<DIALOGO_FINAL>,

<NPC>,

<PETICION>,

<MISION>,

<ACCION>,

<OBJETO>,

<LUGAR>,

<RECORDATORIO>,

<AGRADECIMIENTO>

}

## Símbolos terminales

Σ Elena = {

"Elena:",

"Necesito tu ayuda.",

"Busca",

"Encuentra",

"medicamentos",

"en la farmacia.",

"en el sotano.",

"Todavia necesito los medicamentos.",

"Gracias por traer los medicamentos."

}

---

# 3. Producciones BNF de Elena

<DIALOGO_INICIO> ::= <NPC> <PETICION>

<DIALOGO_RECORDATORIO> ::= <NPC> <RECORDATORIO>

<DIALOGO_FINAL> ::= <NPC> <AGRADECIMIENTO>

<NPC> ::= "Elena:"

<PETICION> ::= "Necesito tu ayuda." <MISION>

<MISION> ::= <ACCION> <OBJETO> <LUGAR>

<ACCION> ::= "Busca" | "Encuentra"

<OBJETO> ::= "medicamentos"

<LUGAR> ::= "en la farmacia." | "en el sotano."

<RECORDATORIO> ::= "Todavia necesito los medicamentos."

<AGRADECIMIENTO> ::= "Gracias por traer los medicamentos."

---

# 4. Derivación por la izquierda de la misión de Elena

Símbolo inicial:

<MISION>

Primera producción:

<MISION>

=> <ACCION> <OBJETO> <LUGAR>

Se sustituye primero el no terminal situado más a la izquierda:

=> "Busca" <OBJETO> <LUGAR>

Después se sustituye <OBJETO>:

=> "Busca" "medicamentos" <LUGAR>

Finalmente se sustituye <LUGAR>:

=> "Busca" "medicamentos" "en la farmacia."

Cadena final:

Busca medicamentos en la farmacia.

Esta es una cadena válida perteneciente al lenguaje generado por
la gramática.

---

# 5. Derivación completa del diálogo inicial de Elena

<DIALOGO_INICIO>

=> <NPC> <PETICION>

=> "Elena:" <PETICION>

=> "Elena:" "Necesito tu ayuda." <MISION>

=> "Elena:" "Necesito tu ayuda."
   <ACCION> <OBJETO> <LUGAR>

=> "Elena:" "Necesito tu ayuda."
   "Busca" <OBJETO> <LUGAR>

=> "Elena:" "Necesito tu ayuda."
   "Busca" "medicamentos" <LUGAR>

=> "Elena:" "Necesito tu ayuda."
   "Busca" "medicamentos" "en la farmacia."

Cadena final:

Elena: Necesito tu ayuda. Busca medicamentos en la farmacia.

---

# 6. Gramática de Marcos

## Símbolos no terminales

V Marcos = {

<DIALOGO_MARCOS_INICIO>,

<DIALOGO_MARCOS_RECORDATORIO>,

<DIALOGO_MARCOS_FINAL>,

<NPC_MARCOS>,

<PETICION_MARCOS>,

<MISION_MARCOS>,

<ACCION_MARCOS>,

<OBJETO_MARCOS>,

<LUGAR_MARCOS>,

<RECORDATORIO_MARCOS>,

<AGRADECIMIENTO_MARCOS>

}

## Símbolos terminales

Σ Marcos = {

"Marcos:",

"Necesito una radio para contactar a los militares.",

"Busca",

"Encuentra",

"la radio",

"en el archivo de la comisaria.",

"Todavia necesito la radio.",

"Gracias por traer la radio. Toma esta tarjeta militar."

}

---

# 7. Producciones BNF de Marcos

<DIALOGO_MARCOS_INICIO> ::=
<NPC_MARCOS> <PETICION_MARCOS>

<DIALOGO_MARCOS_RECORDATORIO> ::=
<NPC_MARCOS> <RECORDATORIO_MARCOS>

<DIALOGO_MARCOS_FINAL> ::=
<NPC_MARCOS> <AGRADECIMIENTO_MARCOS>

<NPC_MARCOS> ::= "Marcos:"

<PETICION_MARCOS> ::=
"Necesito una radio para contactar a los militares."
<MISION_MARCOS>

<MISION_MARCOS> ::=
<ACCION_MARCOS> <OBJETO_MARCOS> <LUGAR_MARCOS>

<ACCION_MARCOS> ::= "Busca" | "Encuentra"

<OBJETO_MARCOS> ::= "la radio"

<LUGAR_MARCOS> ::= "en el archivo de la comisaria."

<RECORDATORIO_MARCOS> ::= "Todavia necesito la radio."

<AGRADECIMIENTO_MARCOS> ::=
"Gracias por traer la radio. Toma esta tarjeta militar."

---

# 8. Derivación por la izquierda de la misión de Marcos

<MISION_MARCOS>

=> <ACCION_MARCOS>
   <OBJETO_MARCOS>
   <LUGAR_MARCOS>

Se sustituye el símbolo no terminal situado más a la izquierda:

=> "Busca"
   <OBJETO_MARCOS>
   <LUGAR_MARCOS>

Después:

=> "Busca"
   "la radio"
   <LUGAR_MARCOS>

Finalmente:

=> "Busca"
   "la radio"
   "en el archivo de la comisaria."

Cadena final:

Busca la radio en el archivo de la comisaria.

---

# 9. Derivación completa del diálogo inicial de Marcos

<DIALOGO_MARCOS_INICIO>

=> <NPC_MARCOS> <PETICION_MARCOS>

=> "Marcos:" <PETICION_MARCOS>

=> "Marcos:"
   "Necesito una radio para contactar a los militares."
   <MISION_MARCOS>

=> "Marcos:"
   "Necesito una radio para contactar a los militares."
   <ACCION_MARCOS>
   <OBJETO_MARCOS>
   <LUGAR_MARCOS>

=> "Marcos:"
   "Necesito una radio para contactar a los militares."
   "Busca"
   <OBJETO_MARCOS>
   <LUGAR_MARCOS>

=> "Marcos:"
   "Necesito una radio para contactar a los militares."
   "Busca"
   "la radio"
   <LUGAR_MARCOS>

=> "Marcos:"
   "Necesito una radio para contactar a los militares."
   "Busca"
   "la radio"
   "en el archivo de la comisaria."

Cadena final:

Marcos: Necesito una radio para contactar a los militares.
Busca la radio en el archivo de la comisaria.

---

# 10. Diálogo final de Marcos

La gramática también permite generar el diálogo que entrega la
Tarjeta Militar.

<DIALOGO_MARCOS_FINAL>

=> <NPC_MARCOS> <AGRADECIMIENTO_MARCOS>

=> "Marcos:" <AGRADECIMIENTO_MARCOS>

=> "Marcos:"
   "Gracias por traer la radio. Toma esta tarjeta militar."

Cadena final:

Marcos: Gracias por traer la radio. Toma esta tarjeta militar.

Este diálogo conecta la GLC con el estado del mundo, porque después
de completar la misión el jugador recibe la Tarjeta Militar que le
permite acceder a BASE_MILITAR.

---

# 11. ¿Por qué es una Gramática Libre de Contexto?

La gramática es libre de contexto porque todas las producciones
tienen un único símbolo no terminal en el lado izquierdo.

Por ejemplo:

<MISION> ::= <ACCION> <OBJETO> <LUGAR>

y:

<MISION_MARCOS> ::=
<ACCION_MARCOS> <OBJETO_MARCOS> <LUGAR_MARCOS>

No es necesario conocer los símbolos anteriores o posteriores para
decidir qué producción aplicar.

---

# 12. Derivación por la izquierda

El videojuego implementa una derivación por la izquierda mediante el
método:

obtener_derivacion()

El algoritmo recorre la cadena de izquierda a derecha y sustituye el
primer símbolo que todavía sea no terminal.

Después vuelve a comenzar el proceso hasta que todos los símbolos
son terminales.

Ejemplo:

<MISION>

=> <ACCION> <OBJETO> <LUGAR>

=> Busca <OBJETO> <LUGAR>

=> Busca medicamentos <LUGAR>

=> Busca medicamentos en la farmacia.

---

# 13. Generación de cadenas en Python

El método:

generar()

recibe un símbolo y comprueba si pertenece a las reglas.

Si no pertenece a las reglas, se considera un símbolo terminal.

Si sí pertenece, obtiene una producción y continúa expandiendo
recursivamente sus símbolos.

Actualmente el código utiliza:

self.reglas[simbolo][0]

Esto significa que selecciona la primera producción disponible.

Por ejemplo:

<ACCION> ::= "Busca" | "Encuentra"

Durante la generación automática se selecciona:

"Busca"

porque es la primera alternativa almacenada.

La gramática formal continúa permitiendo ambas cadenas.

---

# 14. Relación de la GLC con el videojuego

La GLC no controla los cambios de escenario.

El AFN se encarga de los estados narrativos.

La pila se encarga de recordar escenarios anidados.

La GLC se encarga de generar textos válidos para:

- diálogos;
- misiones;
- recordatorios;
- agradecimientos.

Ejemplo de integración:

Marcos
↓
GLC genera misión
↓
Busca la radio en el archivo de la comisaria.
↓
Jugador encuentra Radio
↓
GLC genera diálogo final
↓
Jugador obtiene Tarjeta Militar
↓
Puede entrar a BASE_MILITAR

---

# 15. Resumen

El videojuego contiene dos grupos principales de producciones:

1. Gramática de Elena.
2. Gramática de Marcos.

Ambas están escritas en BNF y permiten producir cadenas válidas
mediante derivación por la izquierda.

La gramática está integrada directamente con los NPC y las misiones
del videojuego.