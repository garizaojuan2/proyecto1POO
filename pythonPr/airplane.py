from aircraft import Aircraft

class Airplane(Aircraft):
    def __init__(self, brand=None, model=None, ident=None, capacity=None, max_speed=None, autonomy=None, year=None, condition=None, max_altitude=None, engine_amount=None, category=None):
        """
        Constructor de la clase Airplane.

        Parámetros:
        - brand (str): Marca de la aeronave.
        - model (str): Modelo de la aeronave.
        - ident (str): Identificador único de la aeronave.
        - capacity (int): Capacidad máxima de pasajeros de la aeronave.
        - max_speed (float): Velocidad máxima de la aeronave.
        - autonomy (float): Autonomía de vuelo de la aeronave.
        - year (int): Año de fabricación de la aeronave.
        - condition (str): Condición actual de la aeronave (e.g., "Operativa", "En mantenimiento").
        - max_altitude (float): Altitud máxima que puede alcanzar la aeronave.
        - engine_amount (int): Cantidad de motores de la aeronave.
        - category (str): Categoría de la aeronave.
        """
        super().__init__(brand, model, ident, capacity, max_speed, autonomy, year, condition)
        self.max_altitude = max_altitude
        self.engine_amount = engine_amount
        self.category = category

    # Métodos de acceso (Getters)
    def get_max_altitude(self):
        """
        Obtiene la altitud máxima que puede alcanzar la aeronave.

        Returns:
        float: Altitud máxima.
        """
        return self.max_altitude

    def get_engine_amount(self):
        """
        Obtiene la cantidad de motores de la aeronave.

        Returns:
        int: Cantidad de motores.
        """
        return self.engine_amount

    def get_category(self):
        """
        Obtiene la categoría de la aeronave.

        Returns:
        str: Categoría de la aeronave.
        """
        return self.category

    # Métodos de modificación (Setters)
    def set_max_altitude(self, new_max_altitude):
        """
        Establece la altitud máxima que puede alcanzar la aeronave.

        Parámetros:
        new_max_altitude (float): Nueva altitud máxima.
        """
        self.max_altitude = new_max_altitude

    def set_engine_amount(self, new_engine_amount):
        """
        Establece la cantidad de motores de la aeronave.

        Parámetros:
        new_engine_amount (int): Nueva cantidad de motores.
        """
        self.engine_amount = new_engine_amount

    def set_category(self, new_category):
        """
        Establece la categoría de la aeronave.

        Parámetros:
        new_category (str): Nueva categoría.
        """
        self.category = new_category
