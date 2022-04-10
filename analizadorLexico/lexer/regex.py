import re


"""
    Clase Regex que inicializa los lexemas a evaluar.
"""
class Regex:
    
    def __init__(self):
        self.componentesLexicos = [
            ("L_CORCHETE", r"/[/g"),
            ("R_CORCHETE", r"/]/g"),
            ("L_LLAVE", r"/{/g"),
            ("R_LLAVE", r"/}/g"),
            ("COMA", r"/,/g"),
            ("DOS_PUNTOS", r"/:/g"),
            ("LITERAL_CADENA", r"/[\".*\"]/g"), # Cadena
            ("LITERAL_NUM", r"/[0-9]+(\.[0-9]+)?((e|E)(+|-)?[0-9]+)?/g"), # Numeros
            ("PR_TRUE", r"/true|TRUE/g"),
            ("PR_FALSE", r"/false|FALSE/g"),
            ("PR_NULL", r"/null|NULL/g"),     
            ("EOF", r"/''/g")
        ]


    """
        Recorre el array de tuplas en donde estan definidos
        los lexemas, y por cada token recibido, verifica 
        su expresion regular.
    """
    def getLexema (self, token):
        errors = []
        try:
            token_regex = '|'.join('(?P<%s>%s)' % par for par in self.componentesLexicos)
            numero_linea = 1 # Numero de linea
            numero_inicio = 0 # Inicio de la lìnea
            for componente in re.finditer(token_regex, token):
                # componente[0]: Nombre del lexema
                # componente[1]: Expresion regular
                regex = re.compile(componente[1])

                if(regex.fullmatch(token)):
                    print(componente[0])
        except:
            print('hola')
                
