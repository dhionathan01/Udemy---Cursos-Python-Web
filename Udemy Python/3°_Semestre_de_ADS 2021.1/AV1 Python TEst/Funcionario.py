
class newFuncionario:
    _id = None
    _nome = None
    _matricula = None
    _cargo = None
    _departamento = None
    _salario = None

    def set_id(self, identificador_unico):
        self._id = identificador_unico

    def get_id(self):
        return self._id

    def set_nome(self, nome):
        self._nome = nome

    def get_nome(self):
        return self._nome

    def set_matricula(self, matricula):
        self._matricula = matricula

    def get_matricula(self):
        return self._matricula

    def set_cargo(self, cargo):
        self._cargo = cargo

    def get_cargo(self):
        return self._cargo

    def set_departamento(self, departamento):
        self._departamento = departamento

    def get_departamento(self):
        return self._departamento

    def set_salario(self, salario):
        self._salario = salario

    def get_salario(self):
        return self._salario

    def calcular_salario_liquido(self):
        salario_liquido = (self._salario * 0.84) * 1.3
        return salario_liquido

    def __str__(self):
        return "{id:" + self.get_id() + \
               ",nome:" + self.get_nome() + \
               ",matricula:" + self.get_matricula() + \
               ",cargo:" + self.get_cargo() + \
               ",departamento:" + self.get_departamento() + \
               ", salario:" + str(self.get_salario())


class FuncionarioDAO:
    dados = {}

    def atualizar(self, novo_funcionario):
        self.dados[novo_funcionario.get_id()] = novo_funcionario

    def deletar(self, novo_funcionario):
        del self.dados[novo_funcionario.get_id()]

    def recuperar_por_id(self, chave):
        return self.dados[chave]

