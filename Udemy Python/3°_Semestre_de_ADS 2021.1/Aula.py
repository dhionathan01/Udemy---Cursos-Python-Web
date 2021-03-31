class Conta:
  numero = 000
  saldo = 0
  nome = ""
  def __init__(self, numero, saldoInicial):
    self.numero = numero
    self.saldo = saldoInicial
  def deposito(self, saldo):
    self.saldo += saldo
  def saque(self,valor):
    if self.saldo > 0 and self.saldo >= valor:
      self.saldo -= valor
    else:
      print("Saldo Insuficiente")
conta = Conta(1234,10)
conta.deposito(20)
conta.deposito(30)
conta.saque(40)
conta.saque(15)
print(conta.saldo)