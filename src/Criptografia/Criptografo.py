from .AlgoritmoCriptografia import AlgoritmoCriptografia

class Criptografo:

    def __init__(self,AlgoritimoCriptografia: AlgoritmoCriptografia):
        self.algoritimo = AlgoritimoCriptografia

    def criptografar(self, mensagem: str) -> str:
        return self.algoritimo.criptografar(mensagem)    

    def descriptografar(self, mensagem: str) -> str:    
        return self.algoritimo.descriptografar(mensagem)