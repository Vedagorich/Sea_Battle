board = [[0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]]


class Board:  # создаем игровое поле

    def __init__(self, list_of_ships: list, game_board: list, hide: bool, living_ships: int):
        self.living_ships = living_ships
        self.hide = hide
        self.game_board = game_board
        self.list_of_ships = list_of_ships


def game_table(value):
    print("|",1,"|",2,"|",3,"|",4,"|",5,"|",6)
    for i in value:
        for i2 in i:
            print(f'|', i2, end=' ')
        print()

game_table(board)
