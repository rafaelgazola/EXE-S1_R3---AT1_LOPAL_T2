# Exercicio 01 - Usando FOR com número de 0 a 100
import time   # biblioteca time

print("Olá eu sou uma calculadora de nmeros Impares ou Pares de 0 a 100")
time.sleep(3)
print("==CONTANDO==")
time.sleep(3)

#Usando o for para fazer a repetição, e o range para gerar o numero na sequencia no caso ate 100
for numero in range(101): #vai ate o 101 porque no PY começa do 0.
  if numero % 2 == 0:
    print(f"{numero} par")
  else:
    print(f"{numero} impar")
