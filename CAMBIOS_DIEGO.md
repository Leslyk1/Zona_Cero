# Registro de cambios de pruebas-diego

Esta rama parte de `pruebas-darvin`. Cada grupo de cambios se documenta aquí
con su propósito, los archivos afectados y las comprobaciones realizadas.
Los comentarios `Diego:` en el código identifican los cambios de esta rama
y explican por qué se hicieron. El historial de Git conserva las versiones.

## 30/09/2026 — Separar los paneles del escenario

**Estado:** incluido en la entrega de interfaz, combate y diario de `pruebas-diego`.

**Problema:** los paneles de inventario y vida ocultaban al personaje inicial
y algunos nombres de habitaciones. La pila tapaba parte de la entrada del
hospital. Los mensajes también se dibujaban encima del mapa.

**Resultado:** el mapa ocupa su propia superficie. Inventario, vida, pila y
misión se muestran en una columna derecha; el estado del AFN queda arriba y
los diálogos e interacciones quedan abajo. La columna incluye los controles.
Se conserva el estilo verde y amarillo, las coordenadas lógicas de 1000 × 650
y la ventana de 1200 × 780. El mapa se ve algo más pequeño para dejar espacio
a la información. Los finales mantienen su presentación a pantalla completa.

| Archivo | Qué cambia y para qué sirve |
| --- | --- |
| `Codigo/configuracion.py` | Define las medidas de la cabecera, columna y mensajes, separadas de las medidas del mapa. |
| `Codigo/main.py` | Dibuja cada grupo de elementos en su superficie y compone la ventana sin deformar el mapa. Limpia los mensajes de interacción cada fotograma. |
| `Codigo/interfaz.py` | Reubica los paneles, ajusta los textos a varias líneas y añade una ayuda de controles. Mantiene el aviso de misión completada de cuatro segundos. |
| `CAMBIOS_DIEGO.md` | Explica el motivo, el resultado y la verificación de este cambio. |

### Comprobaciones realizadas

- Sintaxis válida de los 16 archivos Python y revisión de espacios con Git.
- Pruebas existentes de no determinismo y alcanzabilidad: correctas.
- Arranque y cierre del juego sin ventana visible mediante el controlador
  de vídeo de pruebas de Pygame.
- Simulación de 34 pasos con posiciones preparadas y resultados aleatorios
  controlados: gramática, ambos destinos de EXPLORAR, misión de Elena,
  desaparición del aviso, PUSH/POP, ambos combates, inventario y tres finales.
- Comparación de la superficie del mapa con su región en la composición:
  los paneles generales ya no se dibujan sobre ella.
- Revisión visual de capturas del refugio, calle, hospital, sótano, combate,
  gramática, inventario y final de evacuación.

La simulación no sustituye una partida manual ni verifica todas las rutas
de movimiento, probabilidades o tamaños de pantalla.

Esta etapa se registra junto con la renovación de arte, combate y diario.

## 30/09/2026 — Apariencia RPG, batalla por turnos y diario

**Estado:** incluido en la entrega de `pruebas-diego`. Continúa la
separación de paneles descrita arriba.

### Qué cambia para quien juega

- El jugador, Elena y los dos zombis tienen dibujos propios; la medicina,
  pistola y balas tienen iconos reconocibles. Hay texturas, sombras, señales,
  detalles de suelo y una paleta común de azul oscuro, menta y ámbar.
- El combate presenta al superviviente de espaldas frente al enemigo, con
  plataformas, barras de vida, efectos de daño y tres acciones seleccionables.
  Se puede usar 1/2/3, flechas y Enter o el ratón.
- El ataque se muestra durante 850 ms y la respuesta durante 1000 ms. No se
  pueden acumular ataques pulsando rápidamente. Se conservan daños y probabilidades.
- J abre un diario con las tres misiones actuales, los pasos de Elena, el
  porcentaje de avance y el siguiente objetivo. La columna muestra 0/3 a 3/3.
- El diario pausa movimiento e interacciones; se cierra con J o Esc. La misión
  terminada permanece visible aunque su aviso de cuatro segundos desaparezca.

### Archivos y propósito

| Archivo | Cambio |
| --- | --- |
| `Codigo/arte.py` (nuevo) | Dibujos de personajes, objetos, suelos, paredes y fondos de batalla. Caché de fuentes y fondos. |
| `Codigo/batalla.py` (nuevo) | Presentación del combate, animaciones, barras y áreas de clic. |
| `Codigo/combate.py` | Autómata con fases temporizadas y bloqueo de acciones repetidas. |
| `Codigo/mision.py` | Diario calculado a partir de misión, inventario y enemigos reales. |
| `Codigo/interfaz.py` | Diario, resumen permanente, colores, fuentes y ayuda de controles. |
| `Codigo/main.py` | Controles del diario y del menú de batalla; actualización del combate y del progreso. |
| `Codigo/mapa.py` | Conecta los mapas con el nuevo arte conservando las funciones de colisión. |
| `Codigo/jugador.py` | Apariencia del superviviente y orientación al caminar. |
| `Codigo/npc.py`, `Codigo/enemigo.py`, `Codigo/objeto.py` | Dibujos de personajes y objetos en lugar de cuadrados planos. |
| `Codigo/pruebas_juego.py` (nuevo) | Pruebas de combate y diario con reloj y azar controlados. |
| `Codigo/COMBATE_Y_MISIONES.md` (nuevo) | Diagrama del combate, probabilidades, controles y cálculo de progreso. |
| `Codigo/DIAGRAMA_AFN.md` | Enlace a la documentación del subsistema de combate. |
| `README.md`, `requirements.txt` (nuevo) | Instrucciones actuales y dependencia reproducible. Conserva el historial de Darvin. |

### Verificación

- 12 pruebas automáticas de combate y diario, con casos de frontera de las probabilidades.
- Pruebas originales de EXPLORAR y alcanzabilidad de los tres finales.
- Recorrido simulado de 51 pasos con gramática, diario, ambas batallas, objetivos,
  inventario y tres finales; posiciones y azar preparados para reproducibilidad.
- Comprobación del clic en ventana escalada, doble clic, flechas/Enter, pausa
  de movimiento, derrota y recuperación sin perder las otras misiones.
- Revisión visual de capturas del mapa, combate y diario.

Las comprobaciones automáticas no sustituyen una partida manual. El diario
muestra progreso de la sesión actual; no hay guardado de partidas en disco.

**Entrega:** `Renovar interfaz, combate por turnos y diario de misiones`.
Las 12 pruebas de combate y diario y las pruebas originales del AFN se
ejecutaron nuevamente antes de registrar esta entrega, con resultado correcto.
