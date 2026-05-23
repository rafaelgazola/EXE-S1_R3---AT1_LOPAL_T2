# Exercicio 05 - programa que valida a seguintes pergutas da atividade
#entrada de dados (NOME)
name = input("Digite seu nome senhor: ")
while len(name) <= 3: #Utilize a repetição para sempre ficar na pergunta e o len para contar o caracter
  print("O nome precisa ser maior que 3 caracteres senhor")
  name = input("Digite novamente, com vontade senhor: ")

print(f"Perfeito {name}") #saida

#entrada de dados (IDADE)
idade = int(input("Me fala quantos anos você tem: "))
while idade >= 151: # usando a repetição ate 151 anos fora disso é mais velho
  print("O senhor está muito velho, digite novamente ")
  idade = int(input("Digita qual a sua idade real novamente senhor: "))

print(f"Maravilha então, {idade} anos 🎂") #saida

#entrada dados (SALARIO) float porque pode ser numero quebrado
salario = float(input("Digite qual é o seu salario: "))
while salario <= 0: #mesma sequencia da idade, se for abaixo de 0 você nao tem salario
    print("O senhor está sem dinheiro?")
    salario = float(input("Digite um salario serio: "))

print(f"R${salario} Parabéns senhor, muito dinheiros")

#entrada (GENERO)
genero = input("Digite qual o seu Gênero (f/m): ")
while genero != "f" and genero != "m": # coloquei para ser diferente de f ou o m como erro
  print("O senhor digitou errado, é f ou m !")
  genero = input("Me informe novamente o seu gênero senhor: ")

print(f"top de mais então o senhor é {genero}")

##entrada de dados (ESTADO CIVIL)
civil = input("Me informe o seu estado CIVIL senhor (s,c,v,d): ")
while civil != "s" and civil != "c" and civil != "v" and civil != "d": #mesma a logica do genero
  print("O senhor digitou errado!")
  print("""Segue para conhecimento:
"s" = SOLTEIRO
"c" = CASADO
"v" = VIUVO
"d" = DIVORCIADO""")
  civil = input("Digite qual o seu estado civil novamente: ")
print(f"{civil} Maraviha")

#e uma impressão final dos resultados finais coletados
print("Maravilha senhor, então aqui estão os seus dados cadastrado no nosso sistema: ")
print(f"Nome: {name}")
print(f"Idade: {idade}")
print(f"Salario: {salario}")
print(f"Genero: {genero}")
print(f"Estado Civil: {civil}")