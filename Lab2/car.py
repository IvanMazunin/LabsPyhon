class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


    def __str__(self) -> str:
        return f"Марка: {self.brand}\t Тип: {self.model}\t Цена: {self.price}"


    def __repr__(self)-> str:
        return "Сar: " + self.__str__()