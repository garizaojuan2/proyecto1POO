from control_tower import ControlTower

class Flight:
    def __init__(self, _ident=None, _date=None, _origin=None, _destination=None, _seats=None, _airline=None):
        """
        Constructor de la clase Flight.

        Parámetros:
        - _ident (str): Identificador único del vuelo.
        - _date (str): Fecha del vuelo.
        - _origin (str): Ciudad de origen del vuelo.
        - _destination (str): Ciudad de destino del vuelo.
        - _seats (int): Número de asientos disponibles en el vuelo.
        - _airline (Airline): Objeto Airline que representa la aerolínea asociada al vuelo.
        """
        self.ident = _ident
        self.date = _date
        self.origin = _origin
        self.destination = _destination
        self.assigned_crew = []
        self.boarding_gate = None
        self.passengers_registered = {}
        self.airplane = None
        self.available_seats = _seats
        self.airline = _airline

    def embark(self):
        """
        Método para embarcar el vuelo asignándole una puerta de embarque.

        Utiliza la instancia única de ControlTower para asignar una puerta de embarque al vuelo.
        """
        ControlTower.get_instance().assign_boarding_gate(self)

    def set_airplane(self, airplane):
        """
        Establece la aeronave asociada al vuelo y actualiza el número de asientos disponibles.

        Parámetros:
        - airplane (Airplane): Objeto Airplane que representa la aeronave asociada al vuelo.
        """
        self.airplane = airplane
        self.available_seats = airplane.get_capacity()

    def set_ident(self, ident):
        """
        Establece el identificador del vuelo.

        Parámetros:
        - ident (str): Nuevo identificador del vuelo.
        """
        self.ident = ident

    def set_date(self, date):
        """
        Establece la fecha del vuelo.

        Parámetros:
        - date (str): Nueva fecha del vuelo.
        """
        self.date = date

    def set_origin(self, origin):
        """
        Establece la ciudad de origen del vuelo.

        Parámetros:
        - origin (str): Nueva ciudad de origen del vuelo.
        """
        self.origin = origin

    def set_destination(self, destination):
        """
        Establece la ciudad de destino del vuelo.

        Parámetros:
        - destination (str): Nueva ciudad de destino del vuelo.
        """
        self.destination = destination

    def set_assigned_crew(self, assigned_crew):
        """
        Establece la tripulación asignada al vuelo.

        Parámetros:
        - assigned_crew (list): Lista de objetos Worker que representan la tripulación asignada al vuelo.
        """
        self.assigned_crew = assigned_crew

    def set_available_seats(self, num):
        """
        Establece el número de asientos disponibles en el vuelo.

        Parámetros:
        - num (int): Nuevo número de asientos disponibles en el vuelo.
        """
        self.available_seats = num

    def get_ident(self):
        """
        Obtiene el identificador del vuelo.

        Retorna:
        - str: Identificador del vuelo.
        """
        return self.ident

    def get_date(self):
        """
        Obtiene la fecha del vuelo.

        Retorna:
        - str: Fecha del vuelo.
        """
        return self.date

    def get_origin(self):
        """
        Obtiene la ciudad de origen del vuelo.

        Retorna:
        - str: Ciudad de origen del vuelo.
        """
        return self.origin

    def get_destination(self):
        """
        Obtiene la ciudad de destino del vuelo.

        Retorna:
        - str: Ciudad de destino del vuelo.
        """
        return self.destination

    def get_assigned_crew(self):
        """
        Obtiene la tripulación asignada al vuelo.

        Retorna:
        - list: Lista de objetos Worker que representan la tripulación asignada al vuelo.
        """
        return self.assigned_crew

    def get_boarding_gate(self):
        """
        Obtiene la puerta de embarque asignada al vuelo.

        Retorna:
        - Gate: Objeto Gate que representa la puerta de embarque asignada al vuelo.
        """
        return self.boarding_gate

    def get_passengers_registered(self):
        """
        Obtiene el diccionario de pasajeros registrados en el vuelo.

        Retorna:
        - dict: Diccionario donde las claves son los identificadores de los pasajeros y los valores son objetos Passenger.
        """
        return self.passengers_registered

    def get_airplane(self):
        """
        Obtiene la aeronave asociada al vuelo.

        Retorna:
        - Airplane: Objeto Airplane que representa la aeronave asociada al vuelo.
        """
        return self.airplane

    def get_available_seats(self):
        """
        Obtiene el número de asientos disponibles en el vuelo.

        Retorna:
        - int: Número de asientos disponibles en el vuelo.
        """
        return self.available_seats

    def set_boarding_gate(self, boarding_gate):
        """
        Establece la puerta de embarque asignada al vuelo.

        Parámetros:
        - boarding_gate (Gate): Objeto Gate que representa la puerta de embarque asignada al vuelo.
        """
        self.boarding_gate = boarding_gate

    def set_passengers_registered(self, passenger):
        """
        Agrega un pasajero al diccionario de pasajeros registrados en el vuelo.

        Parámetros:
        - passenger (Passenger): Objeto Passenger que representa al pasajero a agregar.
        """
        passenger_id = passenger.get_id()
        self.passengers_registered[passenger_id] = passenger
