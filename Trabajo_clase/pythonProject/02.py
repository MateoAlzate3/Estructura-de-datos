lista = [1,2,2,3,4,4,5,6,6,7,9,9]

def eliminar(lista):
    resultado = []
    for i in lista:
        if i not in resultado:
            resultado.append(i)
    return resultado

resultado = eliminar(lista)
print(resultado)