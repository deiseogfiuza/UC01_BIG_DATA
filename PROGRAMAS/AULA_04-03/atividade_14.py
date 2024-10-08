try:
    produto = input("Informe o nome do Produto: ")
    qtd = float(input("Informe a quantidade desejada: "))
    valor = float(input("Informe o preço unitário: ")) 
except ValueError:
    print("Verifique os valores informados")
else:    
    total = (qtd * valor)
    print("Total é : " , total)
    if qtd <= 5 :
        print( "Total a pagar : " , (total * 0.98))
    elif qtd >= 5 and qtd <=10 :
        print("Total a pagar : " , (total * 0.97))
    else:
        print("Total a pagar : " , (total * 0.95))