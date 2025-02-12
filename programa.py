from subprocess import call 
from color import Color 
import json
import os
import time

"--------------------------MENUS---------------------------------"

def limpiar():
    call("cls", shell = True)

def Menu_Principal(ruta_archivo):
    limpiar()
    while True:
        print(Color.CYAN)
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

        option = input("Digite una opción: ")

        if option == "1":
            Crear_Registro(ruta_archivo)
        elif option == "2":
            Modificar_Registro(ruta_archivo)
        elif option == "3":
            Consultar_Registro(ruta_archivo)
        elif option == "4":
            Eliminar_Registro(ruta_archivo)
        elif option == "0":
            print("Saliendo del programa...")
            time.sleep(2)
            break
        else:
            print("❌ Opción inválida, intenta de nuevo.")
            input("\nPresiona ENTER para continuar...")  



def Verificar_Archivo(ruta_archivo):
    if not os.path.exists(ruta_archivo) or os.stat(ruta_archivo).st_size == 0:  
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            json.dump({}, archivo, indent=4, ensure_ascii=False)


def Crear_Registro(ruta_archivo):
    llave = input("Ingrese el código del estudiante (Ejemplo: AA01): ").strip().upper()
    nombre = input("Ingrese el nombre completo en MAYUSCULAS del alumno: ").strip()
    materias = input("Ingrese las materias que está cursando (separadas por coma): ").strip()
    materias = [m.strip() for m in materias.split(',')] 
    estado = input("¿Está activo? (S/N): ").strip().lower()

    while True:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            registros = json.load(archivo)
        if not llave or not nombre or not materias:
            print("❌ Error: Todos los campos son obligatorios. Intente de nuevo.")
            continue
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
        # registros = {llave: [nombre, materias, estado_bool]}
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(registros, archivo, indent=4, ensure_ascii=False)
        time.sleep(2)
        print("✅ Registro creado con éxito")
        input("\n Presione ENTER para volver al menú")
        break   
    limpiar()


def Modificar_Registro(ruta_archivo):
    llave = input("Ingrese el código del estudiante a modificar: ").strip().upper()
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        registros = json.load(archivo)

    while True:
        if llave in registros:
            print(f"Datos actuales: {registros[llave]}")
            nombre = input("Nuevo nombre (dejar en blanco para mantener actual): ").strip()
            materias = input("Nuevas materias (separadas por coma, dejar en blanco para mantener actual): ")
            estado = input("¿Está activo? (S/N, dejar en blanco para mantener actual): ").strip().lower()
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
            llave = input("Ingrese el código del alumno a consultar: ").strip()
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                registros = json.load(archivo)

            if llave in registros:
                print("\n📌 Registro encontrado:")
                print(f"\n Datos actuales: {registros[llave]}")
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
        llave = input("Ingrese el código del alumno a eliminar: ").strip().upper()
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