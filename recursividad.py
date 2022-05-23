from math import factorial


def recursividad(n):
    print(n)
    if n == 1:
        return 1
    return n * factorial(n - 1)
  

if __name__ == '__main__':
    n = int(input("Entrada numero entero: "))
    print(factorial(n))