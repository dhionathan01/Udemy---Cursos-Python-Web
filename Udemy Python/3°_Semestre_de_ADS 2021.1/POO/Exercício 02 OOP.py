class BombadeCombustivel:
    tipoCombustivel = ''
    valorLitro = 0.0
    quantidadeCombustivel = 0

    def __init__(self, tipocombustivel, valorlitro, quantidadecombustivel):
        self.tipoCombustivel = tipocombustivel
        self.valorLitro = valorlitro
        self.quantidadeCombustivel = quantidadecombustivel

    def tipo_combustivel(self, tipo):
        if tipo == 'Gasolina Comum':
            self.tipoCombustivel = 'Comum'
            self.valorLitro = 3.50
        elif tipo == 'Gasolina Aditivada':
            self.tipoCombustivel = 'Etanol'
            self.valorLitro = 4.00

    def abastecer_por_valor(self, valorpago):
        quantidade_combustivel_pedido = valorpago / self.valorLitro
        print(f'Qtd Combustivel: {quantidade_combustivel_pedido}')
        posto.__alterar_quantidade_combustivel(quantidade_combustivel_pedido)

    def abastecer_por_litro(self, litros):
        preco = litros * self.valorLitro
        print(f'Total Pagar: {preco}')
        posto.__alterar_quantidade_combustivel(litros)

    def alterar_valor(self, valor):
        self.valorLitro = valor

    def alterar_combustivel(self, tipo):
        self.tipoCombustivel = tipo

    def __alterar_quantidade_combustivel(self, valor):
        self.quantidadeCombustivel = self.quantidadeCombustivel - valor

    def imprimir_qtd_combustivel(self):
        print(self.quantidadeCombustivel)


posto = BombadeCombustivel('Gasolina Comum', 3.50, 500)
posto.imprimir_qtd_combustivel()
posto.tipo_combustivel('Gasolina Aditivada')
posto.abastecer_por_litro(50)
posto.imprimir_qtd_combustivel()
