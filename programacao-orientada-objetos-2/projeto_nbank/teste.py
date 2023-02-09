from conta import *
from banco import Banco

banco = Banco() #criando instancia do banco

# Objetos com numero da conta, cliente, sobrenome, cpf e saldo

c1 = Conta('777', 'Natan','111','Santos','1234', 1000)
c2 = Conta('888', 'David','222','Ribeiro','4321', 1000)

# Deposito e Saque

# c1.deposita(float(input('Digite o valor de deposito: ')))
# c1.saca(float(input('Digite o valor de saque: ')))

# Transferencia entre contas

c1.transfere(c2, 500) 
c2.transfere(c1,100)

# c1.extrato()
# c1._historico.imprime()
# c2._historico.imprime()
# print('Contas criadas no dia: {}'.format(datetime.datetime.today().strftime('%Y-%m-%d %H:%M')))
# print('Total de contas criadas: {}'.format(Conta.get_total_contas()))

#adicionando contas ao banco (True para conta adicionada e False para conta com CPF ja adicionada)

print(banco.adicionar_conta(c1))
print(banco.adicionar_conta(c2))


banco.imprime() # imprime o Nome e CPF de todas as contas adicionadas ao banco

# executando teste de try/except

c1.deposita("AAA") # entrando com string onde devia ser int/float
c1.saca("AAA") # entrando com string onde devia ser int/float