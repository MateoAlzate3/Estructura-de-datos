def resta_circular(matriz):
    return -sum(elemento for fila in matriz for elemento in fila)

# Ejemplo de uso:
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = resta_circular(matriz_ejemplo)
print(resultado)