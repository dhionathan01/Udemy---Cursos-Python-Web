class Pessoa:
    nome = ''
    idade = 0
    sexo = ''
    cpf = ''

    def __init__(self, nome, idade, sexo, cpf):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf


class Funcionario:
    cargo = ''
    salario = 0.0

    def __init__(self, dados_pessoa):
        self.pessoa = dados_pessoa

    def exibir_informacoes(self):
        print(f'Nome: {self.pessoa.nome}')
        print(f'Idade: {self.pessoa.idade}')
        print(f'Sexo:{self.pessoa.sexo}')
        print(f'CPF: {self.pessoa.cpf}')
        print(f'Cargo: {self.cargo}')
        print(f'Salario: {self.salario}')


class Gerente(Funcionario):

    def definir_cargo(self):
        self.cargo = 'Gerente'
        self.salario = 4599.99


class DepartamentoPessoal(Funcionario):
    def definir_cargo(self):
        self.cargo = 'Departamento Pessoal'
        self.salario = 3200.99


class DepartamentoAdministrativo(Funcionario):
    def definir_cargo(self):
        self.cargo = 'Departamento Administrativo'
        self.salario = 4299.99


class Programador(Funcionario):
    def definir_cargo(self):
        self.cargo = 'Programador'
        self.salario = 3800.99


pessoa = Pessoa('Dhionathan Jobim', 18, 'Masculino', '172.334.221-90')
funcionario = Gerente(pessoa)
funcionario.definir_cargo()
funcionario.exibir_informacoes()
