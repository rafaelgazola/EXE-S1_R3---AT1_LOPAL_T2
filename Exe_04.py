# Exercicio 04 - usando a sequencia de Fibonacci gereando a partir da somatória

#entrada de dados
n_user = int(input("Ate que número o senhor gostaria? "))

#colocando uma parte da logica
penultimo = 1
ultimo = 1

#for pra sempre repetir conforme a quantidadde do user
for i in range(n_user):
  print(penultimo)

  proximo = penultimo + ultimo  #logica conforme a do Fibonacci mostrando a sequencia com as variaveis
  penultimo = ultimo
  ultimo = proximo

print(f"Resultado para o senhor {n_user}, Como o senhor queria 👌") #resultado de quantidade q o user queria.