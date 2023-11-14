class Crew:
    def __init__(self):
        self.tripu = []
        self.state = "Inhabilitado"

    def addWorker(self, worker):
        self.tripu.append(worker)
        if len(self.tripu) == 3 and self.state == "Inhabilitado":
            self.enableCrew()

    def enableCrew(self):
        if self.state == "Inhabilitado":
            self.state = "Habilitado"

    def useCrew(self):
        if self.state == "Habilitado":
            self.state = "En Uso"