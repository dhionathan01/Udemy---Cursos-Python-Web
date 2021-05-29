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

    def __str__(self):
        return f'id: {self.get_id()}, ' \
               f'nome:  {self.get_nome()}, ' \
               f'matricula:  {self.get_matricula()}, ' \
               f'cargo:  {self.get_cargo()}, ' \
               f'departamento:  {self.get_departamento()}, ' \
               f'salario: {str(self.get_salario())} ,' \
               f'; \n'


class GerenteDAO:
    dados = {}

    def salva(self, gerente):
        self.dados[gerente.get_id()] = gerente

    def atualizar(self, gerente):
        self.dados[gerente.get_id()] = gerente

    def deletar(self, gerente):
        del self.dados[gerente.get_id()]

    def recuperar_por_id(self, chave):
        return self.dados[chave]

    def listar(self):
        return self.dados
