import os

class Utils() :
    """ Esta clase contiene funciones de utilidad """
    def limpiar_consola():
        """ Funcion que limpia la consola """
        # Detecta el sistema operativo y ejecuta el comando adecuado
        if os.name == 'nt':  # 'nt' indica Windows
            os.system('cls')
        else:  # 'posix' indica Unix, Linux o MacOS
            os.system('clear')

    def vacio(x: str) -> bool: #TODO - Terminar de hacer
        """ Funcion que retorna si el valor pasado por parametro esta vacio """
        return x != ""
    
    def sepearador_decorativo_consola() -> str : 
        return "\n" + "~" * 10 + " * " * 5 + "~" * 10 + "\n"