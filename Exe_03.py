# Exercicio 03 - imprimir o nome do user na vertical em escada/piramide
import time #time para um pequeno delay
#entrada de dados
nome = input("Digite o seu nome aqui: ")

nome = nome.upper() #deixar maiusculo o dado(nome)

#estrutura de for para sermpre gerar mias linha no caso e o len conta os caracteres.
for i in range(1, len(nome) + 1 ):
  print(nome[:i])

time.sleep(2)
print("Que nome lindo 😍")