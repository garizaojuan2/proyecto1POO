class Gate:
    def __init__(self, ident=None, location=None, availability=None, boarding_hour=None):
        """
        Constructor de la clase Gate.

        Parámetros:
        - ident (str): Identificador único de la puerta de embarque.
        - location (str): Ubicación de la puerta de embarque.
        - availability (bool): Disponibilidad de la puerta de embarque.
        - boarding_hour (str): Hora de embarque de la puerta de embarque.
        """
        self.ident = ident
        self.location = location
        self.availability = availability
        self.boarding_hour = boarding_hour
        self.flight_assigned = None
        self.flights_record = []

    def set_flight_assigned(self, flight_assigned):
        """
        Establece el vuelo asignado a la puerta de embarque.

        Parámetros:
        - flight_assigned (Flight): Objeto Flight que representa el vuelo asignado a la puerta de embarque.
        """
        self.flight_assigned = flight_assigned

    def set_ident(self, ident):
        """
        Establece el identificador de la puerta de embarque.

        Parámetros:
        - ident (str): Nuevo identificador de la puerta de embarque.
        """
        self.ident = ident

    def set_location(self, location):
        """
        Establece la ubicación de la puerta de embarque.

        Parámetros:
        - location (str): Nueva ubicación de la puerta de embarque.
        """
        self.location = location

    def set_availability(self, availability):
        """
        Establece la disponibilidad de la puerta de embarque.

        Parámetros:
        - availability (bool): Nuevo estado de disponibilidad de la puerta de embarque.
        """
        self.availability = availability

    def set_boarding_hour(self, boarding_hour):
        """
        Establece la hora de embarque de la puerta de embarque.

        Parámetros:
        - boarding_hour (str): Nueva hora de embarque de la puerta de embarque.
        """
        self.boarding_hour = boarding_hour

    def get_flight_assigned(self):
        """
        Obtiene el vuelo asignado a la puerta de embarque.

        Retorna:
        - Flight: Objeto Flight que representa el vuelo asignado a la puerta de embarque.
        """
        return self.flight_assigned

    def get_ident(self):
        """
        Obtiene el identificador de la puerta de embarque.

        Retorna:
        - str: Identificador de la puerta de embarque.
        """
        return self.ident

    def get_location(self):
        """
        Obtiene la ubicación de la puerta de embarque.

        Retorna:
        - str: Ubicación de la puerta de embarque.
        """
        return self.location

    def is_available(self):
        """
        Verifica si la puerta de embarque está disponible.

        Retorna:
        - bool: True si la puerta de embarque está disponible, False de lo contrario.
        """
        return self.availability

    def get_boarding_hour(self):
        """
        Obtiene la hora de embarque de la puerta de embarque.

        Retorna:
        - str: Hora de embarque de la puerta de embarque.
        """
        return self.boarding_hour

    def get_flights_record(self):
        """
        Obtiene el registro de vuelos asociados a la puerta de embarque.

        Retorna:
        - list: Lista de objetos Flight que representan los vuelos asociados a la puerta de embarque.
        """
        return self.flights_record

    def add_flights_record(self, flight):
        """
        Agrega un vuelo al registro de vuelos asociados a la puerta de embarque.

        Parámetros:
        - flight (Flight): Objeto Flight que representa el vuelo a agregar al registro.
        """
        self.flights_record.append(flight)
