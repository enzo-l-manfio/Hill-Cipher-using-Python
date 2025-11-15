from bidict import bidict
import string


#Caracteres indisponíveis : "`", "{", "|", "}", "~"

caracteres_disponiveis = string.printable[:-11]
modulo = len(caracteres_disponiveis)
dicionario = bidict(zip(range(modulo), caracteres_disponiveis))
print(dicionario[1])
print(dicionario.inverse['1'])
