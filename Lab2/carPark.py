import car
import specialCar
import truck
import json
import copy
class CarPark:
    def __init__(self, name : str = "NOVALUE", trucks : list = [], specialCars : list = []):
        self.name = name
        self.trucks = trucks
        self.specialCars = specialCars

    def __str__(self) -> str:
        result = f"Автопарк: {self.name}\nГрузовики:\n"
        for truck in self.trucks:
            result += truck.__str__() + "\n"
        result += "Cпециализированная техника:\n"
        for specialCar in self.specialCars:
            result += specialCar.__str__() + "\n"
        return result

    def __repr__(self)-> str:
        return self.__str__()
# Сериализация
def SerializeCarPark(carPark : CarPark, path : str):
    with open(path, 'w') as outfile:
        dict = copy.deepcopy(carPark.__dict__)
        dict["trucks"] = [i.__dict__ for i in carPark.trucks]
        dict["specialCars"] = [i.__dict__ for i in carPark.specialCars]
        json.dump(dict, outfile, indent = 4, ensure_ascii = False)
# Десериализация
def DeserializeCarPark(path : str) -> CarPark:
    def Deserialize(dict):
        for i in CarPark().__dict__.keys():
            if not i in dict:
                break
        else:
            return CarPark(dict["name"], [Deserialize(i) for i in dict["trucks"]], [Deserialize(i) for i in dict["specialCars"]])
        for i in truck.Truck().__dict__.keys():
            if not i in dict:
                break
        else:
            return truck.Truck(dict["brand"], dict["model"], dict["price"], dict["capacity"])
        for i in specialCar.SpecialCar().__dict__.keys():
            if not i in dict:
                break
        else:
            return specialCar.SpecialCar(dict["brand"], dict["model"], dict["price"], dict["speciality"])
    with open(path, 'r') as infile:
        data = json.load(infile)
        return Deserialize(data)