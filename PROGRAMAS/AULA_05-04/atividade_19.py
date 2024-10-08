soma = 0
for i in range (5):
    nome = (input("Informe seu Nome: "))
    valor = int(input("Agora sua Idade: "))
    soma = soma + valor
media = soma / (i + 1) 
print(f"A soma é {soma} e a Média é {media:.0f}" )   