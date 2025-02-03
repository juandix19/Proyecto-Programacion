from subprocess import call 
from color import Color 
from funciones import Crear_Registro

"--------------------------MENUS---------------------------------"
def limpiar():
    call("cls", shell = True)

def Menu_Principal():
    while True:
        print(Color.CYAN)
        menu = \
        """
*********************************************************************************************************************************************************************
                                            Programa para el Manejo de Estudiante del Curso
*********************************************************************************************************************************************************************

                                                        1. Crear Registros.
                                                        2. Modificar Registros.  
                                                        3. Consultar Registros.
                                                        4. Eliminar Registro.

                                                        0. <Terminar>a
        """
        print((menu))
        print(Color.WHITE)
        option = input(f"Digite una opción: ".rjust(80))

        if option == "1.":
            Crear_Registro()
            pass
        elif option == "2.":
            pass
        elif option == "3.":
            pass
        elif option == "4.":
            pass
        elif option == "5.":
            pass



if __name__ == '__main__':
    limpiar()
    Menu_Principal()