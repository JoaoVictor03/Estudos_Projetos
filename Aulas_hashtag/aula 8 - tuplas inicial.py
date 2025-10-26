#Tuplas são listas imutáveis
dic_vendas = { #Dicion
    "André": [1000, 500, 300, 5000, 1500, 80, 3000],
    "Andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
    "Alan": [800, 100],
    "Ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180, 100, 120, 110, 130, 140]
}

def calcular_bonus(lista_vendas):
    bonus1 = 2 * len(lista_vendas)
    bonus2 = 0.01 * sum(lista_vendas)
    return bonus1, bonus2 

total_bonus1 = 0
total_bonus2 = 0
#Descobrir o bonus de cada vendedor
for vendedor in dic_vendas:
    bonus1, bonus2 = calcular_bonus(dic_vendas[vendedor])
    print(f"Vendedor: {vendedor}, bônus: {bonus1}")
    total_bonus1 = total_bonus1 + bonus1
    total_bonus2 = total_bonus2 + bonus2

print(f"Total de bônus 1: {total_bonus1}")
print(f"Total de bônus 2: {total_bonus2}")
bonus_total = total_bonus1 + total_bonus2
print("Total de bônus:", bonus_total)