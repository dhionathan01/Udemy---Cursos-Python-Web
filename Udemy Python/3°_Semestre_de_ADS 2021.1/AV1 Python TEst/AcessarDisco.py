import json


class EmployeeDA:
    _nome = "employeeDataAccess"

    def write(self, data):
        with open('employee.txt', "w") as file_open:
            file_open.write(json.dumps(data, default=vars))

    def read(self):
        with open('employee.txt', "r") as file_open:
            data = json.loads(file_open.read())
            return data
