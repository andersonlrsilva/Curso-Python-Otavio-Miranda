class  Carro:
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca





class Caneta:
    def __init__(self, cor) :
        self.cor = cor



iten1 = Caneta('azul')

car1 = Carro('Gol', 'Wolkswagem' )
car2 = Carro('Omega', 'chevrolet')



print(car1.modelo)
print(car1.marca)
print(car2.modelo)
print(car2.marca)
print(iten1.cor)