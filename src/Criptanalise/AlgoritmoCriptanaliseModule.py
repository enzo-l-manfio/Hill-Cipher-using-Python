from abc import ABC, abstractmethod

#Classe para representar um algoritmo de decifração qualquer

class AlgoritmoCriptanalise:

    @abstractmethod
    def Decifrar(self, textoCriptografado: list, textoDescriptografado: list = None) -> list:
        pass