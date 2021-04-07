class BombadeCombustivel:
    tipoCombustivel = ''
    valorLitro = 0.0
    quantidadeCombustivel = 300

    def tipo_combustivel(self, tipo):
        if tipo == 'Comum':
            self.tipoCombustivel = 'Comum'
            self.valorLitro = 3.50
        elif tipo == 'Etanol':
            self.tipoCombustivel = 'Etanol'
            self.valorLitro = 4.00

    def abastecer_por_valor(self, valorpago):
        quantidade_combustivel_pedido = valorpago / self.valorLitro
        print(f'Quantidade de Combustivel: {quantidade_combustivel_pedido}')
        posto.__alterar_quantidade_combustivel(quantidade_combustivel_pedido)

    def abastecer_por_litro(self, litros):
        preco = litros * self.valorLitro
        print(f'Valor a ser Pago: {preco}')
        posto.__alterar_quantidade_combustivel(litros)

    def alterar_valor(self, valor):
        self.valorLitro = valor

    def alterar_combustivel(self, tipo):
        self.tipoCombustivel = tipo

    def __alterar_quantidade_combustivel(self, valor):
        self.quantidadeCombustivel = self.quantidadeCombustivel - valor

    def imprimir_quantidade_combustivel_restante(self):
        print(self.quantidadeCombustivel)


posto = BombadeCombustivel()
posto.tipo_combustivel(input('Insira o Tipo de Combustivel "Comum" ou "Etanol": '))
opcao = (input('Deseja Abaster por "Litro" ou por "Valor": '))
if opcao == 'Litro':
    posto.abastecer_por_litro(float(input('Quantos Litros deseja abastecer ? ')))
elif opcao == 'Valor':
    posto.abastecer_por_valor(float(input('Qual valor em R$ de Combustivel deseja abastecer ?')))

posto.imprimir_quantidade_combustivel_restante()
