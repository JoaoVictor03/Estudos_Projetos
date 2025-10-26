#Funções servem para encapsular um objetivo dentro do código
#Chamamos essas cápsulas de blocos de códigos
lista_preco = [1500, 1000, 800, 2000]
print(lista_preco)

#função para calcular a taxa
def calcular_imposto(lista_valores):
    imposto_total = 0

    for preco in lista_valores:
        taxa = calcular_taxa(preco)
        imposto = preco * taxa
        imposto_total = imposto_total + imposto
    
    return imposto_total
def calcular_taxa(preco):
    if preco > 1000:
        taxa = 0.15
    else:
        taxa = 0.10
    return taxa #Exporta a taxa para fora da função

imposto_lista1 = calcular_imposto(lista_preco)
print(imposto_lista1)
print(imposto_lista1)

#variáveis locais - só existem dentro do bloco
''' Para poder "exportar" o valor de uma variável para fora da função,
é necessário usar o Return'''