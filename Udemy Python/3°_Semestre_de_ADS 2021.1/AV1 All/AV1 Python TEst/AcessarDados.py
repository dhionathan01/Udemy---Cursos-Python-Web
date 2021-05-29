from AcessarDisco import EmployeeDA
from Funcionario import newEmployee
import json


class DataAccess:

    def write(self, employeeData):
        with open('employee.txt', "w") as file_open:
            file_open.write(json.dumps(employeeData.to_list(), default=vars))

    def read(self, employeeData, managerData, departmentData):
        with open('employee.txt', "r") as file_open:
            data = json.loads(file_open.read())
            employeeData.set_list(data)
        with open('manager.txt', "r") as file_open:
            data = json.loads(file_open.read())
            managerData.set_list(data)
        with open('department.txt', "r") as file_open:
            data = json.loads(file_open.read())
            departmentData.set_list(data)


class EmployeeDAO:
    list = {}
    employeeDA = EmployeeDA()

    def to_save(self, new_employee):
        self.list[new_employee.get_id()] = new_employee
        self.employeeDA.write(self.list)

    def update(self, new_employee):
        self.list[new_employee.get_id()] = new_employee
        self.employeeDA.write(self.list)

    def delete(self, new_employee):
        del self.list[new_employee.get_id()]
        self.employeeDA.write(self.list)

    def retrieve_by_id(self, key):
        self.list = self.employeeDA.read()
        e = self.list[key]
        return newEmployee(**e)

    def to_list(self):
        self.list = self.employeeDA.read()
        return self.list
