import os
import json


def cargar_json(path):
    """
    Carga un archivo JSON desde el path dado.
    Si el archivo no existe, devuelve un diccionario vacío.
    """
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"⚠️ Error al decodificar el JSON en: {path}")
            return {}
    else:
        print(f"⚠️ Archivo no encontrado: {path}")
        return {}


def cargar_lista_json(path):
    """
    Carga un archivo JSON que contiene una lista.
    Si el archivo no existe o no es una lista, devuelve una lista vacía.
    """
    data = cargar_json(path)
    if isinstance(data, list):
        return data
    else:
        return []