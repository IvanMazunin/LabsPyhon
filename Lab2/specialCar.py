import car
class SpecialCar(car.Car):
    def __init__(self, brand, model, price, speciality):
        super().__init__(self, brand, model, price)
        self.speciality = speciality

    def  __str__(self) -> str:
        return super().__str__() + f"\tСпецаилизация: {self.speciality}"

    def __repr__(self)-> str:
        return "SpecialCar: " + self.__str__()