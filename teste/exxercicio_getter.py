class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco*(percentual/100))
    









produto1 = Produto('Camisa', 99)
desc = int(input('Digite o valor do desconto: '))
produto1.desconto(desc)
print(produto1.preco)