from modulos.archivos import Archivo
from modulos.regex import Regex
from modulos.traductor import traducir
from modulos.analizadorSintactico import analizador

if(__name__ == '__main__'):
    try:
        lexer = Regex()
        archivo = Archivo()
        codigo = archivo.leer()
        lexema = lexer.getLexema(codigo)
        archivo.escribir(lexema)
        print("Archivo output.txt generado exitosamente. :)")
        traducido = traducir(lexer.tablaTraduccion)
        archivoTraducido = Archivo(salida="output.xml")
        archivoTraducido.escribir(traducido)
    except Exception as error:
        print(error)
        raise error
    else:
       analizador(codigo)