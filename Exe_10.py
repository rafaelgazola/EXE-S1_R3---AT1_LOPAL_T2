# Exercicio 10 - verificação desenha: six senve
#Entrada de dado
senha = int(input("Me informe a senha correta senhor: "))

senha1 = 676767 #definição da variavel com a senha correta

while senha1 != senha: #logica com laço de repetição, se não for a variavel que está a senha
  senha = int(input("Errou senhor, informe novamente: ")) # dará erro
else:
  print(f"Parabéns senhor, correto a senha {senha}") # se for a variavel correta, parabéns.