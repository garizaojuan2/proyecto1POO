from aircraft import Aircraft

class Helicopter(Aircraft):
    def __init__(self,  brand= None,  model= None,  ident= None,  capacity= None,  max_speed= None,  autonomy= None,  year= None,  condition= None,    engine_amount= None,  elevation_capacity= None,  use = None):
        super().__init__(brand, model, ident, capacity, max_speed, autonomy, year, condition)
        self.engine_amount = engine_amount
        self.elevation_capacity = elevation_capacity
        self.use = use

    def get_engine_amount(self):
        return self.engine_amount

    def get_elevation_capacity(self):
        return self.elevation_capacity

    def get_use(self):
        return self.use

    def set_engine_amount(self, new_engine_amount):
        self.engine_amount = new_engine_amount

    def set_elevation_capacity(self, new_elevation_capacity):
        self.elevation_capacity = new_elevation_capacity

    def set_use(self, new_use):
        self.use = new_use