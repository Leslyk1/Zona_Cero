"""Arte original de Zona Cero dibujado con Pygame; no requiere imágenes externas."""



from functools import lru_cache



import random



import pygame





TINTA = (12, 20, 28)



MARFIL = (220, 232, 224)



MENTA = (98, 225, 176)



ORO = (232, 190, 111)





# ===================================

# FUENTES

# ===================================



@lru_cache(maxsize=32)

def fuente(tamano, negrita=False):



    # Diego:

    # reutilizar las fuentes evita

    # buscarlas en Windows cada fotograma.

    return pygame.font.SysFont(

        "Segoe UI",

        tamano,

        bold=negrita

    )





# ===================================

# SPRITES

# ===================================



@lru_cache(maxsize=32)

def sprite(

    tipo,

    espalda=False,

    paso=0

):



    # Diego:

    # personajes originales en una cuadrícula pequeña;

    # el mismo dibujo sirve en el mapa y,

    # ampliado, en la batalla.

    #

    # El rectángulo físico no cambia.



    lienzo = pygame.Surface(

        (48, 64),

        pygame.SRCALPHA

    )





    # -----------------------------------

    # COLORES BASE

    # -----------------------------------



    piel = (211, 164, 122)



    ropa = (39, 107, 105)



    luz = (69, 151, 135)



    pelo = (41, 39, 41)





    # ===================================

    # ELENA

    # ===================================



    if tipo == "elena":



        ropa = (179, 202, 187)



        luz = (222, 233, 213)



        pelo = (92, 48, 43)





    # ===================================

    # MARCOS

    # ===================================



    elif tipo == "marcos":



        # Lesly:

        # Marcos utiliza una apariencia

        # distinta a Elena y a los enemigos.

        #

        # Utilizamos tonos azul oscuro

        # para mantener el estilo

        # posapocalíptico del juego.



        piel = (195, 146, 105)



        ropa = (54, 74, 87)



        luz = (86, 113, 121)



        pelo = (40, 31, 27)





    # ===================================

    # ZOMBI POLICÍA

    # ===================================



    elif tipo == "policia":



        piel = (134, 164, 116)



        ropa = (44, 58, 80)



        luz = (65, 85, 112)





    # ===================================

    # ZOMBI CORREDOR

    # ===================================



    elif tipo == "corredor":



        piel = (152, 159, 111)



        ropa = (111, 64, 57)



        luz = (159, 84, 63)





    # ===================================

    # FUNCIÓN PARA DIBUJAR BLOQUES

    # ===================================



    def bloque(

        rect,

        color,

        borde=True

    ):



        pygame.draw.rect(

            lienzo,

            TINTA,

            rect

        )





        if borde:



            interior = pygame.Rect(

                rect

            ).inflate(

                -2,

                -2

            )



        else:



            interior = rect





        pygame.draw.rect(

            lienzo,

            color,

            interior

        )





    # ===================================

    # CUERPO DEL PERSONAJE

    # ===================================



    # Botas, pantalones, brazos,

    # torso y cabeza.



    desplazamiento = (

        2

        if paso

        else 0

    )





    # Piernas.

    bloque(

        (

            13,

            43,

            10,

            17 - desplazamiento

        ),

        (48, 53, 58)

    )





    bloque(

        (

            26,

            43,

            10,

            17

        ),

        (40, 48, 53)

    )





    # Botas.

    bloque(

        (

            10,

            56 - desplazamiento,

            14,

            7

        ),

        (25, 31, 38)

    )





    bloque(

        (

            25,

            57,

            15,

            6

        ),

        (25, 31, 38)

    )





    # Brazos.

    bloque(

        (

            5,

            28,

            9,

            19

        ),

        ropa

    )





    bloque(

        (

            35,

            28,

            9,

            19

        ),

        ropa

    )





    # Manos.

    bloque(

        (

            6,

            44,

            8,

            7

        ),

        piel

    )





    bloque(

        (

            35,

            44,

            8,

            7

        ),

        piel

    )





    # Torso.

    bloque(

        (

            11,

            24,

            27,

            25

        ),

        ropa

    )





    # Parte clara de la ropa.

    bloque(

        (

            14,

            27,

            9,

            16

        ),

        luz,

        False

    )





    # Cinturón.

    bloque(

        (

            12,

            45,

            26,

            4

        ),

        (59, 47, 39),

        False

    )





    # Hebilla.

    bloque(

        (

            24,

            45,

            5,

            4

        ),

        ORO,

        False

    )





    # Pelo.

    bloque(

        (

            12,

            5,

            26,

            23

        ),

        pelo

    )





    # ===================================

    # PERSONAJE DE ESPALDA

    # ===================================



    if espalda:



        bloque(

            (

                14,

                9,

                22,

                16

            ),

            (48, 73, 72),

            False

        )





        bloque(

            (

                15,

                29,

                20,

                20

            ),

            (115, 87, 55)

        )





        bloque(

            (

                18,

                33,

                14,

                6

            ),

            (153, 119, 72)

        )





        bloque(

            (

                19,

                42,

                12,

                5

            ),

            (85, 67, 45)

        )





    # ===================================

    # PERSONAJE DE FRENTE

    # ===================================



    else:



        # Cara.

        bloque(

            (

                16,

                11,

                19,

                15

            ),

            piel,

            False

        )





        # Parte superior del pelo.

        bloque(

            (

                12,

                5,

                26,

                7

            ),

            pelo,

            False

        )





        # Ojo izquierdo.

        bloque(

            (

                18,

                16,

                4,

                3

            ),

            TINTA,

            False

        )





        # Ojo derecho.

        bloque(

            (

                29,

                16,

                4,

                3

            ),

            TINTA,

            False

        )





        # Boca.

        bloque(

            (

                25,

                22,

                6,

                2

            ),

            (122, 84, 70),

            False

        )





        # ===================================

        # SUPERVIVIENTE

        # ===================================



        if tipo == "superviviente":



            bloque(

                (

                    10,

                    25,

                    29,

                    6

                ),

                (219, 151, 76)

            )





            bloque(

                (

                    30,

                    29,

                    6,

                    12

                ),

                (176, 111, 58),

                False

            )





            bloque(

                (

                    8,

                    3,

                    32,

                    7

                ),

                (37, 89, 88)

            )





        # ===================================

        # ELENA

        # ===================================



        elif tipo == "elena":



            # Cabello largo.

            bloque(

                (

                    13,

                    7,

                    4,

                    23

                ),

                pelo,

                False

            )





            bloque(

                (

                    34,

                    7,

                    5,

                    24

                ),

                pelo,

                False

            )





            # Cruz médica.

            bloque(

                (

                    26,

                    31,

                    8,

                    3

                ),

                (165, 69, 60),

                False

            )





            bloque(

                (

                    29,

                    28,

                    3,

                    9

                ),

                (165, 69, 60),

                False

            )





        # ===================================

        # MARCOS

        # ===================================



        elif tipo == "marcos":



            # Lesly:

            # agregamos algunos detalles

            # simples para distinguirlo

            # visualmente.



            # Franja de la chaqueta.

            bloque(

                (

                    12,

                    28,

                    25,

                    4

                ),

                (104, 139, 145),

                False

            )





            # Pequeño distintivo.

            bloque(

                (

                    30,

                    34,

                    5,

                    6

                ),

                ORO,

                False

            )





            # Cabello corto.

            bloque(

                (

                    15,

                    4,

                    21,

                    6

                ),

                pelo,

                False

            )





        # ===================================

        # POLICÍA

        # ===================================



        elif tipo == "policia":



            # Gorra.

            bloque(

                (

                    9,

                    3,

                    30,

                    10

                ),

                (48, 66, 92)

            )





            bloque(

                (

                    8,

                    11,

                    33,

                    3

                ),

                (29, 37, 55),

                False

            )





            # Insignias.

            bloque(

                (

                    23,

                    6,

                    5,

                    5

                ),

                ORO,

                False

            )





            bloque(

                (

                    28,

                    30,

                    5,

                    6

                ),

                ORO,

                False

            )





        # ===================================

        # CORREDOR

        # ===================================



        else:



            bloque(

                (

                    14,

                    38,

                    8,

                    7

                ),

                piel,

                False

            )





            # Marca / herida.

            pygame.draw.line(

                lienzo,

                (89, 44, 41),

                (20, 21),

                (26, 25),

                2

            )





    return lienzo





