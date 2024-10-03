nome = input("Informe o nome do estudante: ")
n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: ")) 
media = (n1 + n2) / 2
#print(nome,"Sua Média é : ",media)
if media >= 70 :
    media = (n1 + n2) / 2
    print(f"{nome}, Você está Aprovado, pois sua média foi {media:.2f}")
   # print("Você está Aprovado")
elif media >= 30 and media < 70 :
     media = (n1 + n2) / 2
     print(f"{nome}, Você está em Recuperação, pois sua média foi {media:.2f}")
     #print("Você está em Recuperação")
else:
     print(f"{nome}, Você está Reprovado, pois sua média foi {media:.2f}") 