from subprocess import call 
from color import Color 
import os.path 
FILE_NAME = os.path.join(os.path.dirname(__file__), "alumnos.json")
import time
import funciones as f
import archivo as d

"--------------------------MENUS---------------------------------"


def Menu_Principal(ruta_archivo):
    f.limpiar()
    while True:
        print(Color.WHITE + """\n\n
                                                            *****************************************************************************************""" + Color.PINK + """
                                                                                Programa para el manejo de estudiantes de Curso   """ + Color.WHITE +  """
                                                            *****************************************************************************************
                        """
                        + Color.WHITE + """                                                                       
                                                                                            1. Crear Registros.
                                                                                            2. Modificar Registros.  
                                                                                            3. Consultar Registros.
                                                                                            4. Eliminar Registro.

                                                                                            0. <Terminar>
              
                """)

        option = d.centrar_input(Color.CYAN + "Digite una opción: ")
        if option == "1":
            f.limpiar()
            f.Crear_Registro(ruta_archivo)
        elif option == "2":
            f.limpiar()
            f.Modificar_Registro(ruta_archivo)
        elif option == "3":
            f.limpiar()
            f.Consultar_Registro(ruta_archivo)
        elif option == "4":
            f.limpiar()
            f.Eliminar_Registro(ruta_archivo)
        elif option == "0":
            print("Saliendo del programa...")
            time.sleep(2)
            f.limpiar()
            break
        else:
            f.limpiar()
            print("❌ Opción inválida, escriba las opciones que aparecen en el menú.")
            pass


if __name__ == '__main__':
    f.limpiar()
    carpeta = "datos"
    Archivo_Json = os.path.join(carpeta, "alumnos.json")
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    d.Verificar_Archivo(Archivo_Json)
    Menu_Principal(Archivo_Json)
