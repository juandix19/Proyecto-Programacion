from subprocess import call 
from color import Color 
import json
import os.path 
import time
import re

"--------------------------MENUS---------------------------------"

def limpiar():
    call("cls", shell = True)

def Menu_Principal(ruta_archivo):
    limpiar()
    while True:
        print(Color.WHITE + """
                                                                *****************************************************************************************""" + Color.GREEN + """
                                                                                    Programa para el manejo de estudiantes de Curso   """ + Color.WHITE +  """
                                                                *****************************************************************************************
                            """
                            + Color.WHITE + """                                                                       
                                                                                                1. Crear Registros.
                                                                                                2. Modificar Registros.  
                                                                                                3. Consultar Registros.
                                                                                                4. Eliminar Registro.
7
                                                                                                0. <Terminar>
              
                """)

        option = centrar_input(Color.CYAN + "Digite una opción: ")
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
            limpiar()
            break
        else:
            limpiar()
            print("❌ Opción inválida, escriba las opciones que aparecen en el menú.")
            pass

def centrar_input(mensaje, ancho_terminal = 120):
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


def Crear_Registro(ruta_archivo):
    while True:
        print(Color.WHITE + """ 
                                                                ***************************************************************************************** """ + Color.ORANGE + """
                                                                                                    Crear Registros                               """ + Color.WHITE + """
                                                                *****************************************************************************************
                                        """
                                        """
                                                                                            1. Crear un nuevo registro. 
                                                                                            0. <Volver al menú principal> 
                                                                            """)
        llave = centrar_input(Color.YELLOW + "Digite una opción: ")
        if llave == '0':
            print("🔙 Volviendo al menú principal...")
            time.sleep(1)
            break        
        if llave == '1':
            limpiar()
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                registros = json.load(archivo) 
            while True:
                llave = input(Color.MAGENTA + "\n\nIngrese el código del alumno del cual desea crear un registro o escriba '0' para volver*: " + Color.RESET).strip().upper()
                if llave == '0':
                    print("\n\n🔙 Volviendo al menú anterior...")
                    time.sleep(1) 
                    limpiar()   
                    break
                if not re.fullmatch(r"^[ABCDEFGHIJKLMNÑOPQRSTUVWXYZ]{2}\d{2}$", llave):
                    print("❌ Error: El código debe cotener 2 letras mayúsculas seguidas de 2 números (Ejemplo: AA01).")
                    continue
                nombre = input("Ingrese el nombre completo del alumno*: ").strip().upper()
                materias = input("Ingrese las materias que está cursando separadas por coma: ").strip().upper()
                if not materias:
                    materias = "ACTUALMENTE EL ALUMNO NO ESTÁ CURSANDO ALGUNA MATERIA"
                else:
                    materias = [m.strip() for m in materias.split(',')]
                estado = input("¿Está activo? (S/N)*: ").strip().upper()
                if not estado or not nombre:
                    print("❌ Error: Debe introducir todos los datos obligatorios. Intente de nuevo.")
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
                with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
                    json.dump(registros, archivo, indent=4, ensure_ascii=False)
                time.sleep(2)
                print("✅ Registro creado con éxito")
                input("\n Presione ENTER para volver al menú principal ")
                break 
        else:
            limpiar()
            print("❌ Opción inválida, escriba las opciones que aparecen en el menú.")
            pass
    limpiar()


