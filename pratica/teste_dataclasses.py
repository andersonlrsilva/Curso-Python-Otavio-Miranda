from dataclasses import dataclass


@dataclass
class Carro:
    marca: str
    _modelo: str
    portas: int

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, model):
        self.model = model
        self._modelo = self.model


c1 = Carro('ford', 'fusca', 2)
print(c1.marca, c1.modelo, c1.portas)
c1.modelo = ('GM')
print(c1.marca, c1.modelo, c1.portas)
