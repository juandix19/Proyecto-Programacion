from subprocess import call 
from color import Color 
import json
import os
import time
import re

"--------------------------MENUS---------------------------------"

def limpiar():
    call("cls", shell = True)

def Menu_Principal(ruta_archivo):
    limpiar()
    while True:
        print(Color.GREEN)
        print("""
                                            *****************************************************************************************
                                                                Programa para el manejo de Estudiantes de Curso
                                            *****************************************************************************************
        """)
        print(Color.RESET)
        print("""                                                                       
                                                                            1. Crear Registros.
                                                                            2. Modificar Registros.  
                                                                            3. Consultar Registros.
                                                                            4. Eliminar Registro.

                                                                            0. <Terminar>
                """)

        print(Color.CYAN)
        option = input("Digite una opción: ")
        print(Color.RESET)
        
        if option == "1":
            limpiar()
            Crear_Registro(ruta_archivo)
        elif option == "2":
            limpiar()
            Modificar_Registro(ruta_archivo)
        elif option == "3":
            limpiar()
            Consultar_Registro(ruta_archivo)
        elif option == "4":
            limpiar()
            Eliminar_Registro(ruta_archivo)
        elif option == "0":
            print("Saliendo del programa...")
            time.sleep(2)
            break
        else:
            limpiar()
            print("❌ Opción inválida, intenta de nuevo.")
            pass



def Verificar_Archivo(ruta_archivo):
    if not os.path.exists(ruta_archivo) or os.stat(ruta_archivo).st_size == 0:  
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            json.dump({}, archivo, indent=4, ensure_ascii=False)


def Crear_Registro(ruta_archivo):

    while True:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            registros = json.load(archivo) 
        llave = input("Ingrese el código del alumno del cual desea crear registro (o escriba '0' para volver): ").strip().upper()
        if llave == '0':
            print("🔙 Volviendo al menú principal...")
            time.sleep(1)
            break
        if not re.match(r"^[ABCDEFGHIJKLMNÑOPQRSTUVWXYZ]{2}\d{2}$", llave, re.ASCII):
            limpiar()
            print("❌ Error: El código debe tener 2 vocales mayúsculas seguidas de 2 números (Ejemplo: AA01).")
            return
        nombre = input("Ingrese el nombre completo en MAYUSCULAS del alumno: ").strip().upper()
        materias = input("Ingrese las materias que está cursando (separadas por coma): ").strip().upper()
        materias = [m.strip().upper() for m in materias.split(',')] 
        estado = input("¿Está activo? (S/N): ").strip().upper()

        if not llave or not nombre or not materias:
            limpiar()
            print("❌ Error: Todos los campos son obligatorios. Intente de nuevo.")
            return
        if estado  in ["s","S"]:
            estado_bool = True
        elif estado in ["n","N"]:
            estado_bool = False
        else:           
            print("❌ Error: Responda con 'S' para activo o 'N' para inactivo.")
            continue
        if llave in registros:
            print("❌ Error: El código ya existe. No se puede duplicar.")
            continue
        registros[llave] = [nombre, materias, estado_bool]
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(registros, archivo, indent=4, ensure_ascii=False)
        time.sleep(2)
        print("✅ Registro creado con éxito")
        input("\n Presione ENTER para volver al menú")
        break   
    limpiar()


def Modificar_Registro(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        registros = json.load(archivo)

    while True:
        llave = input("Ingrese el código del registro que desea modificar (o escriba '0' para volver): ").strip().upper()
        if llave == '0':
            print("🔙 Volviendo al menú principal...")
            time.sleep(1)
            break
        if llave in registros:
            print(f"Datos actuales: {registros[llave]}")
            nombre = input("Nuevo nombre (dejar en blanco para mantener actual): ").strip().upper
            materias = input("Nuevas materias (separadas por coma, dejar en blanco para mantener actual): ").strip().upper()
            estado = input("¿Está activo? (S/N, dejar en blanco para mantener actual): ").strip().upper()
            if nombre:
                registros[llave][0] = nombre
            if materias:
                registros[llave][1] = [m.strip() for m in materias.split(',')]
            if estado:
                registros[llave][2] = estado in ["s","S"]
            with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(registros, archivo, indent=4, ensure_ascii=False)
            time.sleep(2)
            print("✅ Registro modificado con éxito")
            input("\n Presione ENTER para volver al menú")
            break
        if llave not in registros:
            print("⚠️ No se encontró el código ingresado.")
            return 

        
    limpiar()


def Consultar_Registro(ruta_archivo):
        while True:
            llave = input("Ingrese (1) para registro único, (2) para consultar registro general(o escriba '0' para volver): ").strip().upper()
            if llave == '0':
                print("🔙 Volviendo al menú principal...")
                time.sleep(1)
                break
            if llave == "1":
                llave = input("Ingrese el código del registro que desea consultar (o escriba '0' para volver): ").strip().upper()
                with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                    registros = json.load(archivo)
                if llave in registros:
                    print("\n📌 Registro encontrado:")
                    print("\n" + "-" * 80)
                    print(f"\n Datos actuales: {registros[llave]}")
                    print("\n" + "-" * 80)
                    input("\nPresione ENTER para volver al menú principal")
                    print("🔙 Volviendo al menú principal...")
                    time.sleep(2)
                    break
                else:
                    print("❌ Registro no encontrado. Escriba el codigo del registro correctamente:")
                    continue    
        limpiar()


def Eliminar_Registro(ruta_archivo):
    while True:
        llave = input("Ingrese el código del registro que desea eliminar(o escriba '0' para volver): ").strip().upper()
        if llave == '0':
            print("🔙 Volviendo al menú principal...")
            time.sleep(1)
            break
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            registros = json.load(archivo)
        if llave in registros:
            print(f"📌 Registro encontrado: {registros[llave]}")
            confirmacion = input(f"⚠️ ¿Seguro que quieres eliminar {llave}? (S/N): ").strip().lower()
            if confirmacion in ["n","N"]: 
                print("❌ Operación cancelada. El registro NO fue eliminado.")
                input("\nPresione ENTER para volver al menú.")
                return
            time.sleep(2)
            del registros[llave]
            with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(registros, archivo, indent=4, ensure_ascii=False)
            print("✅ Registro eliminado con éxito")
            input("\n Presione ENTER para volver al menú principal")
            break 
        else:
            print("❌ Código no encontrado. Escriba el codigo correctamente:") 
            continue   
    limpiar()


if __name__ == '__main__':
    limpiar()
    carpeta = "datos"
    Archivo_Json = os.path.join(carpeta, "alumnos.json")
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    Verificar_Archivo(Archivo_Json)
    Menu_Principal(Archivo_Json)