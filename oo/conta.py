from typing import Any


class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Contruido objeto... {}". format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def consultar(self):
        print("Saldo de R$ {} do titular {}". format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = (self.__saldo + self.__limite)
        return valor_a_sacar <= valor_disponivel_a_sacar

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        print("Chamando @propety saldo()")
        return self.__saldo

    @property
    def titular(self):
        print("Chamando @propety titular()")
        return self.__titular

    @property
    def limite(self):
        print("Chamando @propety limite()")
        return self.__limite

    @limite.setter
    def limite(self, limite):
        print("Chamando @limite.setter limite()")
        self.__limite = limite



#Executar comandos abaixo
#from conta import Conta
#Conta()
#conta = Conta()
#conta
