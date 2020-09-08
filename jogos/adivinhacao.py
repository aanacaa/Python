import random

def jogar():
    print(30*"*")
    print("Bem vindo ao jogo de adivinhação")
    print(30*"*")
    #print("Em {} o Carnaval acontece em {} do dia {} até o dia {}".format(ano, mes, dia_ini, dia_fim))
    """Comentários"""
    #Comentários



    #Mais sobre strings:
    #"Tentativa {1} de {0}".format(2,10)
    #"R$ {}".format(1.59)
    #"R$ {:f}".format(1.59)
    #"R$ {:.2f}".format(1.5) - dois digitos depois do .
    #"R$ {:7.2f}".format(1.5) - 7 digitos no total
    #"R$ {:07.2f}".format(1.5) - colocar zero na frente
    #"R$ {:07d}".format(1) - para inteiro é d
    #"R$ {:7d}".format(1) - deixa vazio na frente
    #"Data {:02d}/{:02d}".format(5,10) - Para formatar datas
    #"Data {:02d}/{:02d}/{:04d}".format(5,10,1994) - Para formatar data e ano
    #"R$ {:7.1f}".format(1000.15)
    ######No Python 3.6+
    #Esse recurso é chamado de f-strings ou formatted string literals.
    #print(f'Meu nome é {nome}')
    #print(f'Meu nome é {nome.lower()}')


    #numero_secreto = 42
    #numero_secreto = round(random.random()* 100) # gera entre 0.0 e 1.0 por isso multiplicamos por 100
    #random.seed(100)
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000
    print(numero_secreto)

    print("Qual nivel de dificuldade?")
    print("(1) Facil - (2) Médio - (3) Difícil")
    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    #rodada = 1
    #while rodada <= total_de_tentativas:
    for rodada in range(1, total_de_tentativas + 1):

        print("Tentativa {} de {} :".format(rodada, total_de_tentativas)) # interpolação de string

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)
        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100 ")
            continue


        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("Você errou! Seu número foi maior")

            elif menor:
                print("Você errou! Seu número foi menor")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        #rodada = rodada + 1
    print("Fim do jogo")


if __name__ =="__main__":
    jogar()