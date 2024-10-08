nomes = []
medias = []
resp = "S"
while resp == "S" or resp == "s" :
    nomes.append(input("Informe o nome do estudante: "))
    medias.append(float(input("Informe a média do estudante: ")))
    resp = input("Deseja Continuar(S/N)? ")
for i in range(len(medias)):
        print (i, " - ",nomes[i], " - ", medias [i])
maior_media = max(medias)
pos = medias.index(maior_media)
print(f"{nomes[pos]}, Você possui a maior Média")        
print(f"A Maior Média é : {max(medias)} anos .")
print(f"A Menor Média é : {min(medias)} anos .")
print(f"A Média da Turma é : {(sum(medias)/len(medias)):.1f}")
print(f"A Amplitude da Média da turma é : {max(medias)-min(medias)}")
medias.sort()    
print(medias)