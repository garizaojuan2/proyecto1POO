#from aircraft import Aircraft

class ControlTower:
    def __init__(self):
        self.aircrafts = []
        self.gates = []

    @classmethod
    def get_instance(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = ControlTower()
        return cls.instance

    def add_airplane(self, aircraft):
        self.aircrafts.append(aircraft)

    def aircraft_take_off(self, aircraft):
        msg = f"El avión {aircraft.get_ident()} ha despegado."
        print(f"Torre de Control: {msg}")
        self.notify(aircraft, msg)

        for gate in self.gates:
            if gate.get_flight_assigned().get_ident() == aircraft.get_flight_associated().get_id():
                gate.set_availability(True)
                break

    def aircraft_landed(self, aircraft):
        msg = f"El avión {aircraft.get_ident()} ha aterrizado."
        print(f"Torre de Control: {msg}")
        self.notify(aircraft, msg)

    def aircraft_in_flight(self, aircraft, ubicacion):
        msg = f"El avión {aircraft.get_ident()} informa su ubicación: {ubicacion}"
        print(f"Torre de Control: {msg}")
        self.notify(aircraft, msg)

    def notify(self, aircraft, msg):
        for other_aircraft in self.aircrafts:
            if other_aircraft != aircraft:
                other_aircraft.receive_info(msg)

    def assign_boarding_gate(self, flight):
        available_gate = None
        for gate in self.gates:
            if gate.is_available():
                available_gate = gate
                break

        if available_gate is not None:
            available_gate.set_flight_assigned(flight)
            available_gate.set_availability(False)
            available_gate.add_flights_record(flight)
            flight.set_boarding_gate(available_gate)
            print(f"El vuelo {flight.get_ident()} se ha asociado a la puerta: Gate {available_gate.get_ident()}")
        else:
            print("No hay puertas de embarque disponibles")