# from archivos import Archivo


# archivo = Archivo("output.txt")
# archivo2 = Archivo()
# print(archivo.leer().split())
# print(archivo2.leer().split("\n"))
# lista_ignorar = ["L_LLAVE"]

# for token in archivo.leer().split():
#     pass


def traducir(tabla):
    xml = ""
    elemento_de_lista = False
    es_clave = False
    reemplazar = False 
    for elemento in tabla:
        print(elemento)
        if(elemento.token == "{"):
            es_clave = True
        elif(elemento.token == "["):
            elemento_de_lista = True
        elif(elemento.token == "{" and elemento_de_lista):
            xml += "<item>"
        elif():
            xml += "<" + elemento.token + ">" + "[VALUE]" + "</" + elemento.token + ">"
        elif(elemento.token == "}" and elemento_de_lista):
            xml += "</item>"
            elemento_de_lista = False
        elif():
            pass

        print(xml)

# def concatenarXML(elemento):
#     return "<" + elemento.token + ">" + "</" + elemento.token + ">"

# def concatenarLista():
#     return "<item>" + concatenarElemento() + "</item>"

# def concatenarElemento(elementos):
#     return "<item>" + concatenarElemento() + "</item>"

