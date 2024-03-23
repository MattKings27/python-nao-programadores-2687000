ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
idade = ano_formatura - ano_nascimento
print(f'Gerlaine tinha {idade} anos em sua formatura')
# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
print(ano_nascimento > ano_formatura)
print(ano_formatura == ano_nascimento)
print(ano_nascimento <= ano_formatura)
# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
print(ano_formatura or ano_nascimento > 0)
print(ano_formatura and ano_nascimento > 0)
print(not ano_formatura and ano_nascimento > 0)

