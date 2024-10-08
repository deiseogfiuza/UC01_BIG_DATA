h = float(input("Informe sua altura: "))
sexo = (input("Informe M para Masculino e F para Feminino "))
#if sexo == "M" : // Apenas uma descrição - possibilidades de erro na resposta 
if sexo == "M" or sexo == "m" :
  M = (72.7 * h) - 58
  print(f"O seu peso ideal é {M:.2f}")
#elif sexo == "F" :
elif sexo == "F" or sexo == "f" :
  F = (62.1 * h) - 44.7
  print(f"O seu peso ideal é {F:.2f}")
else: 
 print("Verifique o sexo Informado")