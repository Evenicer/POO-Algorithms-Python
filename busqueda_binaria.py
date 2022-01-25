
import random


def busqueda_binaria(lista, comienzo, final, target):

    print(f'Buscando {target} entre {lista[comienzo]} y {lista[final - 1]}')

    if comienzo > final:
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == target:
        return True
    elif lista[medio] < target:
        return busqueda_binaria(lista, medio + 1, final, target)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, target)            


if __name__ == '__main__':
    size_list = int(input('Enter the size of the list: '))
    target = int(input('Enter the target: '))

    lista = sorted([random.randint(0,100) for i in range(size_list)])

    encontrado = busqueda_binaria(lista, 0, len(lista), target)

    print(lista)
    print(f'El elemento {target} {"esta" if encontrado else "no esta"} en la lista')     