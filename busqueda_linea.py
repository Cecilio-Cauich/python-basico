
from __future__ import barry_as_FLUFL
from random import random


import random

def busquedalineal(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    return match
if __name__ == '__main__':
    tamanolista = int(input('De que tamaño sera la lista '))
    objetivo = int(input('Que numero quieres encontrar '))

    lista= [random.randint(0,100) for i in range(tamanolista)]
    
    encontrado = busquedalineal(lista, objetivo)
    print(lista)
    print(f'Elemento {objetivo} {"Esta" if encontrado else "no esta"} en la lista')
