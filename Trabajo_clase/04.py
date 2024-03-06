lista1 = [1,2,3,4]
lista2 = [5,6,2,8]

def elemento_comun(lista1, lista2):
    for elemento in lista1:
        if elemento in lista2:
            return True

    return False

resultado = elemento_comun(lista1,lista2)
print(resultado)

