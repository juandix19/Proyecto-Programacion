from subprocess import call 
from color import Color 

def limpiar():
    call("cls", shell = True)

def Crear_Registro():
    while True:
        print(Color.CYAN)
        agregar = \
        """
                                                        Crear Registro
                                                    ----------------------------
                                                    1.
                                                    2.
                                                    3.
                                                    4.
        """ 
        print(agregar)
        print(Color.RESET)
        option = input(f"Eliga la opción que desea: ".rjust(80))
