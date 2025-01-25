class ContaBancaria:
    def __init__(self, titular='', saldo=0, ativo=False):
        self.titular = titular
        self.saldo = saldo
        self._ativo = ativo

    def __str__(self):
        return f'Conta de {self.titular} - Saldo: R${self.saldo}'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

    

conta1 = ContaBancaria("João", 1000)
conta2 = ContaBancaria("Maria", 500)
print(conta1)
print(conta2)

conta3 = ContaBancaria("Carlos", 200)
print(f"Antes de ativar: Conta ativa? {conta3._ativo}")
ContaBancaria.ativar_conta(conta3)
print(f"Depois de ativar: Conta ativa? {conta3._ativo}")