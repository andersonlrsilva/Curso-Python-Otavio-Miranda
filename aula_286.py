import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP =  os.path.join(HOME, 'Área de trabalho')
PASTA_ORIGINAL = ('/media/anderson/Arquivos/Programas')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA PASTA')

# Criar a Nova pasta, exist_ok=True ignora caso a pasta ja exista
os.makedirs(NOVA_PASTA, exist_ok=True)

#Criar os caminho das pastas existentes no local original
for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        )
#Cria os diretorios listados em caminho_novo_diretorio       
        os.makedirs(caminho_novo_diretorio, exist_ok=True)

#criar lista de arquivos do diretorio original    
    for file in  files:
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(     
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file # type: ignore
        )
#copia os arquivos listados em caminho_novo_arquivo             
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)

