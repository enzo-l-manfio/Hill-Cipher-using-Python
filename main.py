from Criptografo import Criptografo
from CifraHill import CifraHill
import string


#Caracteres indisponíveis : "`", "{", "|", "}", "~"
alfabeto = string.printable[:-11]


while True:

    print('Criptógrafo de Hill')
    print('1 - Criptografar')
    print('2 - Descriptografar')
    print('0 - Sair')
    escolha = int(input().strip())

    if escolha == 1 or escolha == 2 :
        
        cifraDeHill = None
        while True:

            # Obtem senha (chave), a qual será utilizada para encriptar/decriptar a mensagem
            senha = input("Digite a senha: ").strip()
            # Cria um objeto CifraDeHill com a senha fornecida, caso essa seja válida.
            try:
                cifraDeHill = CifraHill(alfabeto, senha)
                break
            except ValueError:
                print('Impossível utilizar a senha digitada, matriz não invertível')
            except KeyError:
                print('Impossível utilizar a senha digitada, caractere não suportado')
        
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
                except KeyError:
                    print('Impossível criptografar/descriptografar a mensagem digitada, caractere não suportado')
                except ValueError:
                    print("Impossível descriptografar a mensagem digitada, tamanho da senha e mensagem incompatíveis")
    elif escolha == 0 :
        break