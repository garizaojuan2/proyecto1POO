from person import Person

class Worker(Person):
    def __init__(self, _ident=None, _name=None, _lastName=None, _birthdate=None, _gender=None, _address=None,
                 _phoneNumber=None, _email=None, _position=None, _yearsOfExperience=None, _maxDailyHours=None):
        """
        Constructor de la clase Worker.

        Parámetros:
        - _ident (str): Identificación del trabajador.
        - _name (str): Nombre del trabajador.
        - _lastName (str): Apellido del trabajador.
        - _birthdate (date): Fecha de nacimiento del trabajador.
        - _gender (str): Género del trabajador.
        - _address (str): Dirección del trabajador.
        - _phoneNumber (str): Número de teléfono del trabajador.
        - _email (str): Correo electrónico del trabajador.
        - _position (str): Posición del trabajador.
        - _yearsOfExperience (int): Años de experiencia del trabajador.
        - _maxDailyHours (int): Máximo de horas diarias permitidas para el trabajador.
        """
        super().__init__(_ident, _name, _lastName, _birthdate, _gender, _address, _phoneNumber, _email)
        self.position = _position
        self.yearsOfExperience = _yearsOfExperience
        self.maxDailyHours = _maxDailyHours

    # Métodos get de Worker
    def getPosition(self):
        """
        Obtiene la posición del trabajador.

        Retorna:
        - str: Posición del trabajador.
        """
        return self.position

    def getYearsOfExperience(self):
        """
        Obtiene los años de experiencia del trabajador.

        Retorna:
        - int: Años de experiencia del trabajador.
        """
        return self.yearsOfExperience

    def getMaxDailyHours(self):
        """
        Obtiene el máximo de horas diarias permitidas para el trabajador.

        Retorna:
        - int: Máximo de horas diarias permitidas para el trabajador.
        """
        return self.maxDailyHours

    # Métodos set de Worker
    def setPosition(self, _position):
        """
        Establece la posición del trabajador.

        Parámetros:
        - _position (str): Nueva posición del trabajador.
        """
        self.position = _position

    def setYearsOfExperience(self, _yearsOfExperience):
        """
        Establece los años de experiencia del trabajador.

        Parámetros:
        - _yearsOfExperience (int): Nuevos años de experiencia del trabajador.
        """
        self.yearsOfExperience = _yearsOfExperience

    def setMaxDailyHours(self, _maxDailyHours):
        """
        Establece el máximo de horas diarias permitidas para el trabajador.

        Parámetros:
        - _maxDailyHours (int): Nuevo máximo de horas diarias permitidas para el trabajador.
        """
        self.maxDailyHours = _maxDailyHours
