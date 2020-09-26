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
