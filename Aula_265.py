from dataclasses import dataclass


@dataclass
class Pessoas:
    nome: str
    sobrenome: str
    idade: int


@property
def nome_completo(self):
    return f'{self.nome}, {self.sobrenome}'


@nome_completo.setter
def nome_completo(self, valor):
    nome, *sobrenome = valor.split()
    self.nome = nome
    self.sobrenome = ' '.join(sobrenome)


# inicio
if __name__ == '__main__':
    # p1 = Pessoas('Anderson', 30)
    # p2 = Pessoas('Luiz', 30)
    # print(p1 == p2)
    p1 = Pessoas('Luiz', 'Otavio', 30)
    p1.nome_completo = 'Maria Helena'  # type: ignore
    print(p1)
    print(p1.nome_completo, p1.idade)  # type: ignore
