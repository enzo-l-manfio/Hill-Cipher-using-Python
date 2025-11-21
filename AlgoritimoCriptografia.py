from abc import ABC, abstractmethod

class AlgoritimoCriptografia:
    @abstractmethod
    def criptografar(self, texto: str) -> str:
        pass

    @abstractmethod
    def descriptografar(self, texto: str) -> str:
        pass