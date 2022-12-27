import car
class Truck(car.Car):
    def __init__(self, brand : str = "NOVALUE", model : str = "NOVALUE", price : int = 0, capacity : int = 0):
        super().__init__(brand, model, price)
        self.capacity = capacity

    def  __str__(self) -> str:
        return super().__str__() + f"\tГрузоподъемность: {self.capacity}"

    def __repr__(self)-> str:
        return "Truck: " + self.__str__()