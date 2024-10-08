# Calculo de Altura 
# Usar . no lugar de , para calculo decimal 
# nome = input("Informe seu Nome:")
h = float(input("Informe sua altura:"))
M = (72.7 * h) - 58
F = (62.1 * h) - 44.7
# print("O peso ideal para os Homens é:",M, "E o peso ideal para as Mulheres é:",F)
# print = ("O peso Mulher é:",F)
print(f"O peso ideal para os homens é {M:.2f} e o peso ideal para as mulheres é {F:.2f}")