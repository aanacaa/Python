class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f' {self._nome} - {self.ano} - {self._likes} Likes'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f' {self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f' {self._nome} - {self.ano} - {self.temporadas} séries -  {self._likes} Likes'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
        #super().__init__(programas)

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)




   #def tamanho(self):
   #     return len(self.programas)


atlanta = Serie('Atlanta', 2018, 2)
vingadores = Filme('vingadores guerra', 2018, 160)
bela = Filme('A Bela e a Fera', 2018, 200)
stranger = Serie('Stranger Things', 2015, 3)

# print(f' {atlanta.nome} - {atlanta.ano} - {atlanta.temporadas} - {atlanta.likes}')

atlanta.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
stranger.dar_likes()
stranger.dar_likes()
bela.dar_likes()
# print(f' {vingadores.nome} -  {vingadores.ano} -  {vingadores.duracao} - {vingadores.likes}')


filmes_series = [vingadores, atlanta, bela, stranger]
playlist_fim_de_semana = Playlist('fds', filmes_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)

print(f'Está? {bela in playlist_fim_de_semana.listagem}')



# lista = [1, 2, 4, 5]
# print(repr(lista))
# lista = [1, 2, 4, 5]
# print(str(lista))


'''from numbers import Complex
class Numero(Complex):
    def __getitem__(self, item):
        super().__getitem__()'''


class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
#    def mostrar_tarefas(self):
#        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Hipster:
    def __str__(self):
        return f'Hipster,  {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum, Hipster):
    pass


#MRO
# PLENO > ALURA > FUNCIONARIOS> CAELUM > FUNCIONARIOS> HIPSTER
# ENTRETANTO TEM O CONCEITO DE GOOD HEAD
# SE CASO PARA REMOVER O mostrar_tarefas  DO ALURA ELE VAI PROCURAR A PROXIMA GOOD HEAD QUE É CAELUM
# ENTÃO IGNORA O FUNCIONARIOS QUE ESTÁ RELACIONADO COM ALURA


jose = Junior('José')
jose.busca_perguntas_sem_resposta()

luan = Pleno('Luan')
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()

luan.mostrar_tarefas()

print(luan)
