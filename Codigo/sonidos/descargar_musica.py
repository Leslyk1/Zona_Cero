"""Descarga las pistas licenciadas; solo se ejecuta para preparar los recursos.

El juego funciona sin conexión. Véase CREDITOS_MUSICA.txt para autores y licencias.
No extrae archivos arbitrarios de los ZIP: copia únicamente el audio seleccionado.
"""

from io import RawIOBase
from pathlib import Path
from urllib.request import Request, urlopen
from zipfile import ZipFile


CARPETA = Path(__file__).resolve().parent
BASE = "https://opengameart.org/sites/default/files/"
PISTAS = {
    "calle.mp3": "The%20Surreal%20Truth.mp3",
    "hospital.mp3": "Final%20Captain%27s%20Log.mp3",
    "comisaria.mp3": "Cage%20of%20the%20Cryptid.mp3",
    "base_militar.mp3": "Infestation%20in%20the%20Control%20Room.mp3",
    "sotano.mp3": "The%20Depths%20of%20Hell.mp3",
}
PAQUETES = {
    "refugio.mp3": ("safe_room_wav_and_mp3.zip", "Sala_segura_soundtrack.mp3"),
    "menu.ogg": ("ambient_horror_track_01_0.zip", ".ogg"),
    "combate.mp3": ("Zander%20Noriega%20-%20Perpetual%20Tension.zip", ".mp3"),
}


def descargar(nombre):
    with urlopen(BASE + nombre, timeout=60) as respuesta:
        return respuesta.read()


class ArchivoRemoto(RawIOBase):
    """Lee rangos del ZIP para descargar el MP3/OGG sin traer también el WAV."""

    def __init__(self, nombre):
        self.url = BASE + nombre
        with urlopen(Request(self.url, headers={"Range": "bytes=-65536"}), timeout=60) as respuesta:
            if respuesta.status != 206:
                raise OSError("El servidor no admite descargas parciales")
            self.tamano = int(respuesta.headers["Content-Range"].split("/")[-1])
            self.cola = respuesta.read()
        self.posicion = 0

    def seek(self, offset, whence=0):
        self.posicion = offset if whence == 0 else self.posicion + offset if whence == 1 else self.tamano + offset
        return self.posicion

    def tell(self):
        return self.posicion

    def read(self, cantidad=-1):
        fin = self.tamano if cantidad < 0 else min(self.tamano, self.posicion + cantidad)
        if fin <= self.posicion:
            return b""
        inicio_cola = self.tamano - len(self.cola)
        if self.posicion >= inicio_cola:
            datos = self.cola[self.posicion - inicio_cola:fin - inicio_cola]
        else:
            rango = f"bytes={self.posicion}-{fin - 1}"
            with urlopen(Request(self.url, headers={"Range": rango}), timeout=60) as respuesta:
                if respuesta.status != 206:
                    raise OSError("Respuesta parcial no válida")
                datos = respuesta.read()
        self.posicion += len(datos)
        return datos


if __name__ == "__main__":
    for destino, origen in PISTAS.items():
        if (CARPETA / destino).exists():
            continue
        (CARPETA / destino).write_bytes(descargar(origen))
        print("Descargada:", destino, flush=True)
    for destino, (origen, seleccion) in PAQUETES.items():
        if (CARPETA / destino).exists():
            continue
        with ZipFile(ArchivoRemoto(origen)) as paquete:
            candidatos = [n for n in paquete.namelist()
                          if (n == seleccion if not seleccion.startswith(".") else n.lower().endswith(seleccion))
                          and not n.startswith("__MACOSX/")]
            if len(candidatos) != 1:
                raise ValueError(f"Selección de audio ambigua en {origen}: {candidatos}")
            (CARPETA / destino).write_bytes(paquete.read(candidatos[0]))
        print("Preparada:", destino, flush=True)
