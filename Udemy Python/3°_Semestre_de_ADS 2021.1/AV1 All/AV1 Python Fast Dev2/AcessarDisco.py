class AcessarDisco:
    nome_do_arquivo = ''
    dados = {}

    def escolher_arquivo(self, nome_arquivo):
        self.nome_do_arquivo = nome_arquivo

    def salva(self, lista, nome_do_arquivo):
        self.dados = lista
        if nome_do_arquivo == 'funcionario':
            with open('funcionario.txt', "a") as file_open:
                file_open.write(f'{self.dados}')
                file_open.close()
        elif nome_do_arquivo == 'departamento':
            with open('departamento.txt', "a") as file_open:
                file_open.write(f'{self.dados}')
                file_open.close()
        elif nome_do_arquivo == 'gerente':
            with open('gerente.txt', "a") as file_open:
                file_open.write(f'{self.dados}')
                file_open.close()

    def abrir(self):
        convert = []
        if self.nome_do_arquivo == 'funcionario':
            file_open = open('funcionario.txt')
            for file_line in file_open:
                convert.append(file_line.rstrip())
            return convert
        elif self.nome_do_arquivo == 'departamento':
            file_open = open('departamento.txt')
            for file_line in file_open:
                convert.append(file_line)
            return convert
        elif self.nome_do_arquivo == 'gerente':
            file_open = open('gerente.txt')
            for file_line in file_open:
                convert.append(file_line)
            return convert
        else:
            return print('Arquivo Não selecionado')
