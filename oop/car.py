from vehicle import Vehicle


class Car(Vehicle):
    def brag(self):
        print('Look how cool my car is!')


car1 = Car(300)
car1.drive()
car1.add_warning('New warning')
print(car1)

car2 = Car(200)
car2.drive()
print(car2.get_warnigns())
