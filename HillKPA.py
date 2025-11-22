from AlgoritmoCriptanalise import AlgoritmoCriptanalise
from MatrizModular import MatrizModular
from bidict import bidict
import numpy as np

class HillKPA(AlgoritmoCriptanalise):
    def __init__(self, alfabeto):
        self.modulo = len(alfabeto)
        self.dicionario = bidict(zip(alfabeto, range(self.modulo)))

    def Decifrar(self, blocos_criptografados, blocos_descriptografados):
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

        for n in (self.divisores(mdc)) :

            if len(conjunto_descriptografado) < n**2:
                continue
        
            MatrizDescriptografada = MatrizModular(conjunto_descriptografado, self.modulo, [n, n], self.dicionario)
            MatrizCriptografada = MatrizModular(conjunto_criptografado, self.modulo, [n, n], self.dicionario)

            # K = C * D^-1 , em que K é a matriz chave, D a dos blocos descriptografados e C a dos blocos criptografados
            try:
                MatrizChave = MatrizCriptografada @ MatrizDescriptografada.InversaModular()
                ordem = [n, len(conjunto_criptografado)//n]
            except ValueError:
                pass

            #Verifica a consistência do resultado
            D = MatrizModular(conjunto_descriptografado, self.modulo, ordem, self.dicionario)
            C = MatrizModular(conjunto_criptografado, self.modulo, ordem, self.dicionario)
            matrizProduto = MatrizChave @ D
            if np.array_equal(matrizProduto, C) :
                possiveis_matrizes.append(MatrizChave)
        #Armazena as possíveis matrizes como strings
        possiveis_senhas = [matriz.ConverterMatrizParaString(self.dicionario) for matriz in possiveis_matrizes]

        return possiveis_senhas

    @classmethod
    def divisores(cls, n):
        divisores = []
        for i in range(1, n+1):
            if n%i != 0 :
                continue
            else:
                divisores.append(i)
        return divisores