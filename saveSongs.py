import json
import os
from pathlib import Path

ARCHIVO_CANCIONES = str(Path.home() / ".musica_historica.json")

def guardar_canciones(lista_canciones):
    with open(ARCHIVO_CANCIONES, "w", encoding="utf-8") as f:
        json.dump(lista_canciones, f, indent=2, ensure_ascii=False)

def cargar_canciones():
    if os.path.exists(ARCHIVO_CANCIONES):
        with open(ARCHIVO_CANCIONES, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []
