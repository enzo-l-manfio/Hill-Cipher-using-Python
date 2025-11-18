import Criptografia as cript
import numpy as np

def divisores(n):
    divisores = []
    for i in range(1, n+1):
        if n%i != 0 :
            continue
        else:
            divisores.append(i)
    return divisores

def Decifrar(blocos_descriptografados, blocos_criptografados):
    if len(blocos_descriptografados) != len(blocos_criptografados) :
        raise ValueError("blocos descriptografados não correspondem aos blocos criptografados")
    for i in range(len(blocos_descriptografados)) :
        if len(blocos_descriptografados[i]) != len(blocos_criptografados[i]) :
            raise ValueError("blocos descriptografados não correspondem aos blocos criptografados")

    conjunto_descriptografado = ''
    conjunto_criptografado = ''
    mdc = np.gcd.reduce([len(bloco) for bloco in blocos_criptografados])
    if mdc == 1:
        raise ValueError("Vetores de tamanhos primos entre si")
    for i in range(len(blocos_criptografados)):
        conjunto_descriptografado += blocos_descriptografados[i]
        conjunto_criptografado += blocos_criptografados[i]
    possiveis_matrizes = []

    for n in (divisores(mdc)) :
    
        if len(conjunto_descriptografado) < n**2:
            continue
        
        MatrizDescriptografada = cript.CriarMatrizString(conjunto_descriptografado, [n, n])
        MatrizCriptografada = cript.CriarMatrizString(conjunto_criptografado, [n, n])

        # K = C * D^-1 , em que K é a matriz chave, D a dos blocos descriptografados e C a dos blocos criptografados
        MatrizChave = MatrizCriptografada @ cript.InversaModular(MatrizDescriptografada, cript.modulo)
        MatrizChave = cript.Modular(MatrizChave, cript.modulo)
        possiveis_matrizes.append(MatrizChave)
    return possiveis_matrizes



Cifra = cript.CifraHill("EnzoKayc1")

blocos_descriptografados = ["Angulegal"]
blocos_criptografados = [Cifra.Criptografar(mensagem) for mensagem in blocos_descriptografados]

print(Cifra.Matriz)

possiveis_matrizes = Decifrar(blocos_descriptografados, blocos_criptografados)

for possibilidade in possiveis_matrizes:
    print()
    print(possibilidade)