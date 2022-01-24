import time
import sys
sys.setrecursionlimit(1000000)

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta

def factorial_r(n):
    if n == 1:
        return 1
    print("Rec:" + str(n))
    return n * factorial_r(n-1)


if __name__ == '__main__':
    n = 2000

    # comienzo = time.time()
    # factorial(n)
    # final = time.time()
    # print('Tiempo while: ' + str(final-comienzo))       

    comienzor = time.time()
    factorial_r(n)
    finalr = time.time()
    print('Tiempo recursivo: ' + str(finalr-comienzor))             