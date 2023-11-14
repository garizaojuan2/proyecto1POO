from aircraft import Aircraft

class PrivateJet(Aircraft):
    def __init__(self,  brand= None,  model= None,  ident= None,  capacity= None,  max_speed= None,  autonomy= None,  year= None,  condition= None,  ubication= None,  owner = None, _services = None, _destinations = None):
        super().__init__(brand, model, ident, capacity, max_speed, autonomy, year, condition, ubication)
        self.owner = owner
        self.services = _services
        self.destinations = _destinations

    def set_owner(self, owner):
        self.owner = owner

    def add_service(self, service):
        self.services.append(service)

    def add_destination(self, destination):
        self.destinations.append(destination)

    def get_owner(self):
        return self.owner

    def get_services(self):
        return self.services

    def get_destinations(self):
        return self.destinations