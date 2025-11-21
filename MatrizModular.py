import numpy as np
import string




#Herda de np.ndarray
class MatrizModular(np.ndarray):
    
    

   

    
    def __new__(cls,input,modulo,ordem = None,dicionario = None):
        
        
        cls.modulo = modulo
        cls.ordem = ordem

        obj = None
        #Se recebe uma string,converte em matriz modular de ordem especifica
        if(isinstance(input,str)):
            obj = np.asarray(cls.Modular(cls.ConverterStringParaMatriz(cls=cls,txt=input,ordem=ordem,dicionario=dicionario),modulo)).view(cls)
        #Se recebe uma matriz,converte em matriz modular de ordem especifica
        elif(isinstance(input,np.ndarray)):
            obj = np.asarray(cls.Modular(input,modulo)).view(cls)
        else:
            raise TypeError("Input deve ser uma string ou uma matriz numpy ndarray")
        
        return obj
    
    
    
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
    def InversaModular(cls):
            if np.linalg.det(cls) == 0:
                raise ValueError("Matriz nao Invertível")
            
            det_mod = round(np.linalg.det(cls)) % cls.modulo

            if np.gcd(det_mod, cls.modulo) != 1:
                raise ValueError(f"Matriz não invertível para modulo {cls.modulo}")

            adjunta = MatrizModular(np.linalg.inv(cls)*np.linalg.det(cls),cls.modulo)
            inversa = adjunta * pow(det_mod, cls.modulo-2, cls.modulo)
            return MatrizModular(inversa,cls.modulo)




    #função para converter uma string em uma matriz de determinada ordem
    def ConverterStringParaMatriz(cls,dicionario,txt,ordem):
        ordem = [int(o) for o in ordem]
        tamanho_string = len(txt)
        for _ in range(int(ordem[0]*ordem[1]-tamanho_string)):
                txt.append("(")
            
        # Cria a Matriz a partir da senha
        colunas = []
        for j in range(ordem[1]):
            coluna = []
            for i in range(ordem[0]):
                coluna.append(dicionario[txt[i + j*ordem[0]]] )
            colunas.append(coluna)
        return np.transpose(np.array(colunas))

    def ConverterMatrizParaString(cls,dicionario):
        string = ''
        matriz = np.transpose(cls)
        for coluna in matriz:
            for elemento in coluna:
                string += dicionario.inverse[elemento%cls.modulo]
        return string


