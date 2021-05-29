import json


class newFuncionario:
    id = None
    nome = None
    matricula = None
    cargo = None
    departamento = None
    salario = None

    def set_id(self, identificador_unico):
        self.id = identificador_unico

    def get_id(self):
        return self.id

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_matricula(self, matricula):
        self.matricula = matricula

    def get_matricula(self):
        return self.matricula

    def set_cargo(self, cargo):
        self.cargo = cargo

    def get_cargo(self):
        return self.cargo

    def set_departamento(self, departamento):
        self.departamento = departamento

    def get_departamento(self):
        return self.departamento

    def set_salario(self, salario):
        self.salario = salario

    def get_salario(self):
        return self.salario

    def calcular_salario_liquido(self):
        salario_liquido = (self.salario * 0.84) * 1.3
        return salario_liquido

    def __str__(self):
        return "{id:" + self.get_id() + \
               ",nome:" + self.get_nome() + \
               ",matricula:" + self.get_matricula() + \
               ",cargo:" + self.get_cargo() + \
               ",departamento:" + self.get_departamento() + \
               ", salario:" + str(self.get_salario())


class Gerente(newFuncionario):
    cargo = None
    salario = None

    def set_cargo(self, cargo):
        self.cargo = cargo

    def get_cargo(self):
        return self.cargo

    def set_salario(self, salario):
        self.salario = salario

    def get_salario(self):
        return self.salario

    def calcular_salario_liquido(self):
        salario_liquido = (self.salario * 0.84) + (self.salario * 0.5)
        return salario_liquido


class Departamento:
    id = None
    nome = None
    gerente = None

    def set_id(self, identificador_unico):
        self.id = identificador_unico

    def get_id(self):
        return self.id

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_gerente(self, gerente):
        self.gerente = gerente

    def get_gerente(self):
        return self.gerente


class FuncionarioDAO:
    dados = {}

    def salva(self, novo_funcionario):
        self.dados[novo_funcionario.get_id()] = novo_funcionario
        with open('funcionario.txt', "a+") as file_open:
            file_open.write(f'{json.dumps(self.dados, default=vars)}\n')
        self.dados.clear()

    def atualizar(self, novo_funcionario):
        self.dados[novo_funcionario.get_id()] = novo_funcionario

    def deletar(self, novo_funcionario):
        del self.dados[novo_funcionario.get_id()]

    def recuperar_por_id(self, chave):
        return self.dados[chave]

    def listar(self):
        with open("funcionario.txt", "r") as file_open:
            print(file_open.read())


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
funcionarioDao.listar()
