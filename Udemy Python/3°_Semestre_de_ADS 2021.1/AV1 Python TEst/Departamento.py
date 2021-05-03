
class Departamento:
    _id = None
    _nome = None
    _gerente = None
    _status_caixa = 'Close'
    _dinheiro_em_caixa = 0
    _troco = 0
    _numero_de_vendas = 0

    def set_id(self, identificador_unico):
        self._id = identificador_unico

    def get_id(self):
        return self._id

    def set_nome(self, nome):
        self._nome = nome

    def get_nome(self):
        return self._nome

    def set_gerente(self, gerente):
        self._gerente = gerente

    def get_gerente(self):
        return self._gerente

    def set_status_caixa(self, caixa):
        self._status_caixa = caixa

    def get_status_caixa(self):
        return self._status_caixa

    def set_dinheiro_caixa(self, dinheiro):
        self._dinheiro_em_caixa = dinheiro

    def get_dinheiro_caixa(self):
        return self._dinheiro_em_caixa

    def set_troco(self, troco):
        self._troco = troco

    def get_troco(self):
        return self._troco

    def set_numero_de_vendas(self, numero_vendas):
        self._numero_de_vendas = numero_vendas

    def get_numero_de_vendas(self):
        return self._numero_de_vendas

    def abrir_caixa(self, troco, status_caixa='open'):
        self._troco = troco
        self._status_caixa = str(status_caixa).title()
        self.set_dinheiro_caixa(self.get_dinheiro_caixa() + self.get_troco())

    def __calcular_montante(self):
        print(f'Montante/Lucro: {self.get_dinheiro_caixa() - self.get_troco()}\n')

    def registar_venda(self, quantidade, valor):
        if self._status_caixa == 'Open':
            self.set_dinheiro_caixa(self.get_dinheiro_caixa() + (quantidade * valor))
            self.set_numero_de_vendas(self.get_numero_de_vendas() + 1)
        else:
            print('Caixa está Fechado')

    def fechar_caixa(self, status_caixa='Close'):
        self._status_caixa = str(status_caixa).title()
        print(f'Número de Vendas: {self.get_numero_de_vendas()}, \n'
              f'Valor Total em Caixa: {self._dinheiro_em_caixa}')
        self.__calcular_montante()


class DepartamentoDOA:
    dados = {}

    def salva(self, departamento):
        self.dados[departamento.get_id()] = departamento

    def atualizar(self, departamento):
        self.dados[departamento.get_id()] = departamento

    def deletar(self, departamento):
        del self.dados[departamento.get_id()]

    def recuperar_por_id(self, chave):
        return self.dados[chave]

    def listar(self):
        return self.dados
