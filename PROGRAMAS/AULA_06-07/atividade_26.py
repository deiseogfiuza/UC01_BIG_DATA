usuarios = [ "Deise" , "Maria" , "Pedro" , "Duda" , "Eduardo"]
senhas = ["123", "M@ria05", "24*dls", "Dud@", "Eduard.0"]
usuario = input("Informe o nome do acesso ao sistema : ")
for i in range (len(usuarios)):
   if usuarios [i] == usuario:
      senha = input("Informe a sua senha de acesso : ")
      if senhas [i] == senha:
         resp = "Acesso Liberado"
      else:
         resp = "Senha Não Confere"      
      break
   else: 
      resp = "Usuário Não Encontrado"  
print(resp)