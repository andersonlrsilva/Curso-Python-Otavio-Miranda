# import os
import json

# funções


def listar(tarefas):
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    for tarefa in tarefas:
        print(tarefa)


def desfazer(tarefas, tarefas_desfazer):
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)
    print(tarefa)


def refazer(tarefas, tarefas_refazer):
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)


def adicionar(comando, tarefas):
    tarefas.append(comando)


def ler(tarefas, caminho_do_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, ident=2)
    return


caminho_arquivo = 'aula119.json'
tarefas = ler([], caminho_arquivo)
tarefas_refazer = []


# variaveis

tarefas_refazer = []
tarefas = []


# programa

while True:
    print()
    print('-'*30)
    print(f'{"LISTA DE TAREFAS":^30}')
    print('-'*30)
    print('Comandos: Listar, desfazer, refazer, sair')
    print()
    comando = input('Digite uma tarefa ou comando: ')
    if comando == 'listar':
        listar(tarefas)
        continue
    if comando == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        continue
    if comando == 'refazer':
        refazer(tarefas, tarefas_refazer)
        continue
    if comando == 'sair':
        break
    elif adicionar(comando, tarefas):
        print(tarefas)
        continue
