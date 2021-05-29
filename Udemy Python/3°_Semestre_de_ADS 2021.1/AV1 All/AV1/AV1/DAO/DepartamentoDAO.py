from AcessoAoDisco import AcessoAoDisco
from Models.Departamento import *
from DAO.GerenteDAO import *

class DepartamentoDAO:

    def __init__(self):
        self.__acessoAoDisco = AcessoAoDisco("departamento.txt")
        self.__gerenteDAO = GerenteDAO()
    
    def salvar(self, departamento):
        vendas = '#'.join([str(elem) for elem in departamento.getVendas()])
        self.__acessoAoDisco.gravar(f"{departamento.getID()}:{departamento.getNome()}:{departamento.getGerente().getID()}:{departamento.getCaixa()}:{departamento.getTroco()}:{vendas}")
    
    def atualizar(self, departamento):
        lista = self.__acessoAoDisco.abrir()
        listaAtualizada = []
        
        for value in lista:                
            valores = value.split(":")
            
            if int(valores[0]) == departamento.getID():
                vendas = '#'.join([str(elem) for elem in departamento.getVendas()])
                listaAtualizada.append(f"{departamento.getID()}:{departamento.getNome()}:{departamento.getGerente().getID()}:{departamento.getCaixa()}:{departamento.getTroco()}:{vendas}")
            else:
                listaAtualizada.append(value.rstrip())
        
        self.__acessoAoDisco.gravar(listaAtualizada, True)
    
    def deletar(self, departamento):
        lista = self.__acessoAoDisco.abrir()
        listaAtualizada = []
        
        for value in lista:        
            valores = value.split(":")
            if int(valores[0]) != departamento.getID():
                listaAtualizada.append(value.rstrip()) 
        
        self.__acessoAoDisco.gravar(listaAtualizada, True)
        
    def recuperarPoID(self, indice):
        lista = self.__acessoAoDisco.abrir()
        
        for value in lista:
            valores = value.split(":")
            if int(valores[0]) == int(indice):
                departamento = Departamento(valores[0], valores[1], self.__gerenteDAO.recuperarPoID(valores[2]))
                
                if bool(valores[3]):
                    departamento.iniciarCaixa(float(valores[4]))
                
                vendas = valores[5].split("#")
                
                for venda in vendas:
                    departamento.registrarVenda(float(venda))
                
                return departamento
        
        return None
    
    def listar(self):
        lista = self.__acessoAoDisco.abrir()
        departamentos = []
        for value in lista:
            valores = value.split(":")
            departamento = Departamento(valores[0], valores[1], self.__gerenteDAO.recuperarPoID(valores[2]))
                
            if bool(valores[3]):
                departamento.iniciarCaixa(float(valores[4]))
            
            vendas = valores[5].split("#")
            
            for venda in vendas:
                departamento.registrarVenda(float(venda))
                
            departamentos.append(departamento)
        
        return departamentos