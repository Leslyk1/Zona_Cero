# -----------------------------------
# CONFIGURACIÓN GENERAL DEL JUEGO
# -----------------------------------

# Tamaño lógico del mapa: también lo utilizan el movimiento y las colisiones.
ANCHO = 1000
ALTO = 650

# Diego: reservamos espacio fuera del mapa para que los paneles no oculten
# al jugador. Estas medidas solo organizan la interfaz, no las colisiones.
ANCHO_LATERAL = 250
ALTO_CABECERA = 70
ALTO_MENSAJES = 80
ANCHO_INTERFAZ = ANCHO + ANCHO_LATERAL
ALTO_INTERFAZ = ALTO + ALTO_CABECERA + ALTO_MENSAJES

# La composición completa se ajusta a esta ventana conservando su proporción.
ANCHO_VENTANA = 1200
ALTO_VENTANA = 780

# Cantidad de imágenes por segundo
FPS = 60


# -----------------------------------
# COLORES
# -----------------------------------

NEGRO = (0, 0, 0)

BLANCO = (255, 255, 255)

VERDE = (0, 255, 0)

GRIS = (80, 80, 80)

GRIS_OSCURO = (35, 35, 35)

GRIS_CLARO = (110, 110, 110)

AMARILLO = (220, 200, 50)

ROJO = (160, 50, 50)

ASFALTO = (45, 45, 50)
