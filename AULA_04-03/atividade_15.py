import datetime
try:
    data_atual = datetime.date.today()
    base = int(input("Informe o seu Ano de Nascimento : "))
    ano = int(input("Tem quantos anos na empresa : "))
except ValueError:
    print("Verifique os valores informados") 
else: 
    calculo = data_atual.year - base 
    admissao = data_atual.year - ano 
    if calculo >= 65 and admissao >= 30 :
        print( "Apto a Aposentadoria" )
    elif calculo >= 60 and admissao >= 25  :
        print("Apto a Aposentadoria")
    else:
        print("Inapto a Aposentadoria ")