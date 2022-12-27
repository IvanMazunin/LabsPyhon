import car
class Truck(car.Car):
    def __init__(self, brand, model, price, capacity):
        super().__init__(self, brand, model, price)
        self.capacity = capacity

    def  __str__(self) -> str:
        return super().__str__() + f"\tГрузоподъемность: {self.capacity}"

    def __repr__(self)-> str:
        return "Truck: " + self.__str__()