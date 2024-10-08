usuarios = ["Deise", "Maria", "Pedro", "Duda", "Eduardo"]
senhas = ["123", "M@ria05", "24*dls", "Dud@", "Eduard.0"]
#usuario = resp
#senha = input("Informe a sua senha")
#print(input("Informe a sua Senha: "))
for i in range (len(usuarios)):
   if usuarios [i] == usuario:
      resp = input("Informe a sua senha")
      usuario = resp
      senha = resp
for i in range (len(senhas)):
   if senhas [i] == senha:
      resp = input("Senha Encontrada")      
      break
else: 
   resp = "Usuário Não Encontrado"  
print(resp)
