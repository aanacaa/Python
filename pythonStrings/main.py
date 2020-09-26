'''
nome = "RODRIGO"

subString = nome[4]
subString2 = nome[:6]
subString3 = nome[2:6]

print (subString)
print (subString2)
print (subString3)

frase = "Meu nome é Rodrigo e minha idade é 26"
subFrase = frase[35:]
print(subFrase)

argumento = "moedaorigem=real"
index = argumento.find("=")
sub = argumento[index+1:]
print(sub)

listaargumentos = argumento.split("=")
print((listaargumentos))
'''
from ExtratorArgumentosURL import ExtratorArgumentosURL
#url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=700"
url = None
#url = ""

#argumento = ExtratorArgumentosURL(url)
#print(argumento)
#APOS STATIC METHOD
print(ExtratorArgumentosURL.urlEhValida(url))