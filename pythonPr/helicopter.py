from aircraft import Aircraft

class Helicopter(Aircraft):
    def __init__(self, brand=None, model=None, ident=None, capacity=None, max_speed=None, autonomy=None, year=None,
                 condition=None, engine_amount=None, elevation_capacity=None, use=None):
        """
        Constructor de la clase Helicopter.

        Parámetros:
        - brand (str): Marca del helicóptero.
        - model (str): Modelo del helicóptero.
        - ident (str): Identificador único del helicóptero.
        - capacity (int): Capacidad de pasajeros del helicóptero.
        - max_speed (float): Velocidad máxima del helicóptero.
        - autonomy (float): Autonomía de vuelo del helicóptero.
        - year (int): Año de fabricación del helicóptero.
        - condition (str): Condición actual del helicóptero.
        - engine_amount (int): Cantidad de motores del helicóptero.
        - elevation_capacity (float): Capacidad de elevación del helicóptero.
        - use (str): Uso principal del helicóptero.
        """
        super().__init__(brand, model, ident, capacity, max_speed, autonomy, year, condition)
        self.engine_amount = engine_amount
        self.elevation_capacity = elevation_capacity
        self.use = use

    def get_engine_amount(self):
        """
        Obtiene la cantidad de motores del helicóptero.

        Retorna:
        - int: Cantidad de motores del helicóptero.
        """
        return self.engine_amount

    def get_elevation_capacity(self):
        """
        Obtiene la capacidad de elevación del helicóptero.

        Retorna:
        - float: Capacidad de elevación del helicóptero.
        """
        return self.elevation_capacity

    def get_use(self):
        """
        Obtiene el uso principal del helicóptero.

        Retorna:
        - str: Uso principal del helicóptero.
        """
        return self.use

    def set_engine_amount(self, new_engine_amount):
        """
        Establece una nueva cantidad de motores para el helicóptero.

        Parámetros:
        - new_engine_amount (int): Nueva cantidad de motores para el helicóptero.
        """
        self.engine_amount = new_engine_amount

    def set_elevation_capacity(self, new_elevation_capacity):
        """
        Establece una nueva capacidad de elevación para el helicóptero.

        Parámetros:
        - new_elevation_capacity (float): Nueva capacidad de elevación para el helicóptero.
        """
        self.elevation_capacity = new_elevation_capacity

    def set_use(self, new_use):
        """
        Establece un nuevo uso principal para el helicóptero.

        Parámetros:
        - new_use (str): Nuevo uso principal para el helicóptero.
        """
        self.use = new_use
