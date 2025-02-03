from subprocess import call 
from color import Color 
from funciones import Menu_Agregar 

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

        if option == "1.":
            Menu_Agregar()
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