from modulos.archivos import Archivo
from modulos.regex import Regex

if(__name__ == '__main__'):
    try:
        lexer = Regex()
        archivo = Archivo()
        codigo = archivo.leer()
        lexema = lexer.getLexema(codigo)
        archivo.escribir(lexema)
    except Exception as error:
        print(error)