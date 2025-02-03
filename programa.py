from subprocess import call 
from color import Color 

"--------------------------MENUS---------------------------------"
def limpiar():
    call("cls", shell = True)

def Menu_Principal():
    while True:
        print(Color.CYAN)
        menu = \
        """
                                                                Menu Principal 
                                                        ----------------------------
                                                        1. Agregar información.
                                                        2. Modificar información. 
                                                        3. Eliminar inoformación. 
                                                        4. Consultar información
                                                        5. Salir
        """
        print((menu))
        print(Color.RESET)
        option = input(f"Eliga la opción que desea: ".rjust(80))