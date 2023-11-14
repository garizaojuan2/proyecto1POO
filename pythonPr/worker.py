from person import Person

class Worker(Person):
    def __init__(self,  _ident = None,  _name = None,  _lastName = None,  _birthdate = None,  _gender = None,  _address = None,  _phoneNumber = None,  _email = None,  _position = None,  _yearsOfExperience = None,  _maxDailyHours = None):
        super().__init__(_ident, _name, _lastName, _birthdate, _gender, _address, _phoneNumber, _email)
        self.position = _position
        self.yearsOfExperience = _yearsOfExperience
        self.maxDailyHours = _maxDailyHours

    # Métodos get de Worker
    def getPosition(self):
        return self.position

    def getYearsOfExperience(self):
        return self.yearsOfExperience

    def getMaxDailyHours(self):
        return self.maxDailyHours

    # Métodos set de Worker
    def setPosition(self, _position):
        self.position = _position

    def setYearsOfExperience(self, _yearsOfExperience):
        self.yearsOfExperience = _yearsOfExperience

    def setMaxDailyHours(self, _maxDailyHours):
        self.maxDailyHours = _maxDailyHours
