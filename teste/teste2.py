class Carro:
    def __init__(self, nome, marca):
        self.nome = nome
        self.marca = marca


    def modelo(self):
        return self.nome
    





carro1 = Carro('gol', 'volks')
print(modelo())