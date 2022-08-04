class TableException(Exception):
    """Родительский класс моих ошибок"""
    pass


class OutException(TableException):
    """Точка за пределами поля"""
    pass


class DotException(TableException):
    """Точка недоступна"""
    pass


class ShipException(TableException):
    """Нельзя разместить корабль"""
    pass


class Board:
    def __init__(self, hide=False):
        self.hide = hide

    def __str__(self):
        field = [["0"] * 6 for i in range(6)]
        lane = "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, value in enumerate(field):
            lane += f"\n{i + 1} | " + " | ".join(value) + " | "

        if self.hide:
            lane = lane.replace("*", "0")

        return lane


class Dot:
    def __init__(self):
        pass


class Ship:
    def __init__(self):
        pass


a = Board(True)
print(a)
