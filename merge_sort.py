import random
          

def merge_sort(lista):
    n = len(lista)

    if n > 1:
        medio = n // 2
        left = lista[:medio]
        right = lista[medio:]

        print(left, '*' * 5, right)

        #Llamada recursiva en cada mitad
        merge_sort(left)
        merge_sort(right)

        # Iteradores para recorrer las dos sublistas 
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lista[k] = left[i]
                i += 1
            else:
                lista[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1

        print(f'left {left}, right {right}')
        print(lista)
        print('-' * 50)    

    return lista                            


if __name__ == '__main__':
    size_list = int(input('Enter the size of the list: '))

    lista = [random.randint(0,100) for i in range(size_list)]
    print(lista)

    lista_ordenada = merge_sort(lista)
    print(lista_ordenada)