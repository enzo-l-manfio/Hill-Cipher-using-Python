import numpy as np

class Cifra:
    def __init__(self, senha_criptacao, senha_descriptacao, algoritmo_criptacao, algoritmo_descriptacao):
        self.senha_criptacao = senha_criptacao
        self.senha_descriptacao = senha_descriptacao
        self.algoritmo_criptacao = algoritmo_criptacao
        self.algoritmo_descriptacao = algoritmo_descriptacao
    def Criptografar(self, mensagem):
        return self.algoritmo_criptacao(self.senha_criptacao, mensagem)
    def Descriptografar(self, mensagem):
        return self.algoritmo_descriptacao(self.senha_descriptacao, mensagem)



#Função para converter caracteres em números
def pos(x):
    return ord(x) - 38

#Função para converter números em caracteres
def char(x):
    return chr((round(x)+89)%89 + 38)

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



def CriptografarHill(Matriz, mensagem):
    #Converte os caracteres da mensagem para números
    vetor_mensagem = [pos(letra) for letra in mensagem]

    '''
    Caso o tamanho da mensagem não for um múltiplo inteiro da ordem da Matriz
    Adiciona o caractere ( ao final, até esse ser o caso
    '''
    tamanho_vetor_i = len(vetor_mensagem)
    if tamanho_vetor_i%Matriz.shape[0] != 0:
        for _ in range(Matriz.shape[0] - tamanho_vetor_i%Matriz.shape[0]):
            vetor_mensagem.append(pos("("))

    '''
    Como uma Matriz de ordem n só pode multiplicar um vetor com n elementos,
    o vetor mensagem será dividido em múltiplos vetores de ordem n, os quais serão
    multiplicados pela Matriz e reagrupados para formar a mensagem criptografada
    '''
    vetor_mensagem_criptografada = []
    for i in range(int(len(vetor_mensagem) / Matriz.shape[0])):
        vetor_i = []
        for j in range(Matriz.shape[0]):
            vetor_i.append(vetor_mensagem[j + i*Matriz.shape[0]])
        vetor_f = Matriz @ vetor_i
        vetor_mensagem_criptografada += [x for x in vetor_f]

    mensagem_criptografada = ""
    for n in vetor_mensagem_criptografada:
        mensagem_criptografada += char(n)
    return mensagem_criptografada

def DescriptografarHill(MatrizInversaModular, mensagem):
    vetor_mensagem = [pos(letra) for letra in mensagem]
    mensagem_descriptografada = ""

    '''
    Divide o vetor mensagem em múltiplos vetores de ordem n,
    multiplica eles pela Inversa, e adiciona os caracteres correspondentes
    aos seus respectivos elementos numéricos para formar a mensagem original
    '''
    for i in range(int(len(vetor_mensagem) / MatrizInversaModular.shape[0])):
        vetor_i = []
        for j in range(MatrizInversaModular.shape[0]):
            vetor_i.append(vetor_mensagem[j + i*MatrizInversaModular.shape[0]])
        vetor_f = MatrizInversaModular @ vetor_i
        for x in vetor_f:
            mensagem_descriptografada += char(x)

    # Remove os caracteres ( adicionados à mensagem original
    while True:
        n = len(mensagem_descriptografada)
        if mensagem_descriptografada[n-1] == "(" :
            mensagem_descriptografada = mensagem_descriptografada[:-1]
        else:
            break

    return mensagem_descriptografada



class CifraHill(Cifra):
    def __init__(self, senha):
        senha = [letra for letra in senha]
        '''
        Calcula o menor quadrado perfeito maior ou igual ao tamanho da senha, n^2,
        E adiciona o caractere ( ao final da senha até completar esse valor,
        Para poder criar uma Matriz Quadrada de ordem n a partir da senha
        '''
        n = 0
        tamanho_senha = len(senha)
        while(pow(n, 2)<tamanho_senha):
            n += 1
        for _ in range(pow(n, 2)-tamanho_senha):
            senha.append("(")
        
        # Cria a Matriz a partir da senha, e determina a sua Inversa Modular
        linhas = []
        i = 0
        while (i<pow(n, 2)):
            linha=[]
            for j in range(n):
                c = pos(senha[i+j])
                linha.append(c)
            linhas.append(linha)
            i+=n
        Matriz = np.array(linhas)
        if np.linalg.det(Matriz) == 0:
            raise ValueError("Matriz nao Invertível")
        MatrizInversaModular = InversaModular(Matriz, 89)

        Cifra.__init__(self, Matriz, MatrizInversaModular, CriptografarHill, DescriptografarHill)