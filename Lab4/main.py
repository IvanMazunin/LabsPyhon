import csv

FILENAME: str = "data.csv";
OUTPUTFILE: str = "changed_data.csv"

# переопределенный map
def OverrideMap(func, sourceList: list) -> list:
    result = list()
    for obj in sourceList:
        result.append(func(obj))
    return result

# переопределенный reduce
def OverrideReduce(func, sourceList: list):
    index: int = 2
    length: int = len(sourceList)
    result = func(sourceList[0], sourceList[1])
    while (index < length):
        result = func(result, sourceList[index])
        index += 1
    return result

# Запись в .csv
def WriteInCSVFromListDict(dataSet: list, fileName: str):
    with open(fileName, "w", newline="") as file:
        columns = list(dataSet[0].keys())
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=',');
        writer.writeheader()
        writer.writerows(dataSet)

# Чтение из .csv
def ReadFromCSV(fileName: str) -> list:
    with open(fileName, "r", newline="") as file:
        reader = csv.DictReader(file)
        result = list()
        for dict in reader:
            result.append(dict)
    return result

# Разрезание записи
def SplitFullNameFromDict(sourceDict: dict) -> dict:
    result = dict()
    strs = sourceDict["ФИО"].split(' ')
    result["Фамилия"] = strs[0]
    result["Имя"] = strs[1]
    result["Оценка"] = sourceDict["Оценка"]
    return result

def GetSumFromDict(sourceDict1: dict, sourceDict2: dict) -> dict:
    resultDict = dict()
    resultDict["Оценка"] = float(sourceDict1["Оценка"]) + float(sourceDict2["Оценка"])
    return resultDict

# ЗАДАЧА 1, разрезать столбец ФИО на отдельные столбцы
dataSet: list = ReadFromCSV(FILENAME);
changedDataSet: list = OverrideMap(SplitFullNameFromDict, dataSet)
WriteInCSVFromListDict(changedDataSet, OUTPUTFILE)
# ЗАДАЧА 2, подсчёт средней оценки с помощью reduce
averageMark = OverrideReduce(GetSumFromDict, dataSet)["Оценка"]
averageMark = averageMark / dataSet.__len__()
print("Средняя оценка в классе: " + str(averageMark))