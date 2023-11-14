from aircraft import Aircraft

class Airplane(Aircraft):
    def __init__(self,  brand = None,  model = None,  ident = None,  capacity = None,  max_speed = None,  autonomy = None,  year = None,  condition = None, max_altitude = None,  engine_amount = None,  category = None):
        super().__init__(brand, model, ident, capacity, max_speed, autonomy, year, condition)
        self.max_altitude = max_altitude
        self.engine_amount = engine_amount
        self.category = category

    def get_max_altitude(self):
        return self.max_altitude

    def get_engine_amount(self):
        return self.engine_amount

    def get_category(self):
        return self.category

    def set_max_altitude(self, new_max_altitude):
        self.max_altitude = new_max_altitude

    def set_engine_amount(self, new_engine_amount):
        self.engine_amount = new_engine_amount

    def set_category(self, new_category):
        self.category = new_category