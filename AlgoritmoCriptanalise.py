from abc import ABC, abstractmethod

class AlgoritmoCriptanalise:

    @abstractmethod
    def Decifrar(self, textoCriptografado: list, textoDescriptografado: list = None) -> list:
        pass