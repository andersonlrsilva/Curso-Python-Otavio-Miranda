class Pessoa:
    ano = 2023


    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    @classmethod
    def saudacao(cls, nome):
        #print(f'Olá {nome}')
        return f'Olá {nome}'
    
    @classmethod
    def imc(cls, peso, altura):
        imc = peso / (altura ** 2)
        return f'Olá {imc}'







#p1 = Pessoa('João', 34)
#print(p1.nome, p1.idade)
saudacao = Pessoa.imc(80, 1.70)
print(saudacao)
