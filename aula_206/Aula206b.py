import json
from Aula_206a import pessoa

with open('Aula_206/aula206.json', 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = pessoa(**pessoas[0])
    p2 = pessoa(**pessoas[1])
    p3 = pessoa(**pessoas[2])





    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)
