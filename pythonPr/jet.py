from aircraft import Aircraft

class PrivateJet(Aircraft):
    def __init__(self, brand=None, model=None, ident=None, capacity=None, max_speed=None, autonomy=None, year=None,
                 condition=None, owner=None, _services=None, _destinations=None):
        """
        Constructor de la clase PrivateJet.

        Parámetros:
        - brand (str): Marca del jet privado.
        - model (str): Modelo del jet privado.
        - ident (str): Identificador único del jet privado.
        - capacity (int): Capacidad de pasajeros del jet privado.
        - max_speed (float): Velocidad máxima del jet privado.
        - autonomy (float): Autonomía de vuelo del jet privado.
        - year (int): Año de fabricación del jet privado.
        - condition (str): Condición actual del jet privado.
        - owner (str): Propietario del jet privado.
        - _services (list): Lista de servicios ofrecidos por el jet privado.
        - _destinations (list): Lista de destinos a los que puede llegar el jet privado.
        """
        super().__init__(brand, model, ident, capacity, max_speed, autonomy, year, condition)
        self.owner = owner
        self.services = _services
        self.destinations = _destinations

    def set_owner(self, owner):
        """
        Establece el propietario del jet privado.

        Parámetros:
        - owner (str): Nuevo propietario del jet privado.
        """
        self.owner = owner

    def add_service(self, service):
        """
        Añade un nuevo servicio ofrecido por el jet privado.

        Parámetros:
        - service (str): Nuevo servicio a añadir.
        """
        self.services.append(service)

    def add_destination(self, destination):
        """
        Añade un nuevo destino al que puede llegar el jet privado.

        Parámetros:
        - destination (str): Nuevo destino a añadir.
        """
        self.destinations.append(destination)

    def get_owner(self):
        """
        Obtiene el propietario del jet privado.

        Retorna:
        - str: Propietario del jet privado.
        """
        return self.owner

    def get_services(self):
        """
        Obtiene la lista de servicios ofrecidos por el jet privado.

        Retorna:
        - list: Lista de servicios ofrecidos.
        """
        return self.services

    def get_destinations(self):
        """
        Obtiene la lista de destinos a los que puede llegar el jet privado.

        Retorna:
        - list: Lista de destinos alcanzables.
        """
        return self.destinations
