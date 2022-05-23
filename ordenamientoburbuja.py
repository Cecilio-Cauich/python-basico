import random

def ordenamiento_burbuja(lista):
    n = len(lista) - 1

    for i in range(n):
        print('Primer for #'+str(i))

        for j in range(0,n):   
            print('Comparando '+str(lista[j])+' > '+str(lista[j + 1]))

            if lista[j] > lista [j + 1]:
                print('Si es mayor')
                lista[j], lista [j + 1] = lista [j + 1], lista[j]

    return lista

if __name__ == '__main__':

    tamanolista = int(input('De que tamano sera la lista '))

    lista = [random.randint(0,100) for i in range(tamanolista)]
    print(lista)

    listao_ordenada = ordenamiento_burbuja(lista)
    print(listao_ordenada)