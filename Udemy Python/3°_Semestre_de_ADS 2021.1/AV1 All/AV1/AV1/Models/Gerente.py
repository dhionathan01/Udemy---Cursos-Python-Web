from Models.Funcionario import *

class Gerente(Funcionario):
    def __init__(self, ID, nome, matricula, cargo, departamento, salario): 
        super().__init__(ID, nome, matricula, cargo, departamento, salario)
    
    def calcularSalarioLiquido(self):
        return (self._salario * 0.84) + (self._salario * 0.5)