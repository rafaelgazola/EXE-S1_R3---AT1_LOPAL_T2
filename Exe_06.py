# Exercicio 06 - Número Primo
#entrada de dados
inteiro = int(input("Me informe um número primo: "))

divisoes = 0 #Variavel seguindo a logica
for i in range(1, inteiro + 1): #regra da logica do numero primo no py
  if inteiro % i == 0:
   divisoes = divisoes + 1 #logica matematica

#saida de dados
if divisoes == 2: #se a divisão for igual a dois
  print(f"{inteiro} É um número primo")  #sequencia de laço de repetição, para confirmar a resposta correta
else:
  print(f"Não, {inteiro} não é um número primo ")
