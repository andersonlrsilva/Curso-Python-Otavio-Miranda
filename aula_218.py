class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None


#### motor
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

####Fabricante
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor



class Motor:
    def __init__(self, nome):
        self.nome = nome

class fabricante:
    def __init__(self, nome):
        self.nome = nome








######inicio do programa
fusca = Carro('Fusca')
motor_1_0 = Motor('motor_AP 1600')
marca = fabricante('Volkswagen')
fusca.motor = motor_1_0
fusca.fabricante = marca
print(fusca.nome, fusca.motor.nome, fusca.fabricante.nome)


gol = Carro('Gol')
marca = fabricante('Volkswagen')
gol.motor = motor_1_0
gol.fabricante = marca
print(gol.nome, gol.motor.nome, gol.fabricante.nome)

