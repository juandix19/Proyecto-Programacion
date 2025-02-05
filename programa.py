from subprocess import call 
from color import Color 
# from funciones import Crear_Registro 
import json
import os 


"--------------------------MENUS---------------------------------"


def limpiar():
    call("cls", shell = True)


def Menu_Principal():
    while True:
        print(Color.CYAN)
        lineas = \
        """
        ***************************************************************************************************************************************************************
                                             Programa para el manejo de Estudiante de Curso
        ***************************************************************************************************************************************************************
        """
        menu = \
        """

                                                        1. Crear Registros.
                                                        2. Modificar Registros.  
                                                        3. Consultar Registros.
                                                        4. Eliminar Registro.

                                                        0. <Terminar>
        """
        print(lineas)
        print(Color.WHITE)
        print((menu))
        print(Color.BLUE)
        option = input(f"Digite una opción: ".rjust(80))

        if option == "1":
            Crear_Registro(ruta_archivo)
        # elif option == "2.":
        #     pass
        # elif option == "3.":
        #     pass
        # elif option == "4.":
        #     pass
        # elif option == "5.":
        #     pass


# def Verificar_archivo(ruta_archivo):
#     if not os.path.exist(ruta_archivo):
#         with open(ruta_archivo,'w', encoding='utf-8')as archivo:
#             json.dump([],archivo, indent=4, ensure_ascii=False)


def Crear_Registro(ruta_archivo):

    nombre = input("Nombre:")
    materia = input("Materia que está cursando")
    activo = input("Actividad del estudiante")

    nuevo_registro = {
        "nombre" : nombre,
        "materia" : materia,
        "activo" : activo
    }
    with open(ruta_archivo,'r',encoding='utf.8')as archivo:
        registros =json.load(archivo)
    registros.append(nuevo_registro) 

    with open(ruta_archivo,'w',encoding='utf.8')as archivo:      
        json.dump(registros,archivo,indent=4,ensure_ascii=False)
    print("VAMOOOS")


if __name__ == '__main__':
    limpiar()