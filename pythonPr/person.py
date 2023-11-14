class Person:
    def __init__(self, _ident=None, _name=None, _lastName=None, _birthdate=None, _gender=None, _address=None,
                 _phoneNumber=None, _email=None):
        """
        Constructor de la clase Person.

        Parámetros:
        - _ident (str): Identificación de la persona.
        - _name (str): Nombre de la persona.
        - _lastName (str): Apellido de la persona.
        - _birthdate (date): Fecha de nacimiento de la persona.
        - _gender (str): Género de la persona.
        - _address (str): Dirección de la persona.
        - _phoneNumber (str): Número de teléfono de la persona.
        - _email (str): Correo electrónico de la persona.
        """
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
        """
        Obtiene la identificación de la persona.

        Retorna:
        - str: Identificación de la persona.
        """
        return self.ident

    def getName(self):
        """
        Obtiene el nombre de la persona.

        Retorna:
        - str: Nombre de la persona.
        """
        return self.name

    def getLastName(self):
        """
        Obtiene el apellido de la persona.

        Retorna:
        - str: Apellido de la persona.
        """
        return self.lastName

    def getBirthdate(self):
        """
        Obtiene la fecha de nacimiento de la persona.

        Retorna:
        - date: Fecha de nacimiento de la persona.
        """
        return self.birthdate

    def getGender(self):
        """
        Obtiene el género de la persona.

        Retorna:
        - str: Género de la persona.
        """
        return self.gender

    def getAddress(self):
        """
        Obtiene la dirección de la persona.

        Retorna:
        - str: Dirección de la persona.
        """
        return self.address

    def getPhoneNumber(self):
        """
        Obtiene el número de teléfono de la persona.

        Retorna:
        - str: Número de teléfono de la persona.
        """
        return self.phoneNumber

    def getEmail(self):
        """
        Obtiene el correo electrónico de la persona.

        Retorna:
        - str: Correo electrónico de la persona.
        """
        return self.email

    # Métodos set para modificar los valores de los atributos
    def setId(self, _ident):
        """
        Establece la identificación de la persona.

        Parámetros:
        - _ident (str): Nueva identificación de la persona.
        """
        self.ident = _ident

    def setName(self, _name):
        """
        Establece el nombre de la persona.

        Parámetros:
        - _name (str): Nuevo nombre de la persona.
        """
        self.name = _name

    def setLastName(self, _lastName):
        """
        Establece el apellido de la persona.

        Parámetros:
        - _lastName (str): Nuevo apellido de la persona.
        """
        self.lastName = _lastName

    def setBirthdate(self, _birthdate):
        """
        Establece la fecha de nacimiento de la persona.

        Parámetros:
        - _birthdate (date): Nueva fecha de nacimiento de la persona.
        """
        self.birthdate = _birthdate

    def setGender(self, _gender):
        """
        Establece el género de la persona.

        Parámetros:
        - _gender (str): Nuevo género de la persona.
        """
        self.gender = _gender

    def setAddress(self, _address):
        """
        Establece la dirección de la persona.

        Parámetros:
        - _address (str): Nueva dirección de la persona.
        """
        self.address = _address

    def setPhoneNumber(self, _phoneNumber):
        """
        Establece el número de teléfono de la persona.

        Parámetros:
        - _phoneNumber (str): Nuevo número de teléfono de la persona.
        """
        self.phoneNumber = _phoneNumber

    def setEmail(self, _email):
        """
        Establece el correo electrónico de la persona.

        Parámetros:
        - _email (str): Nuevo correo electrónico de la persona.
        """
        self.email = _email
