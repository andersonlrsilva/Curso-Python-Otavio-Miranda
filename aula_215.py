class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    
    @property
    def ferramenta(self):
        return self._ferramenta


    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta



class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome


    def escrever(self):
        return f' A {self.nome} Quebrou'






#############
escritor = Escritor('Luiz')
maquina_de_escrever = FerramentaDeEscrever('maquina')
caneta = FerramentaDeEscrever('caneta Bic')
escritor.ferramenta = maquina_de_escrever



print(escritor.nome)
print(caneta.nome)
print(caneta.escrever())
print(maquina_de_escrever.escrever())
print(escritor.ferramenta.escrever())