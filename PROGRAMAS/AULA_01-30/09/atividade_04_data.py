# Cálculo de Idade com base de ano e inclusão de Nome
import datetime
data_atual = datetime.date.today()
# ano_atual = data_atual.year
nome = input("Informe seu Nome : ")
base = int(input("Informe o seu Ano de Nascimento : "))
calculo = data_atual.year - base 
print(nome,"Sua idade é : " ,calculo) 