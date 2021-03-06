from typing import NamedTuple
import re


class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int


class Regex:
    """
    Clase Regex que inicializa los lexemas a evaluar.
    """
    
    def __init__(self):
        self.componentesLexicos = [
            ("NEW_LINE", r'\n'),
            ("L_CORCHETE", r'\['),
            ("R_CORCHETE", r']'),
            ("L_LLAVE", r'{'),
            ("R_LLAVE", r'}'),
            ("COMA", r','),
            ("DOS_PUNTOS", r':'),
            ("LITERAL_CADENA", r'(?P<quote>[\'"]).*?(?P=quote)'), # Cadena 
            ("LITERAL_NUM", r'[0-9]+(\.[0-9]+)?((e|E)(\+|-)?[0-9]+)?'), # Numeros
            ("PR_TRUE", r'true|TRUE'),
            ("PR_FALSE", r'false|FALSE'),
            ("PR_NULL", r'null|NULL'),
            ("SKIP", r'[ \t]+'),
            ("ESPACIO", r' ')
        ]
        self.tablaTraduccion = []

    
    def getLexema (self, codigo):
        """
        Recorre el array de tuplas en donde estan definidos
        los lexemas, y por cada token recibido, verifica 
        su expresion regular.
        """
        errors = []
        resultado = ""
        tipos = [e[0] for e in self.componentesLexicos]
        try:
            token_regex = '|'.join('(?P<%s>%s)' % par for par in self.componentesLexicos)
            numero_linea = 1 # Numero de linea
            inicio_linea = 0 # Inicio de la lìnea
           
            for token in re.finditer(token_regex, codigo):
                temporal = {}
                tipoLexema = token.lastgroup
                valorLexema = token.group()
    
                if(tipoLexema == "NEW_LINE"):
                    numero_linea += 1
                    inicio_linea = token.end()
                    resultado += "\n"
                    temporal = {
                        "tipoLexema": tipoLexema,
                        "resultado": "\n",
                        "token" : valorLexema
                    }
                    self.tablaTraduccion.append(temporal)
                    continue
                elif(tipoLexema == "LITERAL_CADENA"):
                    resultado += "STRING" + " "
                    temporal = {
                        "tipoLexema": tipoLexema,
                        "resultado": "\n",
                        "token" : valorLexema
                    }
                    self.tablaTraduccion.append(temporal)
                    continue
                elif(tipoLexema == "LITERAL_NUM"):
                    resultado += "NUMBER" + " "
                    temporal = {
                        "tipoLexema": tipoLexema,
                        "resultado": "\n",
                        "token" : valorLexema
                    }
                    self.tablaTraduccion.append(temporal)
                    continue
                elif(tipoLexema == "SKIP"):
                    resultado += "\t"
                    temporal = {
                        "tipoLexema": tipoLexema,
                        "resultado": "\t",
                        "token" : valorLexema
                    }
                    self.tablaTraduccion.append(temporal)
                    continue
                elif(tipoLexema in tipos):
                    resultado += tipoLexema + " "
                    temporal = {
                        "tipoLexema": tipoLexema,
                        "resultado": tipoLexema, 
                        "token" : valorLexema
                    }
                    self.tablaTraduccion.append(temporal)
                    continue
                else:
                    errors.append('Error {} no reconocido en la linea {}'.format(valorLexema, numero_linea))
            
            if(len(errors) > 0):
                raise('Ocurrieron los siguientes errores: ' + '\n'.join(errors))
            else:
                print(resultado)
                return resultado   
        except Exception as error:
            print(error)