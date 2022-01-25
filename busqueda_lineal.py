
import random

#Complejidad de la busqueda lineal: O(n) lINEAL
def busqueda_lineal(list, target):
    match = False #O(1)

    for element in list: #O(n)
        if element == target: #O(1)
            match = True #O(1)
            break #O(1)

    return match

if __name__ == '__main__':
    size_list = int(input('Enter the size of the list: '))
    target = int(input('Enter the target: '))

    list_ = [random.randint(0,100) for i in range(size_list)]

    encontrado = busqueda_lineal(list_, target)
    print(list_)
    print(f'El elemento {target} {"esta" if encontrado else "no esta"} en la lista')        
