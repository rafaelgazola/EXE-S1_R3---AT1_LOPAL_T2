# Exercicio 11 - Tabuada com o número
#Entrada de dados
numero = int(input("Senhor me forneça um número para a tabuada de 1 a 10: "))

for i in range(1,11): # logica para repetir a linha pela quantidade de numero pedido
  multi = numero * i #multiplicação = multiplicando pelo número pedido

  print(f"{numero} x {i} = {multi}") #saida de dados, mostrando o resultado pedido
