import random
def ordenamientomezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        ordenamientomezcla(izquierda)
        ordenamientomezcla(derecha)
        i=0
        j=0
        k=0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda [i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1 
            k += 1
        
        while i < len(izquierda):
            lista[k] = izquierda [i]
            i += 1
            k += 1
        
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

    return lista




if __name__ == '__main__':

    #tamanolista = int(input('De que tamano sera la lista'))

    #lista = [random.randint(0,100) for i in range(tamanolista)]
    lista = [279,42,500,147,605,740,81,401]
 
    print('Lista aleatoria')
    print(lista)

    listaordenada = ordenamientomezcla(lista)
   
    print('Lista ordenada')
    print(listaordenada)