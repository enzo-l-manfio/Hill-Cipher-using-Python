import numpy as np
import string
from bidict import bidict

'''
Função para converter uma matriz para modular
'''
def Modular(matriz, modulo):
        linhas = []
        for i in range(matriz.shape[0]):
            linha = []
            for j in range(matriz.shape[1]):
                elemento = round(matriz[i][j]%modulo)
                linha.append(elemento)
            linhas.append(linha)
        return np.array(linhas)

'''
Função para calcular a inversa modular da Matriz. A inversa modular é
Igual à conjugada vezes o inverso modular do determinante da Matriz.
A matriz conjugada será igual à matriz inversa convecional multiplicado pelo determinante,
e, para o cálculo do inverso modular, será considerado que o módulo é primo,
caso em que o inverso modular do determinante seré igual a este elevado ao modulo menos 2
'''
def InversaModular(matriz, modulo):
        modular = Modular(matriz, modulo)
        det_mod = round(np.linalg.det(modular)) % modulo

        if np.gcd(det_mod, modulo) != 1:
            raise ValueError(f"Matriz não invertível para modulo {modulo}")

        adjunta = Modular(np.linalg.inv(matriz)*np.linalg.det(matriz), modulo)
        inversa = adjunta * pow(det_mod, modulo-2, modulo)
        return Modular(inversa, modulo)


#Caracteres indisponíveis : "`", "{", "|", "}", "~"
caracteres_disponiveis = string.printable[:-11]

modulo = len(caracteres_disponiveis)
#cria um dicionario bidirecional, com caracteres como keys e numeros como values
dicionario = bidict(zip(caracteres_disponiveis, range(modulo)))


#função para converter uma string em uma matriz de determinada ordem
def CriarMatrizString(string, ordem):
    tamanho_string = len(string)
    for _ in range(int(ordem[0]*ordem[1]-tamanho_string)):
            string.append("(")
        
    # Cria a Matriz a partir da senha, e determina a sua Inversa Modular
    colunas = []
    for j in range(ordem[1]):
        coluna = []
        for i in range(ordem[0]):
            coluna.append( dicionario[string[i + j*ordem[0]]] )
        colunas.append(coluna)
    return np.transpose(np.array(colunas))

def CriarStringMatriz(matriz):
    string = ''
    for linha in matriz:
        for elemento in linha:
            string += dicionario.inverse[elemento]
    return string


class CifraHill:
    def __init__(self, senha):
        self.senha = list(senha)

        '''
        Calcula o menor quadrado perfeito maior ou igual ao tamanho da senha, n^2,
        E adiciona o caractere ( ao final da senha até completar esse valor,
        Para poder criar uma Matriz Quadrada de ordem n a partir da senha
        '''
        n = 0
        while(pow(n, 2)<len(self.senha)):
            n += 1
        # Cria a Matriz a partir da senha, e determina a sua Inversa Modular
        self.Matriz = CriarMatrizString(self.senha, [n, n])
        if np.linalg.det(self.Matriz) == 0:
            raise ValueError("Matriz nao Invertível")
        self.MatrizInversaModular = InversaModular(self.Matriz, modulo)
    
    def Criptografar(self, mensagem):
        
        '''
        Caso o tamanho da mensagem não for um múltiplo inteiro da ordem da Matriz
        Adiciona o caractere ( ao final, até esse ser o caso
        '''
        tamanho_mensagem = len(mensagem)
        if tamanho_mensagem%self.Matriz.shape[0] != 0:
            for _ in range(self.Matriz.shape[0] - tamanho_mensagem%self.Matriz.shape[0]):
                mensagem += "("

        #representa a mensagem como uma matriz e multiplica esta pela chave para criptografar
        ordem = [int(self.Matriz.shape[0]), int(len(mensagem)/self.Matriz.shape[0])]
        matriz_mensagem = CriarMatrizString(mensagem, ordem)
        matriz_mensagem_criptografada = Modular(self.Matriz @ matriz_mensagem, modulo)

        #converte a matriz resultado em uma string
        mensagem_criptografada = CriarStringMatriz(matriz_mensagem_criptografada)
        return mensagem_criptografada
    
    def Descriptografar(self, mensagem):
        if len(mensagem) % self.Matriz.shape[0] != 0:
             raise ValueError("Mensagem de tamanho incompatível com o da senha")
    
        #Representa a mensagem criptografada como uma matriz e a multiplica pela inversa para descriptografar
        ordem = [int(self.Matriz.shape[0]), int(len(mensagem)/self.Matriz.shape[0])]
        matriz_mensagem_criptografada = CriarMatrizString(mensagem, ordem)
        matriz_mensagem_descriptografada = Modular ( self.MatrizInversaModular @ matriz_mensagem_criptografada, modulo)

        mensagem_descriptografada = CriarStringMatriz(matriz_mensagem_descriptografada)

        # Remove os caracteres ( adicionados à mensagem original
        while True:
            n = len(mensagem_descriptografada)
            if mensagem_descriptografada[n-1] == "(" :
                mensagem_descriptografada = mensagem_descriptografada[:-1]
            else:
                break

        return mensagem_descriptografada