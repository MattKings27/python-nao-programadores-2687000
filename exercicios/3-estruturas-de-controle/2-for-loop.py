# Crie uma lista
from time import sleep
count = [4, 3, 2, 1, 0]
# Crie um for loop para imprimir cada elemento dessa lista
for number in count:
  print(number)
  sleep(1)
print('Launch!')
# Crie um objeto iterável utilizando a função range()
# Use esse objeto iterável para criar um for loop que imprima na
#  tela a frase "Estou aprendendo uma linguagem de programação."
for item in range(1):
  print(f'{item}. Estou aprendendo python!')
else: 
  print('Game Over')