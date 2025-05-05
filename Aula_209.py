class Pessoa:
    ano = 2023

    def __init__(self, nome, idade, peso, altura):  # type: ignore
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    @classmethod
    def saudacao(cls, nome):  # type: ignore
        # print(f'Olá {nome}')
        return f'Olá {nome}'

    @classmethod
    def imc(cls, peso, altura):  # type: ignore
        imc = peso / (altura ** 2)  # type: ignore
        return f'Olá {imc}'


# p1 = Pessoa('João', 34)
# print(p1.nome, p1.idade)
saudacao = Pessoa.imc(80, 1.70)  # type: ignore
print(saudacao)
