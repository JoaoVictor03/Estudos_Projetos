#Conjuntos -> Estruturas de dados mutáveis, não ordenados para armazenar valores únicos
#Lembre de teorias dos conjuntos do Ensindo fundamental
conjunto1 = {1, 2, 3}
conjunto2 = {2, 3, 4}

conjunto3 = conjunto1 | conjunto2 #União
conjunto3 = conjunto1 & conjunto2 #Interseção
conjunto3 = conjunto1 - conjunto2 #Diferença
print(conjunto3)

#métodos
'''
add(elemento)
remove(elemento)
discard(elemento)
clear() -> remove todos os elementos
'''
