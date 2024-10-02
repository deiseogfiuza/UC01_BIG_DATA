# Calculo de prestação 
prestacao = float(input("Informe o valor da sua prestação:"))
tempo = float(input("Informe o tempo de pagamento:"))
taxa = float(input("Informe o valor da Taxa de juros:"))
valor_final = (prestacao +(prestacao*(taxa/100)*tempo))
print(f"O valor em atraso será de R$ {valor_final:.2f}")
# {valor_final:.2f} formula para organizar o valor decimal na resposta / Caso não queira só colocar 0 antes do f