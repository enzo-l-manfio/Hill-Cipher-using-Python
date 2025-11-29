from src import Criptografo, CifraHill, Decifrador, HillKPA

from string import printable

def main():
    #Caracteres indisponíveis : "`", "{", "|", "}", "~"
    alfabeto = printable[:-11]

    while True:
        print()
        print('Criptógrafo de Hill')
        print()
        print('1 - Criptografar')
        print('2 - Descriptografar')
        print('3 - Decifrar')
        print('0 - Sair')

        try:
            escolha = int(input().strip())
        except ValueError:
            print("Digite uma escolha válida")
            pass

        if escolha == 1 or escolha == 2 :
        
            cifraDeHill = None
            while True:

                # Obtem senha (chave), a qual será utilizada para encriptar/decriptar a mensagem
                senha = input("Digite a senha: ").strip()
                # Cria um objeto CifraDeHill com a senha fornecida, caso essa seja válida.
                try:
                    cifraDeHill = CifraHill(alfabeto, senha)
                    break
                except ValueError as erro:
                    print(f'Erro: {erro}')
                except KeyError as erro:
                    print(f'Erro: Caractere {erro} não suportado')
        
            while True:

                    # Obtem a mensagem a ser encriptada/decriptada
                    mensagem = input("Digite a mensagem: ").strip()

                    # Cria uma Cifra e define a cifra de Hill como o algoritmo a ser utilizado
                    criptografo = Criptografo(cifraDeHill)
                
                    try:
                        if escolha == 1:
                            mensagem_criptografada = criptografo.criptografar(mensagem)
                            print('Mensagem criptografada:', mensagem_criptografada)
                            print()
                            break
                        else:
                            mensagem_descriptografada = criptografo.descriptografar(mensagem)
                            print()
                            print('Mensagem descriptografada:', mensagem_descriptografada, end = '\n')
                            print()
                            break
                    except KeyError as erro:
                        print(f'Erro: {erro}')
                    except ValueError as erro:
                        print(f"Erro: {erro}")
        elif escolha == 3:
            # Cria o algoritmo de decifração Known-Plaintext-Attack para a Cifra de Hill
            algoritmo = HillKPA(alfabeto)
            # Instancia o decifrador
            decifrador = Decifrador(algoritmo)
            while True:
                blocos_criptografados = input("Escreva os blocos criptografados, espaçados: ").split(" ")
                blocos_descriptografados = input("Escreva os seus correspondentes descriptografados, espaçados: ").split(" ")
                try: 
                    possiveis_senhas = decifrador.Decifrar(blocos_criptografados, blocos_descriptografados)
                    if possiveis_senhas:
                        print("Possíveis senhas: ", end = "")
                        for possibilidade in possiveis_senhas:
                            print(f"{possibilidade} ", end="")
                        print()
                    else:
                        print("Nenhuma senha possível determinada")
                    break
                except ValueError as erro:
                    print(f"Erro: {erro}")
                
        elif escolha == 0:
            break
        else:
            print("Digite uma escolha válida")

if __name__=="__main__":
    main()