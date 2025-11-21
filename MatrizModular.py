import numpy as np

#Herda de np.ndarray
class MatrizModular(np.ndarray):
    
    
    def __new__(cls,input,modulo,ordem = None,dicionario = None):
        
        cls.modulo = modulo
        cls.ordem = ordem

        obj = None

        #Se recebe uma string,converte em matriz modular de ordem especifica
        if(isinstance(input,str)):
            array = cls.ConverterStringParaMatriz(input,ordem,dicionario)
            obj = np.asarray(array).view(cls)

        #Se recebe uma matriz,converte em matriz modular de ordem especifica
        elif(isinstance(input,np.ndarray)):
            obj = np.asarray(input%cls.modulo).view(cls)

        #Se recebe uma list, cria o nd array correspondente e converte-o em modular
        elif(isinstance(input, list)):
            linhas = []
            for linha in input:
                 linhas.append([n%modulo for n in linha])
            array = np.array(linhas)
            obj = np.asarray(array).view(cls)

        else:
            raise TypeError("Input deve ser uma string, uma list ou uma matriz numpy ndarray")
        
        return obj

    def __mul__(self, other):
        tipos_escalares = [int, float, np.float64]
        if type(other) in tipos_escalares:
            #Converte a Matriz Modular em um ndarray, multiplica pela matriz, e transforma o resultado em MatrizModular
            ndarray = self.view(np.ndarray)
            return MatrizModular( ndarray*other, self.modulo)
        else:
            raise TypeError(f"Operação de multiplicação por escalar indefinida para {type(other)}")
        
    def __matmul__(self, other):
        ndarray = self.view(np.ndarray)
        return MatrizModular(ndarray@other, self.modulo)

    '''
    Função para calcular a inversa modular da Matriz. A inversa modular é
    Igual à conjugada vezes o inverso modular do determinante da Matriz.
    A matriz conjugada será igual à matriz inversa convecional multiplicado pelo determinante,
    e, para o cálculo do inverso modular, será considerado que o módulo é primo,
    caso em que o inverso modular do determinante seré igual a este elevado ao modulo menos 2
    '''

    def InversaModular(cls):
            if np.linalg.det(cls) == 0:
                raise ValueError("Matriz nao Invertível")
            
            det_mod = round(np.linalg.det(cls)) % cls.modulo

            if np.gcd(det_mod, cls.modulo) != 1:
                raise ValueError(f"Matriz não invertível para modulo {cls.modulo}")

            adjunta = MatrizModular(np.linalg.inv(cls)*np.linalg.det(cls),cls.modulo)
            inversa = adjunta * pow(det_mod, cls.modulo-2, cls.modulo)
            return inversa

    #função para converter uma string em uma matriz de determinada ordem
    @classmethod
    def ConverterStringParaMatriz(cls,txt,ordem, dicionario):
        ordem = [int(o) for o in ordem]
        tamanho_string = len(txt)
        vetor = [dicionario[letra] for letra in txt]
        for _ in range(int(ordem[0]*ordem[1]-tamanho_string)):
                vetor.append(0)
            
        # Cria a Matriz a partir da senha
        colunas = []
        for j in range(ordem[1]):
            coluna = []
            for i in range(ordem[0]):
                coluna.append(vetor[i + j*ordem[0]] )
            colunas.append(coluna)
        return np.transpose(np.array(colunas))

    def ConverterMatrizParaString(cls,dicionario):
        string = ''
        matriz = np.transpose(cls)
        for coluna in matriz:
            for elemento in coluna:
                string += dicionario.inverse[elemento%cls.modulo]
        return string


