def criar_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def depositar(conta, valor):
    conta["saldo"] += valor

def sacar(conta, valor):
    conta["saldo"] -= valor

def consultar_extrato(conta):
    print("Saldo é {}". format(conta["saldo"]))


#>>> from teste import cria_conta
#>>> conta = cria_conta(123, "Nico", 55.0, 1000)
#>>> conta
#{'numero': 123, 'titular': 'Nico', 'saldo': 55.0, 'limite': 1000}
#>>> conta["numero"]
#123
#>>>
