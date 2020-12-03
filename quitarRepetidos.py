def eliminarRepetidos(lista):
    salida = list(set(lista))
    salida.sort()
    return salida


print(eliminarRepetidos([0, 1, 2, 3, 4, 4, 4, 4, 4, 2, 25, 100, 1254,
                         255, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 105487451, 105487451, -5, -8, -10, -58]))
