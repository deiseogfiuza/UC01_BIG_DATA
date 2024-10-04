try:
    n1 = int(input("Informe o primeiro valor: " ))
    n2 = int(input("Informe o segundo valor: " )) 
except ValueError:
    print("Verifique a entrada dos dados")
else:
    try:
        valor = (n1 / n2) 
    except ZeroDivisionError :
        print("Não é aceito 0 como número")
    else:
        print(valor)