from car import *
from carPark import *
from truck import *
from specialCar import *

carPark = CarPark("Автопарк №1",
    [
        Truck("Volvo", "Самосвал", 8000000, 12),
        Truck("ГАЗ", "Седельный тягач", 7500000, 10),
        Truck("Man", "Бортовой автомобиль", 12000000, 15)
    ],
    [
        SpecialCar("ГАЗ", "Газель", 5500000, "Скорая помощь"),
        SpecialCar("Man", "Седан", 1500000, "Полицейский транспорт")
    ])
SerializeCarPark(carPark, "data.json")
print(carPark)
deserialized = DeserializeCarPark("data.json")
print(deserialized)