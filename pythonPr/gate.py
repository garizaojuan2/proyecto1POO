class Gate:
    def __init__(self, ident = None, location = None, availability = None, boarding_hour = None):
        self.ident = ident
        self.location = location
        self.availability = availability
        self.boarding_hour = boarding_hour
        self.flight_assigned = None
        self.flights_record = []

    def set_flight_assigned(self, flight_assigned):
        self.flight_assigned = flight_assigned

    def set_ident(self, ident):
        self.ident = ident

    def set_location(self, location):
        self.location = location

    def set_availability(self, availability):
        self.availability = availability

    def set_boarding_hour(self, boarding_hour):
        self.boarding_hour = boarding_hour

    def get_flight_assigned(self):
        return self.flight_assigned

    def get_ident(self):
        return self.ident

    def get_location(self):
        return self.location

    def is_available(self):
        return self.availability

    def get_boarding_hour(self):
        return self.boarding_hour

    def get_flights_record(self):
        return self.flights_record

    def add_flights_record(self, flight):
        self.flights_record.append(flight)