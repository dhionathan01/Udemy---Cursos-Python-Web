import json


class newEmployee:
    _id = None
    _name = None
    _registration = None
    _office = None
    _department = None
    _wage = None

    def __init__(self, _id, _name, _registration, _office, _department, _wage):
        self._id = _id
        self._name = _name
        self._registration = _registration
        self._office = _office
        self._department = _department
        self._wage = _wage

    def set_id(self, identificador_unico):
        self._id = identificador_unico

    def get_id(self):
        return self._id

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_registration(self, registration):
        self._registration = registration

    def get_registration(self):
        return self._registration

    def set_office(self, office):
        self._office = office

    def get_office(self):
        return self._office

    def set_department(self, department):
        self._department = department

    def get_department(self):
        return self._department

    def set_wage(self, wage):
        self._wage = wage

    def get_wage(self):
        return self._wage

    def calculate_wage_liquid(self):
        wage_liquid = (self._wage * 0.84) * 1.3
        return wage_liquid

    def __str__(self):
        return "{id= " + self.get_id() + \
               ", name= " + self.get_name() + \
               ", registratio= " + self.get_registration() + \
               ", office=" + self.get_office() + \
               ", department= " + self.get_department() + \
               ", wage= " + str(self.get_wage())


class Manager(newEmployee):
    _office = None
    _wage = None

    def set_office(self, office):
        self._office = office

    def get_office(self):
        return self._office

    def set_wage(self, wage):
        self._wage = wage

    def get_wage(self):
        return self._wage

    def calculate_wage_liquid(self):
        wage_liquid = (self._wage * 0.84) * (self._wage * 0.5)
        return wage_liquid


class Department:
    __id = None
    __name = None
    _manager = None
    _sales = []
    _status = False
    _initial_value = 0
    __sales_value = 0

    def set_id(self, identificador_unico):
        self.__id = identificador_unico

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_manager(self, manager):
        self._manager = manager

    def get_manager(self):
        return self._manager

    def set_sales(self, sales):
        self._sales = sales

    def get_sales(self):
        return self._sales

    def set_status(self, status):
        self._status = status

    def get_status(self):
        return self.status

    def open(self, initial_value):
        self.status = True
        self.initial_value = initial_value

    def close(self):
        final_amounts = []
        final_amounts.append(self.initial_value)
        final_amounts.append(self.sales_value)
        self.status = False
        self.initial_value = 0
        self.sales_value = 0

    def add_sale(self, sale):
        if (self.status == True):
            self.sales.append(sale)
            self.sales_value = sum(sale.get_value())
            return sale.get_value()

        else:
             print("O caixa está fechado!")


class sales:
    _id = None
    _produto = None
    _value = 0.0

    def set_produto(self, produto):
        self._produto = produto

    def get_produto(self):
        return self.produto

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self.value

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self.id

class produto:
    _id = None
    _name = None

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self.name


# class DataAccess:
#
#     def write(self, employeeData, managerData, departmentData):
#         with open('employee.txt', "w") as file_open:
#             file_open.write(json.dumps(employeeData.to_list(), default=vars))
#         with open('manager.txt', "w") as file_open:
#             file_open.write(json.dumps(managerData.to_list(), default=vars))
#         with open('department.txt', "w") as file_open:
#             file_open.write(json.dumps(departmentData.to_list(), default=vars))
#
#     def read(self, employeeData, managerData, departmentData):
#         with open('employee.txt', "r") as file_open:
#             data = json.loads(file_open.read())
#             employeeData.set_list(data)
#         with open('manager.txt', "r") as file_open:
#             data = json.loads(file_open.read())
#             managerData.set_list(data)
#         with open('department.txt', "r") as file_open:
#             data = json.loads(file_open.read())
#             departmentData.set_list(data)


class EmployeeDA:
    _nome = "employeeDataAccess"

    def write(self, data):
        with open('employee.txt', "w") as file_open:
            file_open.write(json.dumps(data, default=vars))

    def read(self):
        with open('employee.txt', "r") as file_open:
            data = json.loads(file_open.read())
            return data


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


class ManagerDAO:
    list = {}

    def to_save(self, new_employee):
        self.list[new_employee.get_id()] = new_employee

    def update(self, new_employee):
        self.list[new_employee.get_id()] = new_employee

    def delete(self, new_employee):
        del self.list[new_employee.get_id()]

    def retrieve_by_id(self, key):
        return self.list[key]

    def to_list(self):
        return self.list

    def set_list(self, data):
        self.list = data


class DepartmentDAO:
    list = {}

    def to_save(self, department):
        self.list[department.get_id()] = department

    def update(self, department):
        self.list[department.get_id()] = department

    def delete(self, department):
        del self.list[department.get_id()]

    def retrieve_by_id(self, key):
        return self.list[key]

    def to_list(self):
        return self.list

    def set_list(self, data):
        self.list = data


# employee = newEmployee()
# employee.set_id('01')
# employee.set_name('Marcelo')
# employee.set_registration('00001')
# employee.set_department('Desenvolvimento')
# employee.set_office('Arquiteto')
# employee.set_wage(15500)
#
# employeeDAO = EmployeeDAO()
# employeeDAO.to_save(employee)
#
# employee2 = newEmployee()
# employee2.set_id('02')
# employee2.set_name('Sara')
# employee2.set_registration('00002')
# employee2.set_department('Desenvolvimento')
# employee2.set_office('Back-end')
# employee2.set_wage(9575)
#
# employeeDAO.to_save(employee2)
# print(employeeDAO.to_list())
#
# dataAccess = DataAccess()
# dataAccess.write(employeeDAO)

employeeDAO = EmployeeDAO()
managerDAO = ManagerDAO()
departmentDAO = DepartmentDAO()

# employee2 = newEmployee()
#
# employee2.set_id('04')
# employee2.set_name('Sara')
# employee2.set_registration('00002')
# employee2.set_department('Desenvolvimento')
# employee2.set_office('Back-end')
# employee2.set_wage(9578)
#
# employeeDAO.to_save(employee2)
print(employeeDAO.to_list())
e = employeeDAO.retrieve_by_id('01')
e.set_department('sdkbf')
employeeDAO.update(e)
print(employeeDAO.to_list())
print(type(employeeDAO.to_list()))

#dataAccess.write(employeeDAO)

#exemplo completo, todos os objetos
