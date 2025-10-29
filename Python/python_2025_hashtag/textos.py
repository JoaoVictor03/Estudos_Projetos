email = "joaovictor.fasp@gmail.com"

print(email)
print(len(email))

posicao = email.find("@")
print(posicao)
print(email[11:]) #pegar da posição 11 até o final
print("Servidor:", email[11:])

#Trocar um pedaço do texto

novo_email = email.replace("@gmail.com", "@yahoo.com")
print(novo_email)


#Capitalizar para colocar a primeira letra em maiúscula
nome = "joão victor"
novo_nome = nome.capitalize() #capitalize coloca a primeira letra em maiúscula
print(novo_nome)
novo_nome = nome.title()
print(novo_nome)