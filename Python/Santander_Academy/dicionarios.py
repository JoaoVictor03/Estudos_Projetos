#Dicionarios são estruturas de dados mutáveis, não ordenados e separados por chave : valor
#São delimitados por chaves {}
#Exemplo: armazenar informações de um aluno
aluno = {"Nome":"João", "Idade":22, "Formação":"Engenharia"}
print(aluno["Nome"])
print(aluno["Formação"])
print(aluno["Idade"])

#Adicionar a Cidade ao Dicionario
aluno.update({"Cidade":"São Paulo"})
print(aluno.values())