from AcessoAoDisco import AcessoAoDisco
from Models.Funcionario import *

class FuncionarioDAO:

    def __init__(self):
        self.__acessoAoDisco = AcessoAoDisco("funcionario.txt")
    
    def salvar(self, funcionario):
        self.__acessoAoDisco.gravar(f"{funcionario.getID()}:{funcionario.getNome()}:{funcionario.getMatricula()}:{funcionario.getCargo()}:{funcionario.getDepartamento()}:{funcionario.getSalario()}")
    
    def atualizar(self, funcionario):
        lista = self.__acessoAoDisco.abrir()
        listaAtualizada = []
        
        for value in lista:                
            valores = value.split(":")
            
            if int(valores[0]) == funcionario.getID():
                listaAtualizada.append(f"{funcionario.getID()}:{funcionario.getNome()}:{funcionario.getMatricula()}:{funcionario.getCargo()}:{funcionario.getDepartamento()}:{funcionario.getSalario()}")
            else:
                listaAtualizada.append(value.rstrip())
        
        self.__acessoAoDisco.gravar(listaAtualizada, True)
    
    def deletar(self, funcionario):
        lista = self.__acessoAoDisco.abrir()
        listaAtualizada = []
        
        for value in lista:        
            valores = value.split(":")
            if int(valores[0]) != funcionario.getID():
                listaAtualizada.append(value.rstrip()) 
        
        self.__acessoAoDisco.gravar(listaAtualizada, True)
        
    def recuperarPoID(self, indice):
        lista = self.__acessoAoDisco.abrir()
        
        for value in lista:
            valores = value.split(":")
            if int(valores[0]) == int(indice):
                return Funcionario(valores[0], valores[1], valores[2], valores[3], valores[4], valores[5])
        
        return None
    
    def listar(self):
        lista = self.__acessoAoDisco.abrir()
        funcionarios = []
        for value in lista:
            valores = value.split(":")
            funcionarios.append(Funcionario(valores[0], valores[1], valores[2], valores[3], valores[4], valores[5]))
        
        return funcionarios