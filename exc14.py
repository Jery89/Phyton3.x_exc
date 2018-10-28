def list_reduce1(input):
    lista = input
    index = 0
    for x in range(index+1, len(lista)-1):
        if lista[index] == lista[x]:
            lista.remove(x)
    return lista


def list_reduce2(lista):
    return set(lista)


lista = [1, 1, 2, 3, 4, 7, 7, 6, 4, 3]

print(list_reduce1(lista))
print(list_reduce1(lista))