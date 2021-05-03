from Funcionario import newFuncionario


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
