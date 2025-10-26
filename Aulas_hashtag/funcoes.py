#Funções servem para encapsular um objetivo dentro do código
#Chamamos essas cápsulas de blocos de códigos
lista_preco = [1500, 1000, 800, 2000]
print(lista_preco)

def calcular_imposto(arg_precos):
    imposto_total = 0

    for preco in arg_precos:
        if preco > 1000:
            taxa = 0.15
        else:
            taxa = 0.10
        imposto = preco * taxa
        imposto_total = imposto_total + imposto
    
    return imposto_total

imposto_lista1 = calcular_imposto(lista_preco)
print(imposto_lista1)
print(imposto_lista1)