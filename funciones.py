from subprocess import call 
from color import Color 

def limpiar():
    call("cls", shell = True)

def Menu_Agregar():
    while True:
        print(Color.CYAN)
        agregar = \
        """
                                                        Agregar Información 
                                                    ----------------------------
                                                    1.
                                                    2.
                                                    3.
                                                    4.
        """ 
        print(agregar)
        print(Color.RESET)
        option = input(f"Eliga la opción que desea: ".rjust(80))
