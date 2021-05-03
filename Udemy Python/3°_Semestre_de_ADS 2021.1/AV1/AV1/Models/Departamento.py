class Departamento:
    def __init__(self, ID, nome, gerente): 
        self.__ID = ID 
        self.__nome = nome 
        self.__gerente = gerente
        self.__troco = 0
        self.__caixa = False
        self.__vendas = []
    
    def getID(self):
        return self.__ID
        
    def getNome(self):
        return self.__nome
    
    def getGerente(self):
        return self.__gerente
    
    def getTroco(self):
        return self.__troco
        
    def getCaixa(self):
        return self.__caixa
    
    def getVendas(self):
        return self.__vendas
    
    def registrarVenda(self, venda):
        if self.__caixa:
            self.__vendas.append(venda)
    
    def __calcularMontanteVenda(self):
        montante = 0
        for venda in self.__vendas:
            montante += venda
        
        return montante
    
    def iniciarCaixa(self, troco):
        self.__troco = troco
        self.__caixa = True
        self.__vendas = []
    
    def fecharCaixa(self):
        return {'troco': self.__troco, 'montante': self.__calcularMontanteVenda()}
        