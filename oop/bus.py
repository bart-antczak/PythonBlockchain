from vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, starting_top_speed):
        super().__init__(starting_top_speed)
        self.passengers = []

    def add_group(self, passengers):
        self.passengers.extend(passengers)


bus1 = Bus(100)
bus1.add_group(['Bart', 'Martyna'])
print(bus1.passengers)
