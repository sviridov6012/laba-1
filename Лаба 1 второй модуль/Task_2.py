class Furniture:

    def __init__(self, name: str, color: str):

        self.name = name
        self.color = color

    def get_name(self) -> str:

        return self.name

    def change_color(self, new_color: str) -> None:

        self.color = new_color

    def __str__(self) -> str:

        return f"{self.name} {self.color}"


class Chair(Furniture):

    def __init__(self, name: str, color: str, legs: int = 4):

        if legs < 3 or legs > 5:
            raise ValueError("Количество ножек должно быть от 3 до 5")

        super().__init__(name, color)
        self.legs = legs

    def sit(self) -> None:
        pass


class Table(Furniture):

    def __init__(self, name: str, color: str, shape: str = "прямоугольник"):

        if shape not in ["овал", "прямоугольник", "круг"]:
            raise ValueError("Форма должна быть овал, прямоугольник или круг")

        super().__init__(name, color)
        self.shape = shape

    def put(self, object: str) -> None:
        """ Ставит объект на стол. """
        pass


# Проверка работоспособности классов
if __name__ == "__main__":
    # Инстанцирование классов
    try:
        chair1 = Chair("Стул", "Красный", 4)
        print(f"Создан {chair1}; количество ножек: {chair1.legs}")

        chair2 = Chair("Стул", "Синий", 2)  # Неправильное количество ножек
        print(f"Создан {chair2}; количество ножек: {chair2.legs}")

        table1 = Table("Стол", "Коричневый", "прямоугольник")
        print(f"Создан {table1}; форма: {table1.shape}")

        table2 = Table("Стол", "Белый", "квадрат")  # Неправильная форма
        print(f"Создан {table2}; форма: {table2.shape}")
    except ValueError:
        print("Ошибка: неправильные данные")