def Modificar_Registro(ruta_archivo):
    while True:
        print(Color.WHITE + """ 
                                                                ***************************************************************************************** """ + Color.ORANGE + """
                                                                                                Modificar Registros                              """ + Color.WHITE + """
                                                                *****************************************************************************************
                                        """
                                        """
                                                                                            1. Modificar datos de un registro. 
                                                                                            0. <Volver al menú principal>
                                                                            
              """)
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            registros = json.load(archivo)
        llave = centrar_input(Color.YELLOW + "Digite una opción: ")
        if llave == '0':
            print("🔙 Volviendo al menú principal...")
            time.sleep(1)
            break  
        if llave == '1':
            limpiar()
            while True:
                llave = input(Color.PINK + "\n\nIngrese el código del registro que desea modificar o escriba 0 para volver: " + Color.RESET).strip().upper()
                if llave == "0":
                    print("\n\n🔙 Volviendo al menú anterior...")
                    time.sleep(1) 
                    limpiar()   
                    break
                if llave in registros: 
                    print("\n📋Datos actuales del registro:" + f"\n\n {Mostrar_Registro(llave, registros[llave])}" + "\n")
                    answer = input("\n¿Desea modificar este registro? (A) para modificar y (D) para modificar otro registro: ")
                    if answer == "D":
                        time.sleep(1/2)
                        continue
                    if answer == "A":
                        nuevo_nombre = input("Nuevo nombre (dejar en blanco para mantener actual): ").strip().upper() or registros[llave][0]
                        nuevas_materias = input("Nuevas materias (separadas por coma, dejar en blanco para mantener actual): ").strip().upper()
                        if nuevas_materias:
                            nuevas_materias = [m.strip() for m in nuevas_materias.split(',')]
                        else:
                            nuevas_materias = registros[llave][1]
                        nuevo_estado = input("¿Está activo? (S/N, dejar en blanco para mantener actual): ").strip().upper()
                        estado_bool = nuevo_estado == "S" if nuevo_estado else registros[llave][2]
                        print("\n\n📝 Así se modifarán los datos: ")
                        print(f"🔹 Nombre: {nuevo_nombre}")
                        print(f"🔹 Materias: {', '.join(nuevas_materias) if nuevas_materias else 'Sin materias'}")
                        print(f"🔹 Estado: {'Activo' if estado_bool else 'Inactivo'}\n")
                        confirmación = input("¿Confirmar modificación? (S/N): ").strip().upper()
                        if confirmación == "S":
                            registros[llave] = [nuevo_nombre, nuevas_materias, estado_bool]
                            with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
                                json.dump(registros, archivo, indent=4, ensure_ascii=False)
                            time.sleep(2)
                            print("✅ Registro modificado con éxito")
                            input("\n Presione ENTER para volver al menú ")
                            break
                        else:
                            print("❌ Modificación cancelada. Volviendo a la selección del registro...")
                            time.sleep(2)
                            limpiar()
                            continue
                else:
                    limpiar()
                    print("\n\n⚠️ No se encontró el código ingresado, intente de nuevo")
                    time.sleep(1/2)
                    continue
    limpiar()


def Consultar_Registro(ruta_archivo):
        while True:
            llave = centrar_input(Color.YELLOW + "Ingrese (1) para registro único, (2) para consultar registro general(o escriba '0' para volver): ").strip().upper()
            if llave == '0':
                print("🔙 Volviendo al menú principal...")
                time.sleep(1)
                break
            if llave == "1":
                llave = centrar_input( "Ingrese el código del registro que desea consultar (o escriba '0' para volver): ").strip().upper()
                with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                    registros = json.load(archivo)
                if llave == '0':
                    print("🔙 Volviendo al menú principal...")
                    time.sleep(1)
                    break    
                if llave in registros:
                    print("\n📋Registro encontrado:" + f"\n\n {Mostrar_Registro(llave, registros[llave])}" + "\n")
                    input("\nPresione ENTER para volver al menú principal ")
                    print("🔙 Volviendo al menú principal...")
                    time.sleep(2)
                    break
                else:
                    print("❌ Registro no encontrado. Escriba el codigo del registro correctamente:")
                    continue 
            elif llave == "2":
                time.sleep(1)
                with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                    registros: dict = json.load(archivo)
                if not registros:
                    print("📂 No hay registros guardados.")
                    continue
                else:
                    print("\n📋 REGISTRO GENERAL:")
                    print("-" * 200)
                    for codigo, datos in registros.items():
                        nombre, materias, estado = datos
                        estado_str = "Activo" if estado else "Inactivo"
                        print(f"📌 Código: {codigo} \n 🔹 Nombre: {nombre} \n 📚 Materias: {materias} \n 🟢 Estado: {estado_str}")
                        print("-" * 200)
                input("\nPresione ENTER para volver al menú principal ")
                print("🔙 Volviendo al menú principal...")
                time.sleep(2)
                break 
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
            print("\n 📋Registro encontrado:" + f"\n\n{Mostrar_Registro(llave, registros[llave])}" + "\n")
            confirmacion = input(f"⚠️ ¿Seguro que quieres eliminar {llave}? (S/N): ").strip().lower()
            if confirmacion in ["n","N"]: 
                print("❌ Operación cancelada. El registro NO fue eliminado.")
                input("\nPresione ENTER para volver al menú principal ")
                break
            time.sleep(2)
            del registros[llave]
            with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(registros, archivo, indent=4, ensure_ascii=False)
            print("✅ Registro eliminado con éxito")
            input("\n Presione ENTER para volver al menú principal ")
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
