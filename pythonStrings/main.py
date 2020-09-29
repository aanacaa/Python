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
url = “https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar”
'''
from ExtratorArgumentosURL import ExtratorArgumentosURL
url = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar"
#-- Aula Empty e none
#url = None
#url = ""
#argumento = ExtratorArgumentosURL(url)
#print(argumento)
#APOS STATIC METHOD
#print(ExtratorArgumentosURL.urlEhValida(url))


#---- Aula extrai argumentos

#index = url.find("moedadestino") + len("moedadestino") +1
#substring = url[index:]
#print(substring)


argumentosUrl = ExtratorArgumentosURL(url)
moedaOrigem, moedaDestino = argumentosUrl.extraiArgumentos()
print(moedaOrigem, moedaDestino)





