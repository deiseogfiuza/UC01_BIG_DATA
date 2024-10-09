soma = 0
soma_m = 0
soma_f = 0
soma_o = 0
soma_a = 0
soma_v = 0
soma_c = 0
cont_f = 0
cont_m = 0
cont_o = 0
maior = 0
for i in range (5):
    sexo = input("Informe seu Sexo F ou M : ")
    olhos  = input("Informe a Cor dos seus Olhos: ")
    cabelo  = input("Informe a Cor do seu Cabelo: ")
    idade = int(input("Agora sua Idade: "))     
    if sexo == "M" or sexo == "m" :
        soma_m = soma_m + idade 
        cont_m += 1
    if sexo == "F" or sexo == "f" :
        soma_f = soma_f + idade 
        cont_f += 1
        print(len(soma_f))
    if olhos == "azuis":
        soma_a = soma_a + olhos 
        cont_o += 1 
        print(len(soma_a))
    if olhos == "verdes" :
        soma_v = soma_v + olhos 
        cont_o += 1 
        print(len(soma_v))
    if olhos == "castanhos" :
        soma_c = soma_c + olhos 
        cont_o += 1 
        print(len(soma_c))
    elif idade >= 18 and idade <=65 :
         media = media_f
    print(f"A Média dos Individuos do Sexo Feminino com idade entre 18 e 65 Anos é : {media:.2f}")
else:
    print(f"{nome}, Você está Reprovado, pois sua média foi {media:.2f}")                   
media_m = soma_m / cont_m
media_f = soma_f / cont_f
print(f"A soma das idades dos Homens é {soma_m} e a Média delas é {media_m:.0f} ")
print(f"A soma das idades das Mulheres é {soma_f} e a Média delas é {media_f:.0f}  ")
print(f"A soma das Mulheres com olhos azuis é {soma_a} e cabelos loiros é {media_f:.0f}  ")
         