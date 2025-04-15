class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
        

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Já está filmando')
            return
        
        print(f'{self.nome} está filmando...')
        self.filmando = True


    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} Não está filmando')
            return
        
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar Filmando')
            return
        
        print(f'{self.nome} está fotografando...')



# Comandos


canon = Camera('canon')
canon.filmar()
canon.fotografar()
canon.filmar()
canon.parar_filmar()
canon.parar_filmar()
canon.fotografar()