# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome = input('Greetings sir, how should i call you?')
# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dias = (input(f'How many days will take your wizard training, Mr. {nome}?'))
# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
total_horas = (input(f'And how many hours, if i may ask?'))
# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
curso = (input('Sir, just for curiosity, which magic school are you studying?')) 
# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
print(f'Oh, i see sir, i know you created me, but is good to talk to someone. And very rich to know Mr. {nome}, that you will take {total_dias} days and {total_horas} hours to finish your {curso} training!, must of luck, i bet you have people counting on you!')
