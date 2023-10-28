# importar bibliotecas do OS para acesso ao sistema operacional e manipulação geral e shutil para cópia e remoção de arquivos
import os
import shutil
import time

def backup(origem, destino):
  arquivos_copiados = 0

  # Verifica se o diretório de origem existe
  if not os.path.exists(origem):
    print(f"O diretório de origem '{origem}' não existe.")
    return

  # Verifica se o diretório de destino existe
  if not os.path.exists(destino):
    os.makedirs(destino)
    return

  # Verificação se o item é um arquivo (isfile = Retorna True se path for um arquivo regular existente)
  for nome in os.listdir(origem):
    #evitando repetir o mesmo código, criamos uma variável
    caminho = origem + '/' + nome

    if os.path.isfile(caminho):
      shutil.copy2(caminho, destino + nome)
      informacoes = {
          'Nome': nome,
          'Tamanho': os.path.getsize(caminho),
          'Tipo de arquivo': os.path.splitext(nome)[1],
          'Local do backup': destino + nome,
          'Data de criação do arquivo': time.ctime(os.path.getctime(caminho))
      }
      metadados[caminho] = informacoes
      arquivos_copiados += 1
    elif os.path.isdir(caminho):
      novo_destino = destino + nome + '/'
      if not os.path.isdir(novo_destino):
        os.makedirs(novo_destino)
      backup(caminho, novo_destino)

    print(f"Copiando o item {nome}")
    print(f"Metadados: {informacoes}")
    print('Arquivo copiado!')
    print('---')

  print("Backup completo.")
  print(f"Total de arquivos copiados: {arquivos_copiados}")
  print("Metadados:", metadados)
  print('---')

metadados = {}

origem = 'sample_data'
destino = 'Backup/'

backup(origem, destino)
