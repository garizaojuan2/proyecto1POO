class Flight:
    def __init__(self, _ident= None,  _date= None,  _origin= None,  _destination= None):
        self.ident = _ident
        self.date = _date
        self.origin = _origin
        self.destination = _destination
        self.assigned_crew = None
        self.boarding_gate = None
        self.passengers_registered = None
        self.airplane = None
        self.available_seats = 0

    def embark(self):
        ControlTower.get_instance().assign_boarding_gate(self)

    def set_airplane(self, airplane):
        self.airplane = airplane
        self.available_seats = airplane.get_capacity()
        
    def set_ident(self, ident):
        self.ident = ident
        
    def set_date(self, date):
        self.date = date
        
    def set_origin(self, origin):
        self.origin = origin

    def set_destination(self, destination):
        self.destination = destination
        
    def set_assigned_crew(self, assigned_crew):
        self.assigned_crew = assigned_crew

    def set_available_seats(self, num):
        self.available_seats = num

    def get_ident(self):
        return self.ident

    def get_date(self):
        return self.date

    def get_origin(self):
        return self.origin

    def get_destination(self):
        return self.destination

    def get_assigned_crew(self):
        return self.assigned_crew

    def get_boarding_gate(self):
        return self.boarding_gate

    def get_passengers_registered(self):
        return self.passengers_registered

    def get_airplane(self):
        return self.airplane

    def get_available_seats(self):
        return self.available_seats

    def set_boarding_gate(self, boarding_gate):
        self.boarding_gate = boarding_gate

    def set_passengers_registered(self, passenger):
        passenger_id = passenger.get_id()
        self.passengers_registered[passenger_id] = passenger