from modeloDeRevista import TodoModel

class ControlTower:
    def __init__(self):
        """
        Constructor de la clase ControlTower.

        Inicializa la torre de control con listas vacías de aeronaves, puertas de embarque y utiliza
        una instancia del modelo TodoModel para gestionar los datos del aeropuerto.
        """
        self.aircrafts = []
        self.gates = []
        self.model = TodoModel()

    @classmethod
    def get_instance(cls):
        """
        Método de clase para obtener una instancia única de la clase ControlTower mediante el patrón singleton.

        Retorna:
        - ControlTower: Instancia única de la clase ControlTower.
        """
        if not hasattr(cls, 'instance'):
            cls.instance = ControlTower()
        return cls.instance

    def add_airplane(self, aircraft):
        """
        Agrega una aeronave a la lista de aeronaves controladas por la torre.

        Parámetros:
        - aircraft (Airplane): Objeto Airplane que representa la aeronave a agregar.
        """
        self.aircrafts.append(aircraft)

    def aircraft_take_off(self, aircraft):
        """
        Simula el despegue de una aeronave y notifica a otras aeronaves.

        Parámetros:
        - aircraft (Airplane): Objeto Airplane que representa la aeronave que despega.
        """
        msg = f"El avión {aircraft.get_ident()} ha despegado."
        print(f"Torre de Control: {msg}")
        self.notify(aircraft, msg)

        for gate in self.gates:
            if gate.get_flight_assigned().get_ident() == aircraft.get_flight_associated().get_id():
                gate.set_availability(True)
                break

    def aircraft_landed(self, aircraft):
        """
        Simula el aterrizaje de una aeronave y notifica a otras aeronaves.

        Parámetros:
        - aircraft (Airplane): Objeto Airplane que representa la aeronave que aterriza.
        """
        msg = f"El avión {aircraft.get_ident()} ha aterrizado."
        print(f"Torre de Control: {msg}")
        self.notify(aircraft, msg)

    def aircraft_in_flight(self, aircraft, location):
        """
        Informa la ubicación de una aeronave en vuelo y notifica a otras aeronaves.

        Parámetros:
        - aircraft (Airplane): Objeto Airplane que representa la aeronave en vuelo.
        - location (str): Ubicación actual de la aeronave.
        """
        msg = f"El avión {aircraft.get_ident()} informa su ubicación: {location}"
        print(f"Torre de Control: {msg}")
        self.notify(aircraft, msg)

    def notify(self, aircraft, msg):
        """
        Notifica a otras aeronaves sobre un mensaje específico.

        Parámetros:
        - aircraft (Airplane): Objeto Airplane que envía la notificación.
        - msg (str): Mensaje a enviar.
        """
        for other_aircraft in self.aircrafts:
            if other_aircraft != aircraft:
                other_aircraft.receive_info(msg)

    def assign_boarding_gate(self, flight):
        """
        Asigna una puerta de embarque a un vuelo disponible.

        Parámetros:
        - flight (Flight): Objeto Flight que representa el vuelo al cual se le asignará la puerta de embarque.
        """
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
