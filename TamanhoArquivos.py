dicio = {}
maior = 0
nome = ''
for arquivo in metadados:
  nome = metadados[arquivo]['Nome']
  dicio [nome] = metadados[arquivo]['Tamanho']
  maior += metadados[arquivo]['Tamanho']

print('Essa é a relação dos arquivos e os seus tamanhos:', dicio)
print(f'A soma dos tamanhos de todos os arquivos totaliza {maior} de tamanho total do backup.')
