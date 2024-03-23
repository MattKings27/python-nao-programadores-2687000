# Crie duas variáveis do tipo numérica, uma sinalizando a fase atual do curso e outra o nível final
nv_atual = 1
nv_final = 4
 
# Crie um while loop que imprima na tela o nível atual


# Insira "else" no while loop anterior.
while nv_atual <= nv_final:
  print(f' Você avançou um nível do curso, seu nível atual é {nv_atual}')
  nv_atual += 1
else:
  print(f'Parabéns, você atingiu o nível {nv_final}, que é o máximo.')
