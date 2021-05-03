class newEmployee:
    _id = ''
    _name = ''
    _registration = ''
    _office = ''
    _department = ''
    _wage = ''

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
