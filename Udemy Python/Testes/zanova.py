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
        return "funcionario:{id=" + self.get_id() + ",nome=" + self.get_nome() + ",cargo:" + self.get_cargo()


class Gerente(newFuncionario):
    _cargo = None
    _salario = None

    def set_cargo(self, cargo):
        self._cargo = cargo

    def get_cargo(self):
        return self._cargo

    def set_salario(self, salario):
        self._salario = salario

    def get_salario(self):
        return self._salario

    def calcular_salario_liquido(self):
        salario_liquido = (self._salario * 0.84) + (self._salario * 0.5)
        return salario_liquido


class Departamento:
    _id = None
    _nome = None
    _gerente = None

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


class FuncionarioDAO:
    dados = {}

    def salva(self, novo_funcionario):
        self.dados[novo_funcionario.get_id()] = novo_funcionario

    def atualizar(self, novo_funcionario):
        self.dados[novo_funcionario.get_id()] = novo_funcionario

    def deletar(self, novo_funcionario):
        del self.dados[novo_funcionario.get_id()]

    def recuperar_por_id(self, chave):
        return self.dados[chave]

    def listar(self):
        return self.dados


class GerenteDAO:
    dados = {}

    def salva(self, novo_funcionario):
        self.dados[novo_funcionario.get_id()] = novo_funcionario

    def atualizar(self, novo_funcionario):
        self.dados[novo_funcionario.get_id()] = novo_funcionario

    def deletar(self, novo_funcionario):
        del self.dados[novo_funcionario.get_id()]

    def recuperar_por_id(self, chave):
        return self.dados[chave]

    def listar(self):
        return self.dados


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


funcionario = newFuncionario()
funcionario.set_id('01')
funcionario.set_nome('Dhionathan')
funcionario.set_matricula('332131551')
funcionario.set_departamento('Vendas')
funcionario.set_cargo('Vendedor')
funcionario.set_salario(3500.21)

funcionarioDao = FuncionarioDAO()
funcionarioDao.salva(funcionario)

funcionario2 = newFuncionario()
funcionario2.set_id('02')
funcionario2.set_nome('Sara')
funcionario2.set_matricula('5543')
funcionario2.set_departamento('Vendas')
funcionario2.set_cargo('Vendedor')
funcionario2.set_salario(3500.21)

funcionarioDao.salva(funcionario2)
print(funcionarioDao.recuperar_por_id('01').__str__())

funcionario3 = newFuncionario()
