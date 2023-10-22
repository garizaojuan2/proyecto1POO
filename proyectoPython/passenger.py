from person import Person

class Passenger(Person):
    def __init__(self, _ident, _name, _lastName, _birthdate, _gender, _address, _phoneNumber, _email, _nationality, _baggageAmount, _medicalInformation):
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