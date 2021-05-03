import json


class AcessarDisco:
    nome_do_arquivo = ''
    dados = {}

    def salva(self, lista, nome_do_arquivo):
        self.dados = lista
        if nome_do_arquivo == 'funcionario':
            with open('funcionario.txt', "a") as file_open:
                file_open.write(f'{json.dumps(self.dados, default=vars)}\n')
                file_open.close()
        elif nome_do_arquivo == 'departamento':
            with open('departamento.txt', "a") as file_open:
                file_open.write(f'{json.dumps(self.dados, default=vars)}\n')
                file_open.close()
        elif nome_do_arquivo == 'departamento':
            with open('departamento.txt', "a") as file_open:
                file_open.write(f'{json.dumps(self.dados, default=vars)}\n')
                file_open.close()
