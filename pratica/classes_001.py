

class Pessoas:
    def __init__(self, nome, sobrenome, idade: int = 0, sexo='ND'):
        self.nome = nome
        self.sobrenome = sobrenome
        self._idade = idade
        self.sexo = sexo

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade


p1 = Pessoas('Anderson', 'Luiz', 18)
print(p1.nome)
print(p1.sobrenome)
print(p1.idade)
print(p1.sexo)
p1.idade = 42
print(f'Nova Idade {p1.idade}')
