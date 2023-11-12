
class Airport:
    def __init__(self):
        self.flights_register = {}
        self.gates_register = []
        self.airplane_register = []
        self.helicopter_register = []
        self.private_jet_register = []
        self.airport_crew = []
        self.passengers_registered = []

    @staticmethod
    def get_instance():
        if not hasattr(Airport, "_instance"):
            Airport._instance = Airport()
        return Airport._instance

    def add_flight(self, flight):
        key = (flight.destination, flight.date)
        self.flights_register[key] = flight

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

    def create_airplane(self):
        airplane = Airplane()
        try:
            brand = input("Digite la marca: ")
            model = input("Digite el modelo: ")
            id = input("Digite el ID: ")
            capacity = int(input("Digite la capacidad: "))
            max_speed = int(input("Digite la velocidad maxima: "))
            autonomy = int(input("Digite la autonomia: "))
            year = int(input("Digite el ano: "))
            condition = input("Digite la condicion: ")
            ubication = input("Digite la ubicacion: ")
            max_altitude = int(input("Digite la altitud maxima: "))
            engine_amount = int(input("Digite la cantidad de motores: "))
            category = input("Digite la categoria: ")
            airplane.set_brand(brand)
            airplane.set_model(model)
            airplane.set_id(id)
            airplane.set_capacity(capacity)
            airplane.set_max_speed(max_speed)
            airplane.set_autonomy(autonomy)
            airplane.set_year(year)
            airplane.set_condition(condition)
            airplane.set_ubication(ubication)
            airplane.set_max_altitude(max_altitude)
            airplane.set_engine_amount(engine_amount)
            airplane.set_category(category)
            airplane.set_availability(True)
            self.add_airplane(airplane)
        except ValueError:
            print("Error: Asegúrate de ingresar números enteros para la capacidad, velocidad máxima, autonomía, año, altitud máxima, cantidad de motores.")
            del airplane

    def create_flight(self):
        flight = Flight()
        try:
            id = int(input("Digite el ID del vuelo: "))
            date = input("Digite la fecha del vuelo: ")
            origin = input("Digite el origen: ")
            destination = input("Digite el destino: ")
            flight.set_id(id)
            flight.set_date(date)
            flight.set_origin(origin)
            flight.set_destination(destination)
            self.add_flight(flight)
        except ValueError:
            print("Error: Asegúrate de ingresar un número entero para el ID del vuelo.")
            del flight

    def create_gate(self):
        gate = Gate()
        location = input("Digite la ubicacion de la puerta: ")
        boarding_hour = input("Digite la hora de abordaje: ")
        gate.set_location(location)
        gate.set_boarding_hour(boarding_hour)
        self.add_gate(gate)

    def create_passenger(self):
        passenger = Passenger()
        try:
            id = int(input("Digite el ID del pasajero: "))
            name = input("Digite el nombre del pasajero: ")
            last_name = input("Digite el apellido del pasajero: ")
            birthdate = input("Digite la fecha de nacimiento del pasajero (YYYY-MM-DD): ")
            gender = input("Digite el género del pasajero: ")
            address = input("Digite la dirección del pasajero: ")
            phone_number = int(input("Digite el número de teléfono del pasajero: "))
            email = input("Digite el correo electrónico del pasajero: ")
            nationality = input("Digite la nacionalidad del pasajero: ")
            baggage_amount = int(input("Digite la cantidad de equipaje del pasajero: "))
            medical_information = input("Digite información médica del pasajero: ")
            passenger.set_id(id)
            passenger.set_name(name)
            passenger.set_last_name(last_name)
            passenger.set_birthdate(birthdate)
            passenger.set_gender(gender)
            passenger.set_address(address)
            passenger.set_phone_number(phone_number)
            passenger.set_email(email)
            passenger.set_nationality(nationality)
            passenger.set_baggage_amount(baggage_amount)
            passenger.set_medical_information(medical_information)
            self.add_passenger(passenger)
        except ValueError:
            print("Error: Asegúrate de ingresar un número entero para el ID del pasajero y el número de teléfono.")
            del passenger

    def create_worker(self):
        worker = Worker()
        try:
            id = int(input("Digite el ID del trabajador: "))
            name = input("Digite el nombre del trabajador: ")
            last_name = input("Digite el apellido del trabajador: ")
            birthdate = input("Digite la fecha de nacimiento del trabajador (YYYY-MM-DD): ")
            gender = input("Digite el género del trabajador: ")
            address = input("Digite la dirección del trabajador: ")
            phone_number = int(input("Digite el número de teléfono del trabajador: "))
            email = input("Digite el correo electrónico del trabajador: ")
            position = input("Digite la posición del trabajador: ")
            years_of_experience = int(input("Digite los años de experiencia del trabajador: "))
            max_daily_hours = int(input("Digite el máximo de horas diarias del trabajador: "))
            worker.set_id(id)
            worker.set_name(name)
            worker.set_last_name(last_name)
            worker.set_birthdate(birthdate)
            worker.set_gender(gender)
            worker.set_address(address)
            worker.set_phone_number(phone_number)
            worker.set_email(email)
            worker.set_position(position)
            worker.set_years_of_experience(years_of_experience)
            worker.set_max_daily_hours(max_daily_hours)
            self.add_worker(worker)
        except ValueError:
            print("Error: Asegúrate de ingresar un número entero para el ID del trabajador, número de teléfono, años de experiencia y máximo de horas diarias.")
            del worker

    def create_private_jet(self):
        private_jet = PrivateJet()
        brand = input("Digite la marca: ")
        model = input("Digite el modelo: ")
        id = input("Digite el ID: ")
        capacity = int(input("Digite la capacidad: "))
        max_speed = int(input("Digite la velocidad máxima: "))
        autonomy = int(input("Digite la autonomía: "))
        year = int(input("Digite el año: "))
        condition = input("Digite la condición: ")
        ubication = input("Digite la ubicación: ")
        private_jet.set_brand(brand)
        private_jet.set_model(model)
        private_jet.set_id(id)
        private_jet.set_capacity(capacity)
        private_jet.set_max_speed(max_speed)
        private_jet.set_autonomy(autonomy)
        private_jet.set_year(year)
        private_jet.set_condition(condition)
        private_jet.set_ubication(ubication)
        private_jet.set_availability(True)
        self.add_jet(private_jet)

    def create_helicopter(self):
        helicopter = Helicopter()
        brand = input("Digite la marca: ")
        model = input("Digite el modelo: ")
        id = input("Digite el ID: ")
        capacity = int(input("Digite la capacidad: "))
        max_speed = int(input("Digite la velocidad máxima: "))
        autonomy = int(input("Digite la autonomía: "))
        year = int(input("Digite el año: "))
        condition = input("Digite la condición: ")
        ubication = input("Digite la ubicación: ")
        engine_amount = int(input("Digite la cantidad de motores: "))
        elevation_capacity = int(input("Digite la capacidad de elevación: "))
        use = input("Digite el uso del helicóptero: ")
        helicopter.set_brand(brand)
        helicopter.set_model(model)
        helicopter.set_id(id)
        helicopter.set_capacity(capacity)
        helicopter.set_max_speed(max_speed)
        helicopter.set_autonomy(autonomy)
        helicopter.set_year(year)
        helicopter.set_condition(condition)
        helicopter.set_ubication(ubication)
        helicopter.set_engine_amount(engine_amount)
        helicopter.set_elevation_capacity(elevation_capacity)
        helicopter.set_use(use)
        helicopter.set_availability(True)
        self.add_helicopter(helicopter)

    def assign_flight(self, flight):
        i = 0
        flag = True
        while flag and i < len(self.airplane_register):
            if self.airplane_register[i].get_assigned_flights() < 3:
                self.airplane_register[i].add_flight(flight)
                flight.set_airplane(self.airplane_register[i])
                flag = False
                print(f"El vuelo ha sido asignado al avión identificado con el código {self.airplane_register[i].get_id()}")
            i += 1
        if flag:
            print("No hay aviones disponibles, pero eso no es problema Cristiano Ronaldo te patrocina un nuevo avión\nCrea tu avión...")
            self.create_airplane()

    def buy_flight(self, destination, date, passenger):
        flight = self.flights_register.get((destination, date))
        if flight:
            seats = flight.get_available_seats()
            if seats <= 0:
                print("El vuelo para el destino y fecha seleccionada, no se encuentra disponible")
            else:
                print("Su reserva ha sido exitosa")
                flight.set_available_seats(seats - 1)
                flight.set_passengers_registered(passenger)
        else:
            print("El vuelo no existe para ese destino o fecha")

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