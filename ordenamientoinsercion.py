from re import I


def ordenamientoinsercion(lista):

    for i in range(1, len(lista)):
        print('Vuelta numero '+str(i))
        actual =  lista[i]
        indice = i 

        while indice > 0 and lista[indice - 1] > actual:

            print('comparando: '+str(lista[indice-1])+' > '+str(actual))
            lista [indice] = lista [indice - 1]
            indice = indice - 1
            print(lista)
        lista[indice] = actual
    
    return lista

if __name__ == '__main__':
    lista = [5, 4, 56, 11, 27, 12]

    listaordenada = ordenamientoinsercion(lista)
    print(listaordenada)