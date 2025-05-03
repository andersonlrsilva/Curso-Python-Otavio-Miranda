def recursiva(inicio=0, fim=4):
    print(inicio, fim)
    if inicio >= fim:
        return fim

    inicio += 1
    return recursiva(inicio, fim)


print(recursiva())
print  ('teste')
