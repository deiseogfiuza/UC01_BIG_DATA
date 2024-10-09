sexo = []
olhos = []
cabelos = []
idade = []
resp = "S"
qtd_sexo_idade = 0
qtd_olhos_cabelos = 0
while resp == "S" or resp == "s" :
    sexo.append(input("Informe o seu Sexo M - masculino ou F - feminino "))
    olhos.append(input("Informe a Cor dos seus Olhos A - azuis, V - verdes ou C- castanhos "))
    cabelos.append(input("Informe a Cor do seus Cabelos L - louros, P - pretos ou C - castanhos "))
    idade.append(float(input("Qual a sua idade: ")))
    resp = input("Deseja Continuar(S/N)? ")
for i in range(len(sexo)):
    if(sexo[i] == "F" or sexo[i] == "f") and (idade[i]>=18 and idade[i] <=35) :
        qtd_sexo_idade += 1
    if(olhos[i] == "V" or olhos [i] == "v") and (cabelos[i] == "L" or cabelos [i] == "l"):
        qtd_olhos_cabelos += 1    
print(f"A Maior Idade dos Habitantes é : {max(idade)} anos .")
print(f"A Menor Idade dos Habitantes é : {min(idade)} anos .")
print(f"A Média das Idades é : {(sum(idade)/len(idade)):.0f} anos.")
print(f"A quantidade de pessoas do sexo feminino com idades entre 18 e 35 anos é : {qtd_sexo_idade}")
print(f"A quantidade de pessoas que possuem cabelos loiros e olhos verdes é : {qtd_olhos_cabelos}")
