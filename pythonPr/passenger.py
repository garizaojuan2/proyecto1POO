from person import Person

class Passenger(Person):
    def __init__(self,  _ident = None,  _name = None,  _lastName = None,  _birthdate = None,  _gender = None,  _address = None,  _phoneNumber = None,  _email = None,  _nationality = None,  _baggageAmount = None,  _medicalInformation = None):
        super().__init__(_ident, _name, _lastName, _birthdate, _gender, _address, _phoneNumber, _email)
        self.nationality = _nationality
        self.baggageAmount = _baggageAmount
        self.medicalInformation = _medicalInformation

    # Métodos get de Passenger
    def getNationality(self):
        return self.nationality

    def getBaggageAmount(self):
        return self.baggageAmount

    def getMedicalInformation(self):
        return self.medicalInformation

    # Métodos set de Passenger
    def setNationality(self, _nationality):
        self.nationality = _nationality

    def setBaggageAmount(self, _baggageAmount):
        self.baggageAmount = _baggageAmount

    def setMedicalInformation(self, _medicalInformation):
        self.medicalInformation = _medicalInformation