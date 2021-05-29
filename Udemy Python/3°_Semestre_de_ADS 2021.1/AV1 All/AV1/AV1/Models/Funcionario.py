class Funcionario:
    def __init__(self, ID, nome, matricula, cargo, departamento, salario): 
        self.__ID = int(ID)
        self.__nome = nome
        self.__matricula = matricula
        self.__cargo = cargo
        self.__departamento = departamento
        self._salario = float(salario)
    
    def setSalario(self, salario):
        self._salario = float(salario)
    
    def setCargo(self, cargo):
        self.__cargo = cargo
        
    def getID(self):
        return self.__ID
        
    def getNome(self):
        return self.__nome
        
    def getMatricula(self):
        return self.__matricula
    
    def getCargo(self):
        return self.__cargo
    
    def getDepartamento(self):
        return self.__departamento
    
    def getSalario(self):
        return self._salario
        
    def calcularSalarioLiquido(self):
        return (self._salario * 0.84) * 1.3