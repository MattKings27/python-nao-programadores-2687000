# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
# 2. Armazene esses dados em um dicionário

info = {}

info ['nome']  = input('How should i call you, young padawan? ')
info ['jedi since'] = int(input('Which year did you join the Jedi order? '))
info ['AY'] = int(input('Which year is this? '))
training = input('So, about your trainings, which Jedi mastery did you learn? Separate them by comma ')
info ['training'] = training.split(', ')

# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
total_anos = info['AY'] - info['jedi since']
total_curso = len(info['training'])

print (f'Oh, very interesting indeed young one. So, {info['nome']}, i believe you may not be that much of a Padawan!  \n You are a member of the order since {info['jedi since']} and have {len(info['training'])} masteries, by completing {info['training'][0]} and {info['training'][-1]}, i believe you have {total_anos} years of Jedi discipline in you! But remember, {info['training'][1]} is the balance, so keep the training. ')