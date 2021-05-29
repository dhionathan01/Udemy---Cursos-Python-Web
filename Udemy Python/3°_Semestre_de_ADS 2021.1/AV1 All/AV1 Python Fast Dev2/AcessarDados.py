class AcessarDados:
    dados = {}
    nome_arquivo = None

    def escolher_arquivo(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def Leitura(self):
        leitura = []
        if self.nome_arquivo == 'funcionario':
            file_open = open('funcionario.txt')
            for file_line in file_open:
                leitura.append(file_line)
            return leitura
        elif self.nome_arquivo == 'departamento':
            file_open = open('departamento.txt')
            for file_line in file_open:
                leitura.append(file_line)
            return leitura
        elif self.nome_arquivo == 'gerente':
            file_open = open('gerente.txt')
            for file_line in file_open:
                leitura.append(file_line)
            return leitura
        else:
            return print('Arquivo Não selecionado')

    def listar(self):
        if self.nome_arquivo == 'funcionario':
            with open("funcionario.txt", "r") as file_open:
                file_content = file_open.read()
                fragmentar = file_content.split('\n')
                return fragmentar
        elif self.nome_arquivo == 'gerente':
            with open("gerente.txt", "r") as file_open:
                file_content = file_open.read()
                fragmentar = file_content.split('\n')
                return fragmentar
        elif self.nome_arquivo == 'departamento':
            with open("departamento.txt", "r") as file_open:
                file_content = file_open.read()
                fragmentar = file_content.split('\n')
                return fragmentar
