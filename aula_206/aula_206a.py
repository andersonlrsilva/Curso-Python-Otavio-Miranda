import json
alias_arquivo = 'Aula_206/aula206.json'

#classe Pessoa

class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade




p1 = pessoa('João', 33)
p2 = pessoa('Helena', 21)
p3 = pessoa('Joana', 11)
bd = [vars(p1), vars(p2), vars(p3)]


with open(alias_arquivo, 'r+') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)