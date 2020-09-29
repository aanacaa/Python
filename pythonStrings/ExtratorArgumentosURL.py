class ExtratorArgumentosURL:
    def __init__(self, url):
        if self.urlEhValida(url):
            self.url = url
        else:
            raise LookupError("Url Inválida!!!")

    @staticmethod #remove o self do parenteses
    def urlEhValida(url):
        if url:
            return True
        else:
            return False

    def extraiArgumentos(self):

        buscaMoedaOrigem = "moedaorigem"
        buscaMoedaDestino = "moedadestino"

        indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem = self.url.find("&")

        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        if moedaOrigem == "moedadestino":
            self.trocaMoedaOrigem()
            indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
            indiceFinalMoedaOrigem = self.url.find("&")
            moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]



        indiceInicialMoedaDestino = self.encontraIndiceInicial(buscaMoedaDestino)
        moedaDestino = self.url[indiceInicialMoedaDestino:]

        return moedaOrigem,moedaDestino

    def encontraIndiceInicial(self, moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada) +1

    def trocaMoedaOrigem(self):
        self.url = self.url.replace("moedadestino", "real", 1)
        print(self.url)