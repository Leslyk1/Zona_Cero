"""Carga música y equilibra niveles PCM sin modificar los archivos licenciados."""

from array import array
import json
from pathlib import Path
import warnings

import pygame


# audioop acelera la mezcla en Python 3.12 (versión del proyecto).
# La alternativa conserva compatibilidad cuando ese módulo no está disponible.
try:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        import audioop
except ImportError:
    audioop = None


CARPETA = Path(__file__).resolve().parent / "sonidos"


def cargar_musica(nombre, extension="mp3"):
    sonido = pygame.mixer.Sound(str(CARPETA / (nombre + "." + extension)))
    ajustes = CARPETA / "mezcla.json"
    ganancia = json.loads(ajustes.read_text(encoding="utf-8")).get(nombre, 1.) if ajustes.exists() else 1.
    formato = pygame.mixer.get_init()
    if ganancia == 1 or not formato or formato[1] != -16:
        return sonido
    if audioop is not None:
        pcm = audioop.mul(sonido.get_raw(), 2, ganancia)
    else:
        muestras = array("h", sonido.get_raw())
        pcm = array("h", (max(-32768, min(32767, round(v * ganancia))) for v in muestras)).tobytes()
    return pygame.mixer.Sound(buffer=pcm)
