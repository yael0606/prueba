

mi_lista = [67, 2, 999, 1, 15]
for i in reversed(mi_lista):
    print(i, end=", ")
# corresponde al for pero haciendolo de derecha a izquiera
print(" ")

# esto imprime la lista NO ordenada
print("Lista desordenada: ", mi_lista)

# Ordenemos la lista
mi_lista.sort()
print("Lista Ordenada: ", mi_lista) 
mi_lista.reverse()

# aquí tendremos la lista ordenada
print("Lista Ordenada  Descendente: ", mi_lista) 

