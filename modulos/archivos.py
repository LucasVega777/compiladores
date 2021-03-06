"""
Modulo donde se abstraen las funciones de lectura
y escritura de archivos.
"""


class Archivo():
    """
    Clase que abstrae la lectura y escritura de archivos
    """

    def __init__(self, entrada="./analizadorLexico/fuentes/fuente.txt", salida="./output.txt"):
        self.entrada = entrada
        self.salida = salida


    def leer(self):
        """
        Metodo que retorna el contenido de un archivo.
        """
        archivo = open(self.entrada)
        res = archivo.readlines()
        return ''.join(res)


    def escribir(self, cadena):
        """
        Metodo que escribe la cadena recibida en el archivo.
        """
        with open(self.salida, 'w') as file:
            file.write(cadena)

            

