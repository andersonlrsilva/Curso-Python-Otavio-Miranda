







def analiza_primo(func):
    def primo(*args, **kwargs):
        num = func(*args, **kwargs)
        mult = 0
        for i in range(2, num):
            if (num % i == 0):
                mult += 1
        if (mult==0):
            print(f'O numero {num} e \033[31mprimo\033[m')
        else:
            print(f'O numero {num} e \033[31mnão é primo\033[m')
            return 
    return primo








@analiza_primo
def analiza_numero(numero):
    num = int(numero)
    if num %2 != 0:
        print(f'O numero {num} é ímpar!')
    else:
        print(f'O numero {num} é par!')
    return num





numero = input('Digite um numero: ')
analiza_numero(numero)