class Furniture:
    """
    Базовый класс для мебели.

    Атрибуты:
        name (str): Название мебели.
        color (str): Цвет мебели.
    """

    def __init__(self, name: str, color: str):
        """
        Конструктор для класса мебели.

        Аргументы:
            name (str): Название мебели.
            color (str): Цвет мебели.
        """

        self.name = name
        self.color = color

    def get_name(self) -> str:
        """
        Возвращает название мебели.

        Пример:
            >>> furniture = Furniture("Стул", "Красный")
            >>> furniture.get_name()
            'Стул'
        """
        return self.name

    def change_color(self, new_color: str) -> None:
        """
        Меняет цвет мебели на новый цвет.

        Аргументы:
            new_color (str): Новый цвет мебели.
        """

        self.color = new_color

    def __str__(self) -> str:
        """
        Возвращает строковое представление мебели.

        Пример:
            >>> furniture = Furniture("Стул", "Красный")
            >>> str(furniture)
            'Стул Красный'
        """
        return f"{self.name} {self.color}"


class Chair(Furniture):
    """
    Класс, описывающий стул.

    Атрибуты:
        name (str): Название стула.
        color (str): Цвет стула.
        legs (int): Количество ножек у стула.
    """

    def __init__(self, name: str, color: str, legs: int = 4):
        """
        Конструктор для класса стула.

        Аргументы:
            name (str): Название стула.
            color (str): Цвет стула.
            legs (int, optional): Количество ножек у стула (по умолчанию 4).
        """

        if legs < 3 or legs > 5:
            raise ValueError("Количество ножек должно быть от 3 до 5")

        super().__init__(name, color)
        self.legs = legs

    def sit(self) -> None:
        """
        Сидит на стуле.

        Пример:
            >>> chair = Chair("Стул", "Красный")
            >>> chair.sit()
        """
        pass

    def change_color(self, new_color: str) -> None:
        """
        Меняет цвет стула на новый цвет.

        Аргументы:
            new_color (str): Новый цвет стула.
        """
        self.color = new_color


class Table(Furniture):
    """
    Класс, описывающий стол.

    Атрибуты:
        name (str): Название стола.
        color (str): Цвет стола.
        shape (str): Форма стола (овал, прямоугольник, круг).
    """

    def __init__(self, name: str, color: str, shape: str = "прямоугольник"):
        """
        Конструктор для класса стола.

        Аргументы:
            name (str): Название стола.
            color (str): Цвет стола.
            shape (str, optional): Форма стола (по умолчанию "прямоугольник").
        """

        if shape not in ["овал", "прямоугольник", "круг"]:
            raise ValueError("Форма должна быть овал, прямоугольник или круг")

        super().__init__(name, color)
        self.shape = shape

    def put(self, object: str) -> None:
        """
        Ставит объект на стол.

        Аргументы:
            object (str): Объект, который ставится на стол.

        Пример:
            >>> table = Table("Стол", "Коричневый")
            >>> table.put("Ваза")
        """
        pass