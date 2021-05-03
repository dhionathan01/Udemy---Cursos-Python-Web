from Funcionario import newEmployee
from AcessarDados import EmployeeDAO
from AcessarDados import DataAccess

employee = newEmployee()
employee.set_id('01')
employee.set_name('Marcelo')
employee.set_registration('00001')
employee.set_department('Desenvolvimento')
employee.set_office('Arquiteto')
employee.set_wage('15500')

employeeDAO = EmployeeDAO()
employeeDAO.to_save(employee)

employee2 = newEmployee()
employee2.set_id('02')
employee2.set_name('Sara')
employee2.set_registration('00002')
employee2.set_department('Desenvolvimento')
employee2.set_office('Back-end')
employee2.set_wage('9575')

employeeDAO.to_save(employee2)
print(employeeDAO.to_list())

dataAccess = DataAccess()
dataAccess.write(employeeDAO)
