from AcessoAoDisco import AcessoAoDisco
from Models.Gerente import *

class GerenteDAO:

    def __init__(self):
        self.__acessoAoDisco = AcessoAoDisco("gerente.txt")
    
    def salvar(self, gerente):
        self.__acessoAoDisco.gravar(f"{gerente.getID()}:{gerente.getNome()}:{gerente.getMatricula()}:{gerente.getCargo()}:{gerente.getDepartamento()}:{gerente.getSalario()}")
    
    def atualizar(self, gerente):
        lista = self.__acessoAoDisco.abrir()
        listaAtualizada = []
        
        for value in lista:                
            valores = value.split(":")
            
            if int(valores[0]) == gerente.getID():
                listaAtualizada.append(f"{gerente.getID()}:{gerente.getNome()}:{gerente.getMatricula()}:{gerente.getCargo()}:{gerente.getDepartamento()}:{gerente.getSalario()}")
            else:
                listaAtualizada.append(value.rstrip())
        
        self.__acessoAoDisco.gravar(listaAtualizada, True)
    
    def deletar(self, gerente):
        lista = self.__acessoAoDisco.abrir()
        listaAtualizada = []
        
        for value in lista:        
            valores = value.split(":")
            if int(valores[0]) != gerente.getID():
                listaAtualizada.append(value.rstrip()) 
        
        self.__acessoAoDisco.gravar(listaAtualizada, True)
        
    def recuperarPoID(self, indice):
        lista = self.__acessoAoDisco.abrir()
        
        for value in lista:
            valores = value.split(":")
            if int(valores[0]) == int(indice):
                return Gerente(valores[0], valores[1], valores[2], valores[3], valores[4], valores[5])
        
        return None
    
    def listar(self):
        lista = self.__acessoAoDisco.abrir()
        gerentes = []
        for value in lista:
            valores = value.split(":")
            gerentes.append(Gerente(valores[0], valores[1], valores[2], valores[3], valores[4], valores[5]))
        
        return gerentes