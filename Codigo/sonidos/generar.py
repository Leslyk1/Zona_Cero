"""Regenera las voces estilizadas y los efectos originales de combate.

La música licenciada se prepara con descargar_musica.py; véase CREDITOS_MUSICA.txt.
Este archivo no reemplaza las piezas musicales del juego.
"""

from array import array
import math
import random
from pathlib import Path
import wave


FRECUENCIA = 22050
CARPETA = Path(__file__).resolve().parent


def frecuencia(nota):
    return 440 * 2 ** ((nota - 69) / 12)


def nota(pista, inicio, duracion, midi, volumen, timbre="suave"):
    base = int(inicio * FRECUENCIA)
    cantidad = min(int(duracion * FRECUENCIA), len(pista) - base)
    hz = frecuencia(midi)
    for i in range(cantidad):
        t = i / FRECUENCIA
        ataque = min(1, t / (.18 if timbre == "suave" else .012))
        salida = min(1, (duracion - t) / .20)
        onda = math.sin(math.tau * hz * t)
        if timbre == "pulso":
            onda = .72 * onda + .20 * math.sin(math.tau * hz * 2 * t)
        elif timbre == "campana":
            onda = (.7 * onda + .3 * math.sin(math.tau * hz * 2.01 * t)) * math.exp(-t * 3)
        pista[base + i] += onda * volumen * ataque * salida


def guardar(nombre, pista):
    # Margen amplio para mezclar música, voces y botones sin saturación.
    pico = max(1, max(abs(v) for v in pista) / .72)
    muestras = array("h", (round(max(-1, min(1, v / pico)) * 32767) for v in pista))
    import sys
    if sys.byteorder != "little":
        muestras.byteswap()
    with wave.open(str(CARPETA / (nombre + ".wav")), "wb") as archivo:
        archivo.setparams((1, 2, FRECUENCIA, 0, "NONE", "not compressed"))
        archivo.writeframes(muestras.tobytes())


def voz(nombre, raiz):
    pista = [0.] * int(1.65 * FRECUENCIA)
    # Sílabas electrónicas con alturas distintas para cada personaje.
    for i, cambio in enumerate((0, 3, 1, 5, 2, -1, 3, 0)):
        inicio = i * .19
        nota(pista, inicio, .13, raiz + cambio, .18, "pulso")
        nota(pista, inicio, .12, raiz + cambio + 12, .04, "campana")
    guardar(nombre, pista)


def efecto(nombre, duracion):
    """Capas de aire, impacto y reflejos cortos, sin notas musicales."""
    pista = []
    azar = random.Random(nombre)
    filtrado = 0.
    for i in range(round(duracion * FRECUENCIA)):
        t = i / FRECUENCIA
        blanco = azar.uniform(-1, 1)
        filtrado += .12 * (blanco - filtrado)
        agudo = blanco - filtrado

        def impacto(inicio, peso=1.):
            dt = t - inicio
            if dt < 0:
                return 0.
            ataque = min(1., dt / .0015)
            cuerpo = math.sin(math.tau * (90 * dt + .9 * (1 - math.exp(-dt * 35))))
            return peso * ataque * (cuerpo * .24 * math.exp(-dt * 32)
                                    + filtrado * .75 * math.exp(-dt * 24)
                                    + agudo * .08 * math.exp(-dt * 80))

        if nombre in ("golpe", "herida"):
            aire = agudo * .075 * math.exp(-((t - .025) / .018) ** 2)
            valor = aire + impacto(.045, 1. if nombre == "golpe" else 1.15)
        elif nombre == "disparo":
            ataque = min(1., t / .0008)
            valor = ataque * (agudo * .43 * math.exp(-t * 100)
                              + filtrado * 1.2 * math.exp(-t * 22)
                              + .23 * math.sin(math.tau * 68 * t) * math.exp(-t * 36))
            valor += agudo * .09 * (math.exp(-((t - .075) / .003) ** 2)
                                    + .6 * math.exp(-((t - .11) / .004) ** 2))
        elif nombre == "defensa":
            valor = min(1., t / .001) * (agudo * .16 * math.exp(-t * 65)
                     + sum(.045 * math.sin(math.tau * hz * t) * math.exp(-t * decaimiento)
                           for hz, decaimiento in ((380, 22), (683, 31), (1147, 40), (1820, 55))))
        elif nombre == "esquive":
            valor = agudo * .19 * math.exp(-((t - .075) / .035) ** 2)
        elif nombre == "vacio":
            valor = agudo * .32 * (math.exp(-((t - .008) / .002) ** 2)
                                    + .45 * math.exp(-((t - .036) / .003) ** 2))
        elif nombre == "victoria":
            valor = impacto(.008, .8) + impacto(.13, .45)
        else:
            valor = impacto(.008, 1.1) + filtrado * .16 * math.exp(-((t - .19) / .07) ** 2)
        pista.append(valor)
    if nombre in ("disparo", "defensa", "golpe", "herida"):
        seco = pista.copy()
        for retardo, nivel in ((.023, .13), (.049, .07), (.085, .035)):
            offset = round(retardo * FRECUENCIA)
            for i in range(offset, len(pista)):
                pista[i] += seco[i - offset] * nivel
    for i in range(len(pista)):
        pista[i] *= min(1., (len(pista) - i) / (FRECUENCIA * .015))
    guardar("efecto_" + nombre, pista)


if __name__ == "__main__":
    voz("elena", 64)
    voz("marcos", 51)
    for nombre, duracion in (("golpe", .32), ("disparo", .44), ("defensa", .30),
                              ("esquive", .23), ("herida", .36), ("victoria", .42),
                              ("derrota", .45), ("vacio", .09)):
        efecto(nombre, duracion)
    print("Generadas 2 voces y 8 efectos breves; sin música.")
