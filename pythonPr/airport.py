
class Airport:
    def __init__(self):
        self.gates_register = []
        self.airplane_register = []
        self.helicopter_register = []
        self.private_jet_register = []
        self.airport_crew = []
        self.passengers_registered = []
        self.airlines = []

    @staticmethod
    def get_instance():
        if not hasattr(Airport, "_instance"):
            Airport._instance = Airport()
        return Airport._instance

    def add_airline(self, a):
        self.airlines.append(a)
        
    def add_gate(self, gate):
        self.gates_register.append(gate)

    def add_airplane(self, airplane):
        self.airplane_register.append(airplane)

    def add_helicopter(self, helicopter):
        self.helicopter_register.append(helicopter)

    def add_jet(self, private_jet):
        self.private_jet_register.append(private_jet)

    def add_worker(self, worker):
        self.airport_crew.append(worker)

    def add_passenger(self, passenger):
        self.passengers_registered.append(passenger)


    def assign_flight(self, flight):
        i = 0
        flag = True
        origen = flight.origin
        while flag and i < len(self.airplane_register):
            flagCali = self.airplane_register[i].caliOrig
            if origen != 'Cali' or not flagCali:
                if self.airplane_register[i].state == "Disponible":
                    self.airplane_register[i].add_flight(flight)
                    flight.set_airplane(self.airplane_register[i])
                    flag = False
                    print(f"El vuelo ha sido asignado al avi贸n identificado con el c贸digo {self.airplane_register[i].get_id()}")
            i += 1
        if flag:
            print("No hay aviones disponibles, pero eso no es problema Cristiano Ronaldo te patrocina un nuevo avi贸n\nCrea tu avi贸n...")
            self.create_airplane()
            flight.set_airplane(self.airplane_register[-1])



    def get_passenger(self, n):
        return self.passengers_registered[n]

    def get_passengers_register_size(self):
        return len(self.passengers_registered)

    def get_airplane(self):
        return self.airplane_register

    def get_helicopter(self):
        return self.helicopter_register

    def get_private_jet(self):
        return self.private_jet_register
    
    def get_airlines(self):
        return self.airlines