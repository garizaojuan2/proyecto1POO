
class Airport:
    def __init__(self):
        """
        Constructor de la clase Airport.

        Inicializa las listas y registros para gestionar puertas de embarque, aviones,
        helicópteros, jets privados, personal del aeropuerto, pasajeros y aerolíneas.
        """
        self.gates_register = []
        self.airplane_register = []
        self.helicopter_register = []
        self.private_jet_register = []
        self.airport_crew = []
        self.passengers_registered = []
        self.airlines = []

    @staticmethod
    def get_instance():
        """
        Método estático para obtener una instancia única de la clase Airport mediante el patrón singleton.

        Retorna:
        - Airport: Instancia única de la clase Airport.
        """
        if not hasattr(Airport, "_instance"):
            Airport._instance = Airport()
        return Airport._instance

    def add_airline(self, airline):
        """
        Agrega una aerolínea a la lista de aerolíneas del aeropuerto.

        Parámetros:
        - airline (Airline): Objeto Airline que representa la aerolínea a agregar.
        """
        self.airlines.append(airline)

    def add_gate(self, gate):
        """
        Agrega una puerta de embarque a la lista de puertas de embarque del aeropuerto.

        Parámetros:
        - gate (Gate): Objeto Gate que representa la puerta de embarque a agregar.
        """
        self.gates_register.append(gate)

    def add_airplane(self, airplane):
        """
        Agrega un avión a la lista de aviones del aeropuerto.

        Parámetros:
        - airplane (Airplane): Objeto Airplane que representa el avión a agregar.
        """
        self.airplane_register.append(airplane)

    def add_helicopter(self, helicopter):
        """
        Agrega un helicóptero a la lista de helicópteros del aeropuerto.

        Parámetros:
        - helicopter (Helicopter): Objeto Helicopter que representa el helicóptero a agregar.
        """
        self.helicopter_register.append(helicopter)

    def add_jet(self, private_jet):
        """
        Agrega un jet privado a la lista de jets privados del aeropuerto.

        Parámetros:
        - private_jet (PrivateJet): Objeto PrivateJet que representa el jet privado a agregar.
        """
        self.private_jet_register.append(private_jet)

    def add_worker(self, worker):
        """
        Agrega un trabajador a la lista de personal del aeropuerto.

        Parámetros:
        - worker (Worker): Objeto Worker que representa al trabajador a agregar.
        """
        self.airport_crew.append(worker)

    def add_passenger(self, passenger):
        """
        Agrega un pasajero a la lista de pasajeros registrados en el aeropuerto.

        Parámetros:
        - passenger (Passenger): Objeto Passenger que representa al pasajero a agregar.
        """
        self.passengers_registered.append(passenger)

    def assign_flight(self, flight):
        """
        Asigna un vuelo a un avión disponible en el aeropuerto.

        Parámetros:
        - flight (Flight): Objeto Flight que representa el vuelo a asignar.
        """
        i = 0
        flag = True
        origin = flight.origin
        while flag and i < len(self.airplane_register):
            flag_cali = self.airplane_register[i].caliOrig
            if origin != 'Cali' or not flag_cali:
                if self.airplane_register[i].state == "Disponible":
                    self.airplane_register[i].add_flight(flight)
                    flight.set_airplane(self.airplane_register[i])
                    flag = False
                    print(f"El vuelo ha sido asignado al avión identificado con el código {self.airplane_register[i].get_id()}")
            i += 1
        if flag:
            print("No hay aviones disponibles, pero eso no es problema. Cristiano Ronaldo te patrocina un nuevo avión.\nCrea tu avión...")
            self.create_airplane()
            flight.set_airplane(self.airplane_register[-1])

    def get_passenger(self, n):
        """
        Obtiene un pasajero de la lista de pasajeros registrados.

        Parámetros:
        - n (int): Índice del pasajero en la lista.

        Retorna:
        - Passenger: Objeto Passenger correspondiente al índice especificado.
        """
        return self.passengers_registered[n]

    def get_passengers_register_size(self):
        """
        Obtiene el tamaño de la lista de pasajeros registrados.

        Retorna:
        - int: Tamaño de la lista de pasajeros registrados.
        """
        return len(self.passengers_registered)

    def get_airplane(self):
        """
        Obtiene la lista de aviones registrados en el aeropuerto.

        Retorna:
        - list: Lista de objetos Airplane representando aviones registrados.
        """
        return self.airplane_register

   
