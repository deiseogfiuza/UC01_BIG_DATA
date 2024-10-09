temperatura = []
resp ="S"
while resp == "S" or resp == "s":
    temperatura.append(float(input("Informe a temperatura: ")))
    resp = input("Deseja Continuar (S/N) ")
print(f"A Maior Temperatura é : {max(temperatura)} ºC ")
print(f"A Menor Temperatura é : {min(temperatura)} ºC ")
print(f"A Média das Temperaturas é : {sum(temperatura)/len(temperatura)} ºC ")