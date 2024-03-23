# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
lista_cursos = ['Python', 'SQL', 'Fortran', 'Javascript', 'Java']
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
python = str(lista_cursos[0])
java = str(lista_cursos[-1])
js = str(lista_cursos[3])
git = 'Github'
# 3. Crie um dicionário vazio para armazenar a nota do curso
nota = {}
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
if python in lista_cursos:
  print('O curso está na lista!')
  nota['python'] = int(input('Digite a nota obtida: '))
if java in lista_cursos:
  nota['java'] = int(input('Digite a nota obtida: '))
if js in lista_cursos:
  nota['js'] = int(input('Digite a nota obtida: '))  
if git in lista_cursos:
  print('Tu é o bixão mermo') 
else:
  print(' O curso não está na lista!')
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota
media = 0
for value in nota.values():
  media = media + value
print(f'Sua média é de: {media/(len(nota))}')