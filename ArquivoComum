tipos = [metadados[arquivo]['Tipo de arquivo'] for arquivo in metadados]
# printando a lista de arquivos para verificação
print(tipos)
quantidade = {}
maior = 0
nome = ''
# fazendo a contagem dos tipos de arquivos
for tipo in tipos:
  quantidade [tipo] = tipos.count(tipo)
  if quantidade[tipo] > maior:
    maior = quantidade[tipo]
    nome = tipo

print(f'O tipo de arquivo mais comum é o tipo {nome}, que se repete {maior} vezes.')
