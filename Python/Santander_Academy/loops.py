'''frutas = ["Maça", "Banana", "Morango"]

for fruta in frutas:
    print(fruta)

print("\n")

#Loop while
contador = 0


while True:

    print(contador)
    contador += 1

    if contador == 10000:
        break
    print(contador)'''

for i in range(10):
    if i % 2 == 0:
        continue #Pula o bloco para a próxima etapa
    print(i)