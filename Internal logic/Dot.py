class Dot:  # создаем точку на игровом поле

    def __init__(self, coordinate_x: int, coordinate_y: int):
        self.x = coordinate_x
        self.y = coordinate_y

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, value):
        self._y = value
