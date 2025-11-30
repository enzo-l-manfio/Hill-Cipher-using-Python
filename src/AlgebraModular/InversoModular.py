from sympy import isprime
from numpy import gcd

def inversoModular(numero, modulo):

    #Caso o módulo é primo, utiliza o Teorema de Euler
    if isprime(modulo):
        inverso =  pow(numero, modulo-2, modulo)
    
    #Se o módulo e o número forem primos entre si, o inverso não existe
    elif gcd(numero, modulo) != 1:
        inverso = None

    #Se o módulo não for primo e o inverso existir, aplica o Algoritmo Extendido de Euclides
    else:
        a = modulo
        b = numero
        q = int(a/b)
        r = a%b
        t1 = 0
        t2 = 1
        t3 = t1 - q*t2
        while b != 1:
            a = b
            b = r
            t1 = t2
            t2 = t3
            q = int(a/b)
            r = a%b
            t3 = t1 - q*t2
        inverso = t2%modulo

    return inverso
