import AlgoritimoCriptografia

class GerenciadorDeCriptografia:

    def __init__(self,AlgoritimoCriptografia: AlgoritimoCriptografia):
        self.algoritimo = AlgoritimoCriptografia

    def criptografar(self, mensagem: str) -> str:
        return self.algoritimo.criptografar(mensagem)    

    def descriptografar(self, mensagem: str) -> str:    
        return self.algoritimo.descriptografar(mensagem)