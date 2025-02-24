from subprocess import call 
from color import Color 
import json
import os.path 
import time
import re
def centrar_input(mensaje, ancho_terminal = 117):
    espacios = (ancho_terminal - len(mensaje))  
    return input(" " * espacios + mensaje + Color.RESET)


def Verificar_Archivo(ruta_archivo):
    if not os.path.exists(ruta_archivo) or os.stat(ruta_archivo).st_size == 0:  
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            json.dump({}, archivo, indent=4, ensure_ascii=False)


def Mostrar_Registro(llave, datos):
    nombre, materias, estado = datos
    estado_str = "Activo" if estado else "Inactivo"
    return (f"📌 Código: {llave} \n 🔹 Nombre: {nombre} \n 📚 Materias: {materias} \n 🟢 Estado: {estado_str}")

def anuncios_bold(texto):
    texto in [""]
    return (Color.BOLD + texto + Color.RESET)