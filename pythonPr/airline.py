
from airport import Airport
class Airline:
    def __init__(self, i, n):
        self.name = n
        self.ident = i
        self.flights = []

    def getName(self):
        return self.name
    def add_flight(self, flight):
        self.flights.append(flight)
        aeropuerto = Airport.get_instance()
        aeropuerto.assign_flight(flight)
        

    

        

