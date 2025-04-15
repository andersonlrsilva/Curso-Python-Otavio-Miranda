class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []


    def inserir_enderecos(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))
    

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)








class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero




cliente1 = Cliente('Anderson')
cliente1.inserir_enderecos('rua padre', 275)
cliente1.listar_enderecos()