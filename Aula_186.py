caminho = 'aula186.txt'
# arquivo = open(caminho, 'w+')
# with open(caminho, 'w+') as arquivo:


with open(caminho, 'a+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')


arquivo = open(caminho, 'a+')
arquivo.write('linha4\n')
arquivo.close()
