import random

def busquedabinaria(lista, comienzo, final, objetivo):

    print(f'buscando{objetivo} entre {lista[comienzo]} y {lista[final]}')#error encontrado

    if comienzo > final: #error encontrado aquì
        return False

    medio = (comienzo + final) // 2 #division de enteros
    print('Medio = '+str(medio))
    print('Valor en medio '+str(lista[medio]))
    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        print('Menor que objetivo')
        return busquedabinaria(lista, medio + 1, final, objetivo)
    else:
       print('Mayor que objetivo')
       return busquedabinaria(lista, comienzo, medio - 1, objetivo)


if __name__ == '__main__':
    tamanolista = int(input('De que tamaño sera la lista '))
    objetivo = int(input('Que numero quieres encontrar '))

    lista= sorted([random.randint(0,100) for i in range(tamanolista)])
    
    encontrado = busquedabinaria(lista, 0, len(lista), objetivo)
    print(len(lista))
    print(lista)
    # for i in range(0,10):
    #     print('NUmero: '+str(lista[i]))
    #     print ('indice: '+str(i))
    print('tamano lista'+str(len(lista)))
    print(f'Elemento {objetivo} {"Esta" if encontrado else "no esta"} en la lista')
