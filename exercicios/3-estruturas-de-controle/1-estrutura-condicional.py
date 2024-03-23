# Declare 4 variáveis do tipo numérica
n1 = int(input('Which number am i thinking?'))
n2 = 6
n3 = 11.7
n4 = 90
lista = [n1, n2, n3, n4] 
maior = max(lista)
menor = min(lista)

# Crie uma estrutura condicional para comparar dois números
if n1 > n2 and n1 != 11:
  # Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor
  print(f'Close enough! {maior} was the number')
elif n1 < n2:
  print(' Try a bigger value') 
elif n1 == 11:
  print('JACKPOT!')  
else: 
  print(f'Not quite close, not enough, try something around {max}')
# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor
# Insira outras condições na estrutura condicional usando o elif
# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"
# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"
