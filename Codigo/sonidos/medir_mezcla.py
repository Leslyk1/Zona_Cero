"""Calcula ganancias conservadoras para las pistas, sin modificar los originales.

Herramienta de preparación: el juego solo lee el pequeño archivo mezcla.json.
Mide RMS y pico PCM; no pretende ser una medición perceptual LUFS.
"""

from array import array
import json
import math
import os
from pathlib import Path


if __name__ == "__main__":
    os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
    import pygame

    pygame.mixer.init(frequency=22050, size=-16, channels=2)
    carpeta = Path(__file__).resolve().parent
    ganancias = {}
    nombres = ("menu.ogg", "refugio.mp3", "calle.mp3", "hospital.mp3",
               "comisaria.mp3", "base_militar.mp3", "sotano.mp3", "combate.mp3")
    for nombre in nombres:
        sonido = pygame.mixer.Sound(str(carpeta / nombre))
        muestras = array("h", sonido.get_raw())
        rms = math.sqrt(sum(v * v for v in muestras) / len(muestras)) / 32768
        pico = max(abs(v) for v in muestras) / 32768
        ganancia = min(8., .12 / max(rms, .001), .85 / max(pico, .001))
        ganancias[Path(nombre).stem] = round(ganancia, 4)
        print(nombre, f"{sonido.get_length():.1f}s RMS={rms:.3f} pico={pico:.3f} ganancia={ganancia:.3f}", flush=True)
    (carpeta / "mezcla.json").write_text(json.dumps(ganancias, indent=2) + "\n", encoding="utf-8")
    pygame.quit()
