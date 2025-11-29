
#Classe para implementar um determinado algoritmo de decifração
class Decifrador:
    def __init__(self, algoritmoCriptoanalise):
        self.AlgoritmoCriptanalise = algoritmoCriptoanalise
    
    def Decifrar(self, textoCriptografado: list, textoDescriptografado: list = None) -> list:
        return self.AlgoritmoCriptanalise.Decifrar(textoCriptografado, textoDescriptografado)