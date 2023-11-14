from person import Person

class Passenger(Person):
    def __init__(self, _ident=None, _name=None, _lastName=None, _birthdate=None, _gender=None, _address=None,
                 _phoneNumber=None, _email=None, _nationality=None, _baggageAmount=None, _medicalInformation=None):
        """
        Constructor de la clase Passenger.

        Parámetros:
        - _ident (str): Identificación del pasajero.
        - _name (str): Nombre del pasajero.
        - _lastName (str): Apellido del pasajero.
        - _birthdate (date): Fecha de nacimiento del pasajero.
        - _gender (str): Género del pasajero.
        - _address (str): Dirección del pasajero.
        - _phoneNumber (str): Número de teléfono del pasajero.
        - _email (str): Correo electrónico del pasajero.
        - _nationality (str): Nacionalidad del pasajero.
        - _baggageAmount (int): Cantidad de equipaje del pasajero.
        - _medicalInformation (str): Información médica del pasajero.
        """
        super().__init__(_ident, _name, _lastName, _birthdate, _gender, _address, _phoneNumber, _email)
        self.nationality = _nationality
        self.baggageAmount = _baggageAmount
        self.medicalInformation = _medicalInformation

    # Métodos get de Passenger
    def getNationality(self):
        """
        Obtiene la nacionalidad del pasajero.

        Retorna:
        - str: Nacionalidad del pasajero.
        """
        return self.nationality

    def getBaggageAmount(self):
        """
        Obtiene la cantidad de equipaje del pasajero.

        Retorna:
        - int: Cantidad de equipaje del pasajero.
        """
        return self.baggageAmount

    def getMedicalInformation(self):
        """
        Obtiene la información médica del pasajero.

        Retorna:
        - str: Información médica del pasajero.
        """
        return self.medicalInformation

    # Métodos set de Passenger
    def setNationality(self, _nationality):
        """
        Establece la nacionalidad del pasajero.

        Parámetros:
        - _nationality (str): Nueva nacionalidad del pasajero.
        """
        self.nationality = _nationality

    def setBaggageAmount(self, _baggageAmount):
        """
        Establece la cantidad de equipaje del pasajero.

        Parámetros:
        - _baggageAmount (int): Nueva cantidad de equipaje del pasajero.
        """
        self.baggageAmount = _baggageAmount

    def setMedicalInformation(self, _medicalInformation):
        """
        Establece la información médica del pasajero.

        Parámetros:
        - _medicalInformation (str): Nueva información médica del pasajero.
        """
        self.medicalInformation = _medicalInformation
