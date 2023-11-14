
class Person:
    def __init__(self, _ident = None, _name = None, _lastName = None, _birthdate = None, _gender = None, _address = None, _phoneNumber = None, _email = None):
        self.ident = _ident
        self.name = _name
        self.lastName = _lastName
        self.birthdate = _birthdate
        self.gender = _gender
        self.address = _address
        self.phoneNumber = _phoneNumber
        self.email = _email

    # Métodos get para obtener los valores de los atributos
    def get_ident(self):
        return self.ident

    def getName(self):
        return self.name

    def getLastName(self):
        return self.lastName

    def getBirthdate(self):
        return self.birthdate

    def getGender(self):
        return self.gender

    def getAddress(self):
        return self.address

    def getPhoneNumber(self):
        return self.phoneNumber

    def getEmail(self):
        return self.email

    # Métodos set para modificar los valores de los atributos
    def setId(self, _ident):
        self.ident = _ident

    def setName(self, _name):
        self.name = _name

    def setLastName(self, _lastName):
        self.lastName = _lastName

    def setBirthdate(self, _birthdate):
        self.birthdate = _birthdate

    def setGender(self, _gender):
        self.gender = _gender

    def setAddress(self, _address):
        self.address = _address

    def setPhoneNumber(self, _phoneNumber):
        self.phoneNumber = _phoneNumber

    def setEmail(self, _email):
        self.email = _email