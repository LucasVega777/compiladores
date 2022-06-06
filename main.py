from modulos.archivos import Archivo
from modulos.regex import Regex
from modulos.traductor import traducir
if(__name__ == '__main__'):
    try:
        lexer = Regex()
        archivo = Archivo()
        codigo = archivo.leer()
        lexema = lexer.getLexema(codigo)
        archivo.escribir(lexema)
        print("Archivo output.txt generado exitosamente. :)")
        traducir(lexer.tablaTraduccion)
    except Exception as error:
        print(error)