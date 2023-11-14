from modeloDeRevista import TodoModel
class ControlTower:
    def __init__(self):
        self.aircrafts = []
        self.gates = []
        self.model = TodoModel()

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
        l = self.model.getAllPuertaDeEmbarque()
        for gate in l:
            if l[gate].is_available():
                available_gate = gate
                break

        if available_gate is not None:
            self.model.puerta_de_embarque[gate].set_flight_assigned(flight)
            self.model.puerta_de_embarque[gate].set_availability(False)
            self.model.puerta_de_embarque[gate].add_flights_record(flight)
            self.model.vuelo[flight].set_boarding_gate(available_gate)
            print(f"El vuelo {flight.get_ident()} se ha asociado a la puerta: Gate {available_gate.get_ident()}")
        else:
            print("No hay puertas de embarque disponibles")