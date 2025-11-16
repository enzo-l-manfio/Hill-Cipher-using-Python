import Criptografia as cript
import numpy as np

def Decifrar(blocos_descriptografados, blocos_criptografados):
    conjunto_descriptografado = ''
    conjunto_criptografado = ''
    n = np.lcm.reduce([len(bloco) for bloco in blocos_criptografados])
    for i in range(len(blocos_criptografados)):
        conjunto_descriptografado += blocos_descriptografados[i]
        conjunto_criptografado += blocos_criptografados[i]
    
    linhas = []
    i = 0
    while (i<pow(n, 2)):
        linha=[]
        for j in range(n):
            c = cript.dicionario[conjunto_descriptografado[i+j]]
            linha.append(c)
        linhas.append(linha)
        i+=n
    MatrizDescriptografada = np.array(linhas)

    linhas = []
    i = 0
    while (i<pow(n, 2)):
        linha=[]
        for j in range(n):
            c = cript.dicionario[conjunto_criptografado[i+j]]
            linha.append(c)
        linhas.append(linha)
        i+=n
    MatrizCriptografada = np.array(linhas)

    # K = ( D^-1 * C)^T , em que K é a matriz chave, D a dos blocos descriptografados e C a dos blocos criptografados
    MatrizChave = np.transpose(cript.InversaModular(MatrizDescriptografada, cript.modulo) @ MatrizCriptografada)
    return cript.Modular(MatrizChave, cript.modulo)



Cifra = cript.CifraHill("CriptografiaHill")

blocos_descriptografados = ["Enzo", "sabo", "sexo", "paes"]
blocos_criptografados = [Cifra.Criptografar(mensagem) for mensagem in blocos_descriptografados]



print(Cifra.Matriz)

print(Decifrar(blocos_descriptografados, blocos_criptografados))