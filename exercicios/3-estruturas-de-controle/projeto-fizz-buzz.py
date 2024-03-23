# Criaremos um programa para substituir números por palavras em uma lista
# 1. Crie uma lista com 15 números
lista = list(range(1,31))
# 2. Crie um for loop para percorrer todos os elementos da lista
print(lista)
indice = 0
# 3. Crie uma estrutura condicional para verificar cada número da lista:
for numbers in lista:
  if numbers % 5 == 0 and numbers % 3 == 0:
    lista[indice] = 'FizzBuzz'
  elif numbers % 3 == 0:
    lista[indice] = 'Fizz'
  elif numbers % 5 == 0:
    lista[indice] = 'Buzz'
  else: 
    lista[indice] = numbers
  indice += 1

print(lista)

# 3.1 Caso o número seja divisível por 3, substitua-o por "Fizz"
# 3.2 Caso o número seja divisível por 5, substitua-o por "Buzz"
# 3.3 Caso o número seja divisível por 3 e 5, substitua-o por "FizzBuzz"

