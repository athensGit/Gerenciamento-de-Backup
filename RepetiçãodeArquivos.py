todos_os_arquivos = [metadados[arquivo]['Nome'] for arquivo in metadados]
quantidade = {}
for tipo in todos_os_arquivos:
  quantidade[tipo] = todos_os_arquivos.count(tipo)
  if quantidade[tipo] > 1:
    print(f'O arquivo {tipo} se repete {quantidade[tipo]} vezes.')
print(quantidade)
if quantidade[tipo] == 1:
  print('Nenhum arquivo se repete.')
