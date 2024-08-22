class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        print(self.message)


class IncorrectCarNumbers:
    def __init__(self, message):
        self.message = message
        print(self.message)


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin) and self.__is_valid_numbers(numbers):
            self.__vin = vin
            self.__numbers = numbers
            print(f'{self.model} успешно создан')
        else:
            pass

    def __is_valid_vin(self, vin_number):
        try:
            if vin_number > 9999999 or vin_number < 1000000:
                raise IncorrectVinNumber('Некорректный тип vin номерa')
            if not isinstance(vin_number, int):
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
            return 1
        except:
            pass
        else:
            return 1

    def __is_valid_numbers(self, numbers):
        try:
            if len(numbers) != 6:
                raise IncorrectVinNumber('Некорректный тип данных для номеров')
            if not isinstance(numbers, str):
                raise IncorrectVinNumber('Неверная длина номера')
            return 1
        except:
            pass
        else:
            return 1


car1 = Car('Mod1', 5555555, 'r222op')
car2 = Car('Mod1', 55533335555, 'r222op')
car3 = Car('Mod1', 5555555, 'r2op')
