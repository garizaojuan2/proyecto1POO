
from airport import Airport

class Airline:
    def __init__(self, airline_id, name):
        """
        Constructor de la clase Airline.

        Parámetros:
        - airline_id (str): Identificación única de la aerolínea.
        - name (str): Nombre de la aerolínea.
        """
        self.ident = airline_id
        self.name = name
        self.flights = []

    def get_name(self):
        """
        Obtiene el nombre de la aerolínea.

        Retorna:
        - str: Nombre de la aerolínea.
        """
        return self.name

    def add_flight(self, flight):
        """
        Agrega un vuelo a la lista de vuelos de la aerolínea y lo asigna a un avión en el aeropuerto.

        Parámetros:
        - flight (Flight): Objeto Flight que representa el vuelo a agregar.
        """
        self.flights.append(flight)
        airport = Airport.get_instance()
        airport.assign_flight(flight)

        

        

