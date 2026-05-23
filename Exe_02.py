# Exercicio 02 - Número maior e menor usando lista
import time
#Entrada de dados
n1 = int(input("Digite o primeiro numero:"))
n2 = int(input("Digite o segundo nuemro:"))
n3 = int(input("Digite o terceiro numero:"))

#criando a lista
lista = [n1,n2,n3]

#lista definindo maior numero, e o menor numero.
maior = max(lista)
menor = min(lista)

#imprime o resultado
print(f"O Maior número é: {maior}")
print(f"O Menor número é: {menor}")

