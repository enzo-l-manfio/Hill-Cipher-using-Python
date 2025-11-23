from abc import ABC, abstractmethod

class AlgoritmoCriptografia:
    @abstractmethod
    def criptografar(self, texto: str) -> str:
        pass

    @abstractmethod
    def descriptografar(self, texto: str) -> str:
        pass