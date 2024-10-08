soma = 0
soma_m = 0
soma_f = 0
cont_f = 0
cont_m = 0
maior = 0
for i in range (5):
    nome = input("Informe seu Nome: ")
    sexo = input("Informe seu Sexo F ou M : ")
    idade = int(input("Agora sua Idade: "))
    if idade > maior:
        maior = idade     
    if sexo == "M" or sexo == "m" :
        soma_m = soma_m + idade 
        cont_m += 1
    if sexo == "F" or sexo == "f" :
        soma_f = soma_f + idade 
        cont_f += 1
media_m = soma_m / cont_m
media_f = soma_f / cont_f
print(f"A soma das idades dos Homens é {soma_m} e a Média delas é {media_m:.0f} ")
print(f"A soma das idades das Mulheres é {soma_f} e a Média delas é {media_f:.0f}  ")
print(f"A maior idade é {maior}") 