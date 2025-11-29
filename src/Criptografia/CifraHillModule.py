from .AlgoritmoCriptografiaModule import AlgoritmoCriptografia
from src.AlgebraModular import MatrizModular
from bidict import bidict
from sympy import isprime

#Classe para implementar o algoritmo específico da Cifra de Hill
class CifraHill(AlgoritmoCriptografia):

    
    def __init__(self, alfabeto, senha):
        
        self.modulo = len(alfabeto)
        
        if not isprime(self.modulo) :
            raise ValueError("Modulo precisa ser primo")
        self.senha = senha
        
        # Cria um dicionario bidirecional, mapeando cada caractere (key) a um valor numérico (value) até N°Modulo-1
        # Exemplo: {'A':0, 'B':1, ... 'N': N°Modulo-1}
        self.dicionario =bidict(zip(alfabeto, range(self.modulo)))
        
        # Calcula o menor quadrado perfeito maior ou igual ao tamanho da senha, pois a matriz senha precisa ser quadrada para ser invertível
        n = 0
        while(pow(n, 2)<len(self.senha)):
            n += 1

        # Adiciona o último caractere do alfabeto ao final da senha até completar esse valor, como um preenchimento (escolha arbitrária)
        for _ in range( n**2 - len(senha)):
            # Em dicionario.inverse, o caractere corresponde ao valor e o valor numérico do caractere corresponde à chave
            # Exemplo: {0:'A', 1:'B', ... N°Modulo-1 : 'N'}
            
            senha += self.dicionario.inverse[self.modulo - 1]

        # Cria a Matriz a partir da senha, e determina a sua Inversa Modular
        self.Matriz = MatrizModular(senha,self.modulo,[n,n],self.dicionario)
        self.MatrizInversaModular = self.Matriz.InversaModular()
        

    
    def criptografar(self, mensagem):
        
        '''
        Caso o tamanho da mensagem não for um múltiplo inteiro da ordem da Matriz
        Adiciona o primeiro caractere do alfabeto ao final, até esse ser o caso
        '''
        tamanho_mensagem = len(mensagem)
        if tamanho_mensagem%self.Matriz.shape[0] != 0:
            for _ in range(self.Matriz.shape[0] - tamanho_mensagem%self.Matriz.shape[0]):
                mensagem += self.dicionario.inverse[0]

        #representa a mensagem como uma matriz e multiplica esta pela chave para criptografar
        ordem = [self.Matriz.shape[0], len(mensagem)/self.Matriz.shape[0]]
        matriz_mensagem = MatrizModular(mensagem,self.modulo,ordem,self.dicionario)
        matriz_mensagem_criptografada = self.Matriz @ matriz_mensagem
        #converte a matriz resultado em uma string
        mensagem_criptografada = matriz_mensagem_criptografada.ConverterMatrizParaString(self.dicionario)
        return mensagem_criptografada
    
    def descriptografar(self, mensagem):
        if len(mensagem) % self.Matriz.shape[0] != 0:
            raise ValueError("Mensagem de tamanho incompatível com o da senha")
    
        #Representa a mensagem criptografada como uma matriz e a multiplica pela inversa para descriptografar
        ordem = [self.Matriz.shape[0], len(mensagem)/self.Matriz.shape[0]]
        
        matriz_mensagem_criptografada = MatrizModular(mensagem,self.modulo, ordem,self.dicionario)
        matriz_mensagem_descriptografada = self.MatrizInversaModular @ matriz_mensagem_criptografada

        mensagem_descriptografada = matriz_mensagem_descriptografada.ConverterMatrizParaString(self.dicionario)

        # Remove os caracteres adicionados à mensagem original
        while True:
            n = len(mensagem_descriptografada)
            if mensagem_descriptografada[n-1] == self.dicionario.inverse[0] :
                mensagem_descriptografada = mensagem_descriptografada[:-1]
            else:
                break

        return mensagem_descriptografada