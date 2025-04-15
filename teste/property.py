class Carro:
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self._fabricante = marca

    @property
    def marca(self):
        return self._fabricante


c1 = Carro('teste', 'carro')

print(c1.modelo, c1.marca)
