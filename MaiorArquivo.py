maior = 0
nome_do_maior_arquivo = ''
for arquivo in metadados:
  if metadados[arquivo]['Tamanho'] > maior:
    maior = metadados[arquivo]['Tamanho']
    nome_do_maior_arquivo = metadados[arquivo]['Nome']

print(f'O maior aquivo é {nome_do_maior_arquivo} cuja extensão é de {maior}.')
