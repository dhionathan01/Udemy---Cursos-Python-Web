class Pessoa:
    nome = ''
    idade = 0
    peso = 0.0
    altura = 0.0

    def envelhecer(self):
        self.idade = self.idade + 1
        if self.idade < 21:
            self.crescer()

    def engordar(self, peso):
        self.peso = self.peso + peso

    def crescer(self):
        self.altura = self.altura + 0.05

    def emagrecer(self, peso):
        self.peso = self.peso - peso

    def imprimir(self):
        print(f'Nome: {self.nome} idade: {self.idade} peso: {self.peso} altura: {self.altura}')


pessoa = Pessoa()
pessoa.nome = input('Digite o Nome :')
pessoa.idade = int(input('Digite Idade: '))
pessoa.peso = float(input('Digite o peso: '))
pessoa.altura = float(input('Digite a altura: '))
pessoa.crescer()
pessoa.imprimir()