# ===================================

# DIBUJAR PERSONAJE

# ===================================



def personaje(

    ventana,

    rect,

    tipo="superviviente",

    espalda=False,

    moviendo=False

):



    fase = (

        (pygame.time.get_ticks() // 160) % 2

        if moviendo

        else 0

    )





    dibujo = pygame.transform.scale(

        sprite(

            tipo,

            espalda,

            fase

        ),

        (42, 56)

    )





    # Sombra.

    pygame.draw.ellipse(

        ventana,

        (13, 20, 27),

        (

            rect.x - 4,

            rect.bottom - 8,

            48,

            14

        )

    )





    # Personaje.

    ventana.blit(

        dibujo,

        (

            rect.centerx - 21,

            rect.bottom - 52

        )

    )





    # Línea especial del jugador.

    if tipo == "superviviente":



        pygame.draw.line(

            ventana,

            MENTA,

            (

                rect.x + 8,

                rect.bottom + 6

            ),

            (

                rect.right - 8,

                rect.bottom + 6

            ),

            2

        )





# ===================================

# ETIQUETA

# ===================================



def etiqueta(

    ventana,

    texto,

    centro,

    color=MARFIL,

    tamano=15

):



    dibujo = fuente(

        tamano,

        True

    ).render(

        texto,

        True,

        color

    )





    rect = dibujo.get_rect(

        center=centro

    )





    pygame.draw.rect(

        ventana,

        (19, 31, 39),

        rect.inflate(

            18,

            9

        ),

        border_radius=4

    )





    ventana.blit(

        dibujo,

        rect

    )





# ===================================

# OBJETOS

# ===================================



def objeto(

    ventana,

    rect,

    nombre

):



    x = rect.x

    y = rect.y





    # Sombra.

    pygame.draw.ellipse(

        ventana,

        (12, 22, 29),

        (

            x - 5,

            y + 23,

            40,

            12

        )

    )





    # ===================================

    # MEDICAMENTO

    # ===================================



    if nombre == "Medicamento":



        pygame.draw.circle(

            ventana,

            MENTA,

            (

                x + 15,

                y + 15

            ),

            23,

            1

        )



        pygame.draw.rect(

            ventana,

            (205, 221, 207),

            (

                x,

                y + 5,

                30,

                23

            ),

            border_radius=4

        )



        pygame.draw.rect(

            ventana,

            (114, 59, 57),

            (

                x + 11,

                y + 9,

                8,

                15

            )

        )



        pygame.draw.rect(

            ventana,

            (114, 59, 57),

            (

                x + 7,

                y + 13,

                16,

                7

            )

        )





    # ===================================

    # PISTOLA

    # ===================================



    elif nombre == "Pistola":



        pygame.draw.circle(

            ventana,

            ORO,

            (

                x + 15,

                y + 15

            ),

            23,

            1

        )



        pygame.draw.polygon(

            ventana,

            (164, 178, 183),

            [

                (x, y + 8),

                (x + 29, y + 8),

                (x + 29, y + 16),

                (x + 16, y + 16),

                (x + 12, y + 29),

                (x + 4, y + 27),

                (x + 8, y + 15),

                (x, y + 15)

            ]

        )



        pygame.draw.line(

            ventana,

            (60, 76, 85),

            (

                x + 5,

                y + 10

            ),

            (

                x + 26,

                y + 10

            ),

            2

        )





    # ===================================

    # RADIO

    # ===================================



    elif nombre == "Radio":



        pygame.draw.circle(

            ventana,

            MENTA,

            (

                x + 15,

                y + 15

            ),

            23,

            1

        )



        # Cuerpo.

        pygame.draw.rect(

            ventana,

            (45, 62, 72),

            (

                x + 2,

                y + 5,

                27,

                25

            ),

            border_radius=4

        )



        # Borde.

        pygame.draw.rect(

            ventana,

            (112, 139, 145),

            (

                x + 2,

                y + 5,

                27,

                25

            ),

            2,

            border_radius=4

        )



        # Pantalla.

        pygame.draw.rect(

            ventana,

            MENTA,

            (

                x + 7,

                y + 9,

                15,

                6

            ),

            border_radius=2

        )



        # Bocina.

        pygame.draw.circle(

            ventana,

            (18, 28, 35),

            (

                x + 15,

                y + 22

            ),

            5

        )



        # Botón.

        pygame.draw.circle(

            ventana,

            ORO,

            (

                x + 24,

                y + 20

            ),

            2

        )



        # Antena.

        pygame.draw.line(

            ventana,

            (164, 178, 183),

            (

                x + 24,

                y + 6

            ),

            (

                x + 29,

                y - 6

            ),

            2

        )





    # ===================================

    # ARCHIVO MILITAR

    # ===================================



    elif nombre == "Archivo Militar":



        # Resplandor de interacción.

        pygame.draw.circle(

            ventana,

            MENTA,

            (

                x + 15,

                y + 15

            ),

            23,

            1

        )



        # Carpeta militar.

        pygame.draw.rect(

            ventana,

            (85, 96, 67),

            (

                x + 2,

                y + 8,

                28,

                20

            ),

            border_radius=3

        )



        # Pestaña de la carpeta.

        pygame.draw.rect(

            ventana,

            (112, 124, 83),

            (

                x + 5,

                y + 4,

                12,

                7

            ),

            border_radius=2

        )



        # Hoja confidencial.

        pygame.draw.rect(

            ventana,

            (215, 218, 194),

            (

                x + 7,

                y + 10,

                18,

                14

            )

        )



        # Líneas del documento.

        pygame.draw.line(

            ventana,

            (78, 87, 70),

            (

                x + 10,

                y + 14

            ),

            (

                x + 22,

                y + 14

            ),

            2

        )



        pygame.draw.line(

            ventana,

            (78, 87, 70),

            (

                x + 10,

                y + 18

            ),

            (

                x + 19,

                y + 18

            ),

            2

        )



        # Sello de documento clasificado.

        pygame.draw.rect(

            ventana,

            (151, 60, 55),

            (

                x + 10,

                y + 20,

                12,

                4

            )

        )



    # ===================================

    # BALAS

    # ===================================



    elif nombre == "Balas":



        pygame.draw.circle(

            ventana,

            ORO,

            (

                x + 15,

                y + 15

            ),

            23,

            1

        )



        for desplazamiento in (

            0,

            10,

            20

        ):



            pygame.draw.rect(

                ventana,

                (181, 128, 64),

                (

                    x + desplazamiento,

                    y + 9,

                    7,

                    19

                )

            )



            pygame.draw.polygon(

                ventana,

                ORO,

                [

                    (

                        x + desplazamiento,

                        y + 9

                    ),

                    (

                        x + desplazamiento + 3,

                        y + 3

                    ),

                    (

                        x + desplazamiento + 7,

                        y + 9

                    )

                ]

            )





    # ===================================

    # OBJETO GENÉRICO

    # ===================================



    else:



        pygame.draw.circle(

            ventana,

            ORO,

            (

                x + 15,

                y + 15

            ),

            15

        )





# ===================================

# PISO DE LOS ESCENARIOS

# ===================================



@lru_cache(maxsize=8)

def piso(tipo):



    # Diego:

    # la decoración es fija

    # y se genera una sola vez.

    #

    # Se utiliza un generador local

    # para que el arte no cambie

    # las probabilidades del combate.



    rng = random.Random(

        tipo

    )





    lienzo = pygame.Surface(

        (1000, 650)

    )





    bases = {



    "REFUGIO":

        (38, 50, 53),



    "HOSPITAL":

        (37, 59, 59),



    "SOTANO_HOSPITAL":

        (31, 38, 45),



    "COMISARIA":

        (37, 47, 61),



    "CALLE":

        (37, 43, 51),



    # Base Militar.

    "BASE_MILITAR":

        (43, 51, 45)

}





    base = bases[

        tipo

    ]





    lienzo.fill(

        (18, 26, 34)

    )





    # -----------------------------------

    # CUADRÍCULA DEL SUELO

    # -----------------------------------



    for x in range(

        0,

        1000,

        40

    ):



        for y in range(

            0,

            650,

            40

        ):



            brillo = rng.randint(

                -3,

                3

            )





            color = tuple(

                c + brillo

                for c in base

            )





            pygame.draw.rect(

                lienzo,

                color,

                (

                    x,

                    y,

                    39,

                    39

                )

            )





            if rng.random() < .16:



                pygame.draw.line(

                    lienzo,

                    tuple(

                        c + 5

                        for c in color

                    ),

                    (

                        x + 8,

                        y + 30

                    ),

                    (

                        x + 22,

                        y + 30

                    )

                )





    # ===================================

    # CALLE

    # ===================================



    if tipo == "CALLE":



        pygame.draw.rect(

            lienzo,

            (50, 59, 65),

            (

                0,

                0,

                1000,

                100

            )

        )





        pygame.draw.rect(

            lienzo,

            (50, 59, 65),

            (

                0,

                550,

                1000,

                100

            )

        )





        for x in range(

            120,

            1000,

            120

        ):



            pygame.draw.rect(

                lienzo,

                (164, 148, 88),

                (

                    x,

                    322,

                    65,

                    5

                )

            )





        for _ in range(

            30

        ):



            x = rng.randrange(

                80,

                970

            )



            y = rng.randrange(

                195,

                550

            )





            pygame.draw.lines(

                lienzo,

                (25, 32, 39),

                False,

                [

                    (

                        x,

                        y

                    ),

                    (

                        x + 14,

                        y - 8

                    ),

                    (

                        x + 23,

                        y - 4

                    )

                ],

                2

            )





        for x, y in (

            (290, 290),

            (590, 170),

            (820, 490)

        ):



            pygame.draw.ellipse(

                lienzo,

                (35, 57, 63),

                (

                    x,

                    y,

                    85,

                    22

                )

            )





            pygame.draw.arc(

                lienzo,

                (61, 88, 88),

                (

                    x,

                    y,

                    85,

                    22

                ),

                0,

                3,

                1

            )





    # ===================================

    # REFUGIO

    # ===================================



    elif tipo == "REFUGIO":



        # Sacos decorativos.

        for y in (

            225,

            260

        ):



            for x in (

                100,

                250

            ):



                pygame.draw.rect(

                    lienzo,

                    (43, 72, 66),

                    (

                        x,

                        y,

                        85,

                        25

                    ),

                    border_radius=6

                )





                pygame.draw.rect(

                    lienzo,

                    (133, 152, 126),

                    (

                        x + 5,

                        y + 4,

                        18,

                        17

                    ),

                    border_radius=3

                )





        pygame.draw.rect(

            lienzo,

            (48, 66, 68),

            (

                590,

                210,

                230,

                105

            ),

            2,

            border_radius=8

        )





        pygame.draw.circle(

            lienzo,

            (68, 92, 85),

            (

                705,

                260

            ),

            32,

            2

        )





    # ===================================

    # HOSPITAL

    # ===================================



    elif tipo == "HOSPITAL":



        pygame.draw.rect(

            lienzo,

            (41, 83, 77),

            (

                460,

                75,

                55,

                500

            )

        )





        for y in range(

            95,

            510,

            60

        ):



            pygame.draw.line(

                lienzo,

                (111, 143, 125),

                (

                    486,

                    y

                ),

                (

                    486,

                    y + 20

                ),

                2

            )





        for x, y in (

            (290, 425),

            (835, 220)

        ):



            pygame.draw.rect(

                lienzo,

                (71, 113, 100),

                (

                    x,

                    y,

                    12,

                    38

                )

            )





            pygame.draw.rect(

                lienzo,

                (71, 113, 100),

                (

                    x - 13,

                    y + 13,

                    38,

                    12

                )

            )





    # ===================================

    # OTROS ESCENARIOS

    # ===================================



    else:



        for y in (

            160,

            510

        ):



            pygame.draw.line(

                lienzo,

                (58, 70, 78),

                (

                    95,

                    y

                ),

                (

                    310,

                    y

                ),

                2

            )





            for x in range(

                95,

                310,

                24

            ):



                pygame.draw.line(

                    lienzo,

                    (58, 70, 78),

                    (

                        x,

                        y - 7

                    ),

                    (

                        x + 8,

                        y + 7

                    ),

                    2

                )





    return lienzo





# ===================================

# PUERTAS

# ===================================



def puerta(

    ventana,

    rect,

    texto,

    color=ORO

):



    pygame.draw.rect(

        ventana,

        (20, 36, 43),

        rect,

        border_radius=4

    )





    pygame.draw.rect(

        ventana,

        color,

        rect,

        2,

        border_radius=4

    )





    for x in range(

        rect.left + 7,

        rect.right - 5,

        15

    ):



        pygame.draw.line(

            ventana,

            color,

            (

                x,

                rect.bottom - 9

            ),

            (

                x + 6,

                rect.bottom - 3

            ),

            2

        )





    etiqueta(

        ventana,

        texto,

        (

            rect.centerx,

            rect.top - 15

        ),

        color,

        13

    )





# ===================================

# ESCENARIOS

# ===================================



def escenario(

    ventana,

    paredes,

    tipo

):



    ventana.blit(

        piso(tipo),

        (0, 0)

    )





    # Diego:

    # se decoran las paredes recibidas

    # del mapa.

    #

    # Estas siguen siendo las únicas

    # colisiones del escenario.



    for i, pared in enumerate(

        paredes

    ):



        pygame.draw.rect(

            ventana,

            (18, 26, 34),

            pared.move(

                5,

                7

            ),

            border_radius=3

        )





        pygame.draw.rect(

            ventana,

            (67, 81, 85),

            pared,

            border_radius=3

        )





        pygame.draw.rect(

            ventana,

            (102, 120, 117),

            pared,

            1,

            border_radius=3

        )





        interior = pared.inflate(

            -8,

            -8

        )





        pygame.draw.rect(

            ventana,

            (45, 58, 65),

            interior,

            border_radius=2

        )





        if (

            tipo == "CALLE"

            and

            pared.width > 100

        ):



            for x in range(

                pared.left + 15,

                pared.right - 20,

                35

            ):



                pygame.draw.rect(

                    ventana,

                    (28, 43, 54),

                    (

                        x,

                        pared.top + 18,

                        18,

                        28

                    )

                )





                pygame.draw.line(

                    ventana,

                    (115, 126, 107),

                    (

                        x,

                        pared.top + 18

                    ),

                    (

                        x + 17,

                        pared.top + 18

                    ),

                    2

                )





        elif pared.width > 200:



            pygame.draw.line(

                ventana,

                (111, 152, 138),

                (

                    pared.left + 18,

                    pared.top + 6

                ),

                (

                    pared.left + 65,

                    pared.top + 6

                ),

                3

            )





    # ===================================

    # REFUGIO

    # ===================================



    if tipo == "REFUGIO":



        etiqueta(

            ventana,

            "DORMITORIO",

            (

                235,

                108

            )

        )





        etiqueta(

            ventana,

            "ALMACÉN",

            (

                220,

                390

            )

        )





        etiqueta(

            ventana,

            "SALA PRINCIPAL",

            (

                690,

                115

            )

        )





        puerta(

            ventana,

            pygame.Rect(

                897,

                285,

                27,

                82

            ),

            "SALIDA",

            MENTA

        )





    # ===================================

    # CALLE

    # ===================================



    elif tipo == "CALLE":



        etiqueta(

            ventana,

            "CALLE ABANDONADA",

            (

                495,

                293

            ),

            MARFIL,

            18

        )





        puerta(

            ventana,

            pygame.Rect(

                70,

                285,

                16,

                80

            ),

            "REFUGIO",

            MENTA

        )





        puerta(

            ventana,

            pygame.Rect(

                800,

                174,

                70,

                12

            ),

            "HOSPITAL"

        )





        puerta(

            ventana,

            pygame.Rect(

                120,

                432,

                80,

                14

            ),

            "COMISARÍA"

        )


        # ===================================
        # BASE MILITAR
        # ===================================

        puerta(

            ventana,

            pygame.Rect(

                385,

                174,

                100,

                12

            ),

            "BASE MILITAR",

            MENTA

        )





    # ===================================

    # HOSPITAL

    # ===================================



    elif tipo == "HOSPITAL":



        etiqueta(

            ventana,

            "RECEPCIÓN",

            (

                230,

                115

            )

        )





        etiqueta(

            ventana,

            "LABORATORIO",

            (

                730,

                112

            )

        )





        etiqueta(

            ventana,

            "FARMACIA",

            (

                695,

                382

            ),

            MENTA

        )





        puerta(

            ventana,

            pygame.Rect(

                130,

                210,

                90,

                65

            ),

            "SÓTANO"

        )





        puerta(

            ventana,

            pygame.Rect(

                445,

                558,

                110,

                12

            ),

            "SALIDA",

            MENTA

        )

    # ===================================

    # BASE MILITAR

    # ===================================



    elif tipo == "BASE_MILITAR":



        etiqueta(

            ventana,

            "CONTROL DE ACCESO",

            (

                205,

                115

            ),

            MENTA

        )





        etiqueta(

            ventana,

            "CENTRO DE COMANDO",

            (

                700,

                115

            ),

            ORO

        )





        etiqueta(

            ventana,

            "ARSENAL MILITAR",

            (

                740,

                365

            ),

            ORO

        )





        # Salida hacia la calle.

        puerta(

            ventana,

            pygame.Rect(

                445,

                558,

                110,

                12

            ),

            "SALIDA",

            MENTA

        )





        # Decoración de cajas militares.

        for x, y in (

            (120, 220),

            (200, 220),

            (680, 400),

            (760, 400)

        ):



            pygame.draw.rect(

                ventana,

                (57, 75, 60),

                (

                    x,

                    y,

                    55,

                    35

                ),

                border_radius=4

            )





            pygame.draw.rect(

                ventana,

                (102, 126, 91),

                (

                    x,

                    y,

                    55,

                    35

                ),

                2,

                border_radius=4

            )





            pygame.draw.line(

                ventana,

                ORO,

                (

                    x + 5,

                    y + 17

                ),

                (

                    x + 50,

                    y + 17

                ),

                2

            )



    # ===================================

    # SÓTANO

    # ===================================



    elif tipo == "SOTANO_HOSPITAL":



        etiqueta(

            ventana,

            "GENERADORES",

            (

                207,

                115

            )

        )





        etiqueta(

            ventana,

            "ARCHIVO CLÍNICO",

            (

                736,

                113

            )

        )





        puerta(

            ventana,

            pygame.Rect(

                460,

                68,

                80,

                43

            ),

            "ESCALERAS",

            MENTA

        )





        for y in range(

            78,

            110,

            9

        ):



            pygame.draw.line(

                ventana,

                ORO,

                (

                    469,

                    y

                ),

                (

                    530,

                    y

                ),

                2

            )





    # ===================================

    # COMISARÍA

    # ===================================



    else:



        etiqueta(

            ventana,

            "RECEPCIÓN",

            (

                210,

                114

            )

        )





        etiqueta(

            ventana,

            "ARCHIVO",

            (

                715,

                115

            )

        )





        etiqueta(

            ventana,

            "ARMERÍA",

            (

                700,

                354

            ),

            ORO

        )





        puerta(

            ventana,

            pygame.Rect(

                445,

                558,

                110,

                12

            ),

            "SALIDA",

            MENTA

        )





# ===================================

# FONDO DE BATALLA

# ===================================



@lru_cache(maxsize=2)

def fondo_batalla(

    subterraneo=False

):



    lienzo = pygame.Surface(

        (1000, 650)

    )





    arriba = (

        (19, 31, 46)

        if not subterraneo

        else (22, 32, 39)

    )





    abajo = (

        (72, 92, 94)

        if not subterraneo

        else (63, 72, 69)

    )





    # -----------------------------------

    # DEGRADADO

    # -----------------------------------



    for y in range(

        650

    ):



        t = min(

            1,

            y / 460

        )





        color = tuple(

            round(

                a + (b - a) * t

            )

            for a, b

            in zip(

                arriba,

                abajo

            )

        )





        pygame.draw.line(

            lienzo,

            color,

            (

                0,

                y

            ),

            (

                1000,

                y

            )

        )





    # Diego:

    # Siluetas y luces originales:

    # una arena RPG que conserva

    # el mundo posapocalíptico.



    rng = random.Random(

        41

    )





    # ===================================

    # SÓTANO

    # ===================================



    if subterraneo:



        # Tuberías y generadores.

        for x in range(

            50,

            1000,

            180

        ):



            pygame.draw.rect(

                lienzo,

                (27, 43, 49),

                (

                    x,

                    70,

                    100,

                    220

                )

            )





            pygame.draw.rect(

                lienzo,

                (59, 77, 78),

                (

                    x + 12,

                    100,

                    78,

                    132

                ),

                2

            )





            for y in range(

                120,

                225,

                16

            ):



                pygame.draw.line(

                    lienzo,

                    (50, 68, 71),

                    (

                        x + 24,

                        y

                    ),

                    (

                        x + 78,

                        y

                    ),

                    3

                )





            pygame.draw.circle(

                lienzo,

                ORO,

                (

                    x + 51,

                    93

                ),

                3

            )





        for y in (

            77,

            253

        ):



            pygame.draw.line(

                lienzo,

                (79, 92, 86),

                (

                    0,

                    y

                ),

                (

                    1000,

                    y

                ),

                6

            )





            pygame.draw.line(

                lienzo,

                (30, 46, 52),

                (

                    0,

                    y + 5

                ),

                (

                    1000,

                    y + 5

                ),

                3

            )





    # ===================================

    # SUPERFICIE

    # ===================================



    else:



        for x in range(

            0,

            1000,

            80

        ):



            altura = rng.randrange(

                90,

                175

            )





            pygame.draw.rect(

                lienzo,

                (25, 40, 51),

                (

                    x,

                    280 - altura,

                    70,

                    altura

                )

            )





            for y in range(

                285 - altura,

                260,

                25

            ):



                for wx in (

                    x + 12,

                    x + 39

                ):



                    pygame.draw.rect(

                        lienzo,

                        (65, 84, 85),

                        (

                            wx,

                            y,

                            9,

                            12

                        )

                    )





    # -----------------------------------

    # SUELO DE BATALLA

    # -----------------------------------



    pygame.draw.polygon(

        lienzo,

        (37, 54, 61),

        [

            (

                0,

                290

            ),

            (

                1000,

                250

            ),

            (

                1000,

                650

            ),

            (

                0,

                650

            )

        ]

    )





    for y in range(

        320,

        470,

        35

    ):



        pygame.draw.line(

            lienzo,

            (48, 67, 71),

            (

                0,

                y

            ),

            (

                1000,

                y - 40

            ),

            1

        )





    # Plataformas.

    for rect in (



        pygame.Rect(

            610,

            264,

            290,

            75

        ),



        pygame.Rect(

            105,

            384,

            360,

            83

        )



    ):



        pygame.draw.ellipse(

            lienzo,

            (23, 36, 45),

            rect.move(

                0,

                9

            )

        )





        pygame.draw.ellipse(

            lienzo,

            (81, 103, 100),

            rect

        )





        pygame.draw.ellipse(

            lienzo,

            (142, 162, 137),

            rect,

            2

        )





        pygame.draw.ellipse(

            lienzo,

            (64, 87, 84),

            rect.inflate(

                -40,

                -24

            ),

            2

        )





    return lienzo
