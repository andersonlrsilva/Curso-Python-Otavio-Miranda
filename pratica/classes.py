class Nome:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        resultado = self.func(*args, **kwargs)
        return resultado.capitalize()


@Nome
def maiuscula(nome):
    text = nome.lower()
    return text
