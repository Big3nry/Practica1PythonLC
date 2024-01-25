lista_original = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
lista_modificada = [x for (i, x) in enumerate(lista_original) if i not in (0, 4, 5)]
print(lista_modificada)