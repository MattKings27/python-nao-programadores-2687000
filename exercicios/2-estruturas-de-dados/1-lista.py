# Crie uma lista apenas com elementos numéricos
num = [1, 2, 3]
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
lista = [1, [3,7], 'gandalf', 1.4]

# Imprima na tela apenas os 5 primeiros elementos da lista
print(lista[:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par
print(lista[2:4])

# Remova da lista o último item
lista.pop()

# Insira na lista um novo item
lista.append('balrog')
# Remova da lista um item específico
lista.remove('gandalf')

print(lista)