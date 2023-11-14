
class Aircraft:
    def __init__(self,  brand = None,  model = None,  ident = None,  capacity = None,  max_speed = None,  autonomy = None,  year = None,  condition = None):
        
        self.brand = brand
        self.model = model
        self.ident = ident
        self.capacity = capacity
        self.max_speed = max_speed
        self.autonomy = autonomy
        self.year = year
        self.condition = condition
        self.ubication = None
        self.flight_associated = None
        self.assigned_flights = []
        self.assigned_flightsNum = 0
        self.caliOrig = False
        self.state = "Disponible"

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_ident(self):
        return self.ident

    def get_capacity(self):
        return self.capacity

    def get_max_speed(self):
        return self.max_speed

    def get_autonomy(self):
        return self.autonomy

    def get_year(self):
        return self.year

    def get_condition(self):
        return self.condition

    def get_ubication(self):
        return self.ubication

    def get_state(self):
        return self.state

    def get_flight_associated(self):
        return self.flight_associated

    def get_assigned_flights(self):
        return len(self.assigned_flights)

    def set_brand(self, brand):
        self.brand = brand

    def set_model(self, model):
        self.model = model

    def set_ident(self, ident):
        self.ident = ident

    def set_capacity(self, capacity):
        self.capacity = capacity

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed

    def set_autonomy(self, autonomy):
        self.autonomy = autonomy

    def set_year(self, year):
        self.year = year

    def set_condition(self, condition):
        self.condition = condition

    def set_ubication(self, ubication):
        self.ubication = ubication

    def set_state(self, _state):
        self.state = _state

    def set_flight_associated(self, flight_associated):
        self.flight_associated = flight_associated
    
    def setAssociatedNum(self,num):
        self.assigned_flightsNum = num
        
    def setCaliOrig(self, b):
        self.caliOrig = b
        
    

    def take_off(self):
        ControlTower.get_instance().aircraft_take_off(self)

    def landed(self):
        ControlTower.get_instance().aircraft_landed(self)

    def report_location(self, ubicacion):
        ControlTower.get_instance().aircraft_in_flight(self, ubicacion)

    def recibe_info(self, mensaje):
        print(f"Avion {self.ident} recibio un mensaje: {mensaje}")

    def add_flight(self, flight):
        self.assigned_flights.append(flight)