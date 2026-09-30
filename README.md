Resumen de cambios de Zona Cero Ultimo Refugio   29/09/2026

**Rama de trabajo:** `pruebas-darvin`

## Resumen general

Se trabajó en una rama separada llamada `pruebas-darvin` para no modificar directamente la rama principal del proyecto. Los cambios principales fueron agregar una acción no determinista al AFN, mostrar su historial de transiciones y renovar la interfaz del juego.

## Cambios realizados

- Se agregó la acción `EXPLORAR` cuando el jugador está en `CALLE`. Se activa con la tecla **X**.
- `EXPLORAR` puede enviar al jugador al `HOSPITAL` o a la `COMISARIA`. Esto demuestra el comportamiento no determinista del AFN.
- Se agregó un historial que guarda el estado anterior, la acción realizada, los destinos posibles y el destino elegido.
- La barra superior muestra el estado actual y la última transición del AFN.
- Se renovó toda la interfaz con paneles oscuros, bordes verdes y amarillos, nuevos iconos y textos más claros.
- Se rediseñaron también las pantallas de combate, gramática, evacuación y finales.
- La ventana aumentó a **1200 × 780** para que los nombres y títulos se puedan leer mejor, sin cambiar las coordenadas internas ni las colisiones.
- El mensaje de misión completada ahora desaparece automáticamente después de cuatro segundos.
- Se hicieron más pequeños los cuadros de inventario, vida y pila del mundo para que ocupen menos espacio en pantalla.
- La carpeta `.venv` quedó ignorada por Git y no se subió al repositorio.

## Archivos principales modificados

- `automata.py`: acción `EXPLORAR`, destinos posibles e historial del AFN.
- `main.py`: control con la tecla **X**, integración de transiciones y escalado de la ventana.
- `interfaz.py`: nuevo diseño del HUD y de las pantallas auxiliares.
- `mision.py`: temporizador para ocultar el mensaje de misión completada.
- `mapa.py`, `npc.py` y `enemigo.py`: ajustes de fuentes, nombres y tamaños.
- `finales.py`: actualización visual de las pantallas finales.
- `pruebas_alcanzabilidad.py`: pruebas del no determinismo, historial y finales.
- `DIAGRAMA_AFN.md`: documentación actualizada del autómata.

## Pruebas realizadas

- Se comprobó que `EXPLORAR` tenga dos destinos posibles: `HOSPITAL` y `COMISARIA`.
- Se comprobó que el historial guarde correctamente cada transición.
- Se verificó que los tres finales del juego sigan siendo alcanzables.
- Se revisó que el juego inicie y que la interfaz se muestre sin errores importantes.
- Se comprobó que el aviso de misión completada desaparezca automáticamente.

## Commits realizados

- `6c26d53` — Agregar exploración no determinista y renovar interfaz.
- `6156707` — Mostrar historial de transiciones del AFN.

## Texto para compartir con ChatGPT

> Estoy trabajando en el proyecto Zona Cero: Ultimo Refugio, hecho en Python con Pygame. En la rama pruebas-darvin se agregó la acción EXPLORAR desde CALLE, que puede llevar a HOSPITAL o COMISARIA para representar un AFN no determinista. También se añadió un historial de transiciones, se renovó la interfaz completa, se aumentó el tamaño de la ventana, se hizo temporal el aviso de misión completada y se actualizaron las pruebas y la documentación. Necesito continuar trabajando sobre estos cambios sin modificar la rama main.

## Estado actual

Los cambios ya fueron subidos a GitHub en la rama `pruebas-darvin`. La rama principal no fue modificada directamente y el proyecto puede continuar desarrollándose desde esta rama.
