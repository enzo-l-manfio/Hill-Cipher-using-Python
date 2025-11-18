
from Criptografia import CifraHill


while True:

    print('Criptógrafo de Hill')
    print('1 - Criptografar')
    print('2 - Descriptografar')
    print('0 - Sair')
    escolha = int(input().strip())
    match escolha:

        case 1:
            while True:
                senha = input("Digite a senha: ").strip()
                try:
                    criptografo = CifraHill(senha)
                    break
                except ValueError:
                    print('Impossível utilizar a senha digitada, matriz não invertível')
                except KeyError:
                    print('Impossível utilizar a senha digitada, caractere não suportado')
            while True:
                mensagem = input("Digite a mensagem: ").strip()
                try:
                    mensagem_criptografada = criptografo.Criptografar(mensagem)
                    print()
                    print('Mensagem criptografada:', mensagem_criptografada, end = '\n')
                    print()
                    break
                except KeyError:
                    print('Impossível criptografar a mensagem digitada, caractere não suportado')
            
        
        case 2:
            while True:
                senha = input("Digite a senha: ").strip()
                try:
                    criptografo = CifraHill(senha)
                    break
                except ValueError:
                    print('Impossível utilizar a senha digitada, matriz não invertível')
            while True:
                try:
                    mensagem_criptografada = input("Digite a mensagem criptografada: ").strip()
                    mensagem_descriptografada = criptografo.Descriptografar(mensagem_criptografada)
                    print()
                    print('Mensagem descriptografada:', mensagem_descriptografada)
                    print()
                    break
                except KeyError:
                    print('Impossível criptografar a mensagem digitada, caractere não suportado')

        case 0:
            break
