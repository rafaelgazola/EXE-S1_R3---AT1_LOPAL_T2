# Exercicio 07 - Fatorial pelo número do usuario
#entrada de dados
fat = int(input("Digite um número para descobrir a fatorial senhor: "))

fatorial = 1  #Calcula usando range a fatorial multiplicando todos os numeros do n ate o 1
for i in range(1, fat +1):
  fatorial = fatorial * i  #aplicando na variavel

print(f"Sua fatorial senhor, é {fatorial}") #saida de dados
    