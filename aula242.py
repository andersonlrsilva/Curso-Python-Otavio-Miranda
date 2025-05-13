from contextlib import contextmanager


@contextmanager
def mu_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu erro, e')
    finally:
        print('Fechando arquivo')
        arquivo.close()
