
import os

caminho = os.path.join('F:\\')
# print(os.listdir(caminho))

for pasta in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, pasta)
    # print(caminho_completo)
    if not os.listdir(caminho_completo):
        continue

    for itens in os.listdir(caminho_completo):
        print(itens)
