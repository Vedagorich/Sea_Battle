from tkinter import *
from tkinter import messagebox
import time
import random

tk = Tk()
app_running = True

size_canvas_x = 500
size_canvas_y = 500
s_x = s_y = 6  # размер игрового поля
step_x = size_canvas_x // s_x  # шаг по горизонтали
step_y = size_canvas_y // s_y  # шаг по вертикали
size_canvas_x = step_x * s_x
size_canvas_y = step_y * s_y
delta_menu_x = 4

menu_x = step_x * delta_menu_x  # размер меню по X
menu_y = 40  # размер меню по Y

ships = (s_x // 2)+1  # определяем макс кол-во кораблей
ship_len1 = s_x // 5  # длина первого корабля
ship_len2 = s_x // 3 # длина второго корабля
ship_len3 = s_x // 2 # длина третьего корабля
enemy_ships1 = [[0 for i in range(s_x + 1)] for i in range(s_y + 1)]  # список кораблей игрока
enemy_ships2 = [[0 for i in range(s_x + 1)] for i in range(s_y + 1)]  # список кораблей компьютера
list_ids = []  # список объектов canvas

# список куда мы кликнули мышкой
points1 = [[-1 for i in range(s_x)] for i in range(s_y)]
points2 = [[-1 for i in range(s_x)] for i in range(s_y)]

# список попаданий по коблям противника
boom = [[0 for i in range(s_x)] for i in range(s_y)]

# список кораблей компьютера
ships_list = []

# Если True, то ходит Компьютер. Если FALSE, то ходит игрок.
hod_igrovomu_polu_1 = False


computer_vs_human = True
if computer_vs_human:
    add_to_label = "(ИИ)"
    hod_igrovomu_polu_1 = False
else:
    add_to_label = ""


# print(enemy_ships1)


def on_closing():  # функция выхода из игры
    global app_running
    if messagebox.askokcancel("Выход из игры", "Хотите выйти?"):
        app_running = False
        tk.destroy()


# характеристики нашего приложения и отрисовка поля.
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Морской бой")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=size_canvas_x + menu_x + size_canvas_x, height=size_canvas_y + menu_y, bd=0,
                highlightthickness=0)
canvas.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill="white")  # область игрока
canvas.create_rectangle(size_canvas_x + menu_x, 0, size_canvas_x + menu_x + size_canvas_x, size_canvas_y,
                        fill="gray")  # область компьютера
canvas.pack()
tk.update()


def draw_table(offset_x=0):  # функция отрисовки ячеек на поле
    for i in range(0, s_x + 1):
        canvas.create_line(offset_x + step_x * i, 0, offset_x + step_x * i, size_canvas_y)
    for i in range(0, s_y + 1):
        canvas.create_line(offset_x, step_y * i, offset_x + size_canvas_x, step_y * i)


draw_table()
draw_table(size_canvas_x + menu_x)

# создаем название полям игрока и компа
t0 = Label(tk, text="ИГРОК", font=("Helvetica", 16))
t0.place(x=size_canvas_x // 2 - t0.winfo_reqwidth() // 2, y=size_canvas_y + 3)
t1 = Label(tk, text="КОМПЬЮТЕР" + add_to_label, font=("Helvetica", 16))
t1.place(x=size_canvas_x + menu_x + size_canvas_x // 2 - t1.winfo_reqwidth() // 2, y=size_canvas_y + 3)

# цветом выделяем ход игрока
t0.configure(bg="red")
t0.configure(bg="#f0f0f0")

t3 = Label(tk, text="ОТЛАДКА", font=("Helvetica", 18))
t3.place(x=size_canvas_x + step_x, y=3*step_y)


def mark_igrok(mark_igrok1):
    if mark_igrok1:
        t1.configure(bg="red")
        t0.configure(bg="#f0f0f0")
        t3.configure(text="Ход КОМПЬЮТЕРА")
    else:
        t0.configure(bg="red")
        t1.configure(bg="#f0f0f0")
        t3.configure(text="Ход ИГРОКА")


mark_igrok(hod_igrovomu_polu_1)


def button_show_enemy1():  # кнопка отрисовывает все корабли противника
    for i in range(0, s_x):
        for j in range(0, s_y):
            if enemy_ships1[j][i] > 0:
                color = "red"
                if points1[j][i] != -1:
                    color = "green"
                _id = canvas.create_rectangle(i * step_x, j * step_y, i * step_x + step_x, j * step_y + step_y,
                                              fill=color)
                list_ids.append(_id)


def button_show_enemy2():  # кнопка отрисовывает все корабли противника
    for i in range(0, s_x):
        for j in range(0, s_y):
            if enemy_ships2[j][i] > 0:
                color = "red"
                if points2[j][i] != -1:
                    color = "green"
                _id = canvas.create_rectangle(size_canvas_x + menu_x + i * step_x, j * step_y, size_canvas_x + menu_x + i * step_x + step_x, j * step_y + step_y,
                                              fill=color)
                list_ids.append(_id)


def button_begin_again():  # функция сброса и размещения кораблей на поле
    global list_ids
    global points1, points2
    global boom
    global enemy_ships1
    global enemy_ships2

    for el in list_ids:
        canvas.delete(el)
    list_ids = []
    generate_ship_list()
    enemy_ships1 = generate_enemy_ships()
    enemy_ships2 = generate_enemy_ships()
    points1 = [[-1 for i in range(s_x)] for i in range(s_y)]
    points2 = [[-1 for i in range(s_x)] for i in range(s_y)]
    boom = [[0 for i in range(s_x)] for i in range(s_y)]


# b0 = Button(tk, text="показать корабли ИГРОКА", command=button_show_enemy1)
# b0.place(x=size_canvas_x + 20, y=30)
#
# b1 = Button(tk, text="показать корабли КОМПЬЮТЕРА", command=button_show_enemy2)
# b1.place(x=size_canvas_x + 20, y=70)

b2 = Button(tk, text="Начать заново!", command=button_begin_again)
b2.place(x=size_canvas_x + 110, y=490)


def draw_point(x, y):
    # print(enemy_ships1[y][x])
    if enemy_ships1[y][x] == 0:
        color = "red"
        id1 = canvas.create_oval(x * step_x, y * step_y, x * step_x + step_x, y * step_y + step_y, fill=color)
        id2 = canvas.create_oval(x * step_x + step_x // 3, y * step_y + step_y // 3, x * step_x + step_x - step_x // 3,
                                 y * step_y + step_y - step_y // 3, fill="white")
        list_ids.append(id1)
        list_ids.append(id2)

    elif enemy_ships1[y][x] > 0:
        color = "blue"
        id1 = canvas.create_oval(x * step_x, y * step_y + step_y // 2 - step_y // 10, x * step_x + step_x,
                                 y * step_y + step_y // 2 + step_y // 10, fill=color)
        id2 = canvas.create_oval(x * step_x + step_x // 2 - step_x // 10, y * step_y,
                                 x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color)
        list_ids.append(id1)
        list_ids.append(id2)


def draw_point2(x, y, offset_x=size_canvas_x + menu_x):
    # print(enemy_ships1[y][x])
    if enemy_ships2[y][x] == 0:
        color = "red"
        id1 = canvas.create_oval(offset_x + x * step_x, y * step_y, offset_x + x * step_x + step_x, y * step_y + step_y, fill=color)
        id2 = canvas.create_oval(offset_x + x * step_x + step_x // 3, y * step_y + step_y // 3, offset_x + x * step_x + step_x - step_x // 3,
                                 y * step_y + step_y - step_y // 3, fill="white")
        list_ids.append(id1)
        list_ids.append(id2)

    elif enemy_ships2[y][x] > 0:
        color = "blue"
        id1 = canvas.create_oval(offset_x + x * step_x, y * step_y + step_y // 2 - step_y // 10,offset_x + x * step_x + step_x,
                                 y * step_y + step_y // 2 + step_y // 10, fill=color)
        id2 = canvas.create_oval(offset_x + x * step_x + step_x // 2 - step_x // 10, y * step_y,
                                 offset_x + x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color)
        list_ids.append(id1)
        list_ids.append(id2)


def check_winner2():
    win = True
    for i in range(0, s_x):
        for j in range(0, s_y):
            if enemy_ships1[j][i] > 0:
                if points1[j][i] == -1:
                    win = False

    return win


def check_winner2_igrok_2():
    win = True
    for i in range(0, s_x):
        for j in range(0, s_y):
            if enemy_ships2[j][i] > 0:
                if points2[j][i] == -1:
                    win = False

    return win


def hod_computer():
    global points1, points2, hod_igrovomu_polu_1
    tk.update()
    time.sleep(1)
    hod_igrovomu_polu_1 = False
    ip_x = random.randint(0, s_x-1)
    ip_y = random.randint(0, s_y-1)
    while not points1[ip_y][ip_x] == -1:
        ip_x = random.randint(0, s_x-1)
        ip_y = random.randint(0, s_y-1)
    points1[ip_y][ip_x] = 7
    draw_point(ip_x, ip_y)
    if check_winner2():
        winner = "Победа КОМПЬЮТЕРА!!!"
        print(winner)
        points1 = [[10 for i in range(s_x)] for i in range(s_y)]
        points2 = [[10 for i in range(s_x)] for i in range(s_y)]
        id1 = canvas.create_rectangle(step_x * 3, step_y * 3, size_canvas_x + menu_x + size_canvas_x - step_x * 3,
                                      size_canvas_y - step_y, fill="green")  # банер победителя
        list_ids.append(id1)
        id2 = canvas.create_rectangle(step_x * 3 + step_x // 2, step_y * 3 + step_y // 2,
                                      size_canvas_x + menu_x + size_canvas_x - step_x * 3 - step_x // 2,
                                      size_canvas_y - step_y - step_y // 2, fill="yellow")
        list_ids.append(id2)
        id3 = canvas.create_text(step_x * 8, step_y * 4, text=winner, font=("Arial", 40), justify=CENTER)
        list_ids.append(id3)


def add_to_all(event):  # координаты клика мышкой
    global points1, points2, hod_igrovomu_polu_1
    _type = 0  # ЛКМ
    if event.num == 3:
        _type = 1  # ПКМ
    # print(_type)
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    # print(mouse_x, mouse_y)

    ip_x = mouse_x // step_x
    ip_y = mouse_y // step_y

    # первое игровое поле
    print(ip_x, ip_y, "_type:", _type)
    if ip_x < s_x and ip_y < s_y and hod_igrovomu_polu_1:       # проверка, что клик в пределах игр. области игрока
        if points1[ip_y][ip_x] == -1:
            points1[ip_y][ip_x] = _type
            hod_igrovomu_polu_1 = False
            draw_point(ip_x, ip_y)
            if check_winner2():
                hod_igrovomu_polu_1 = True
                winner = "Победа КОМПЬЮТЕРА!!!"
                print(winner)
                points1 = [[10 for i in range(s_x)] for i in range(s_y)]
                points2 = [[10 for i in range(s_x)] for i in range(s_y)]
                id1 = canvas.create_rectangle(step_x * 3, step_y * 3, size_canvas_x + menu_x + size_canvas_x-step_x*3, size_canvas_y - step_y, fill="green") # банер победителя
                list_ids.append(id1)
                id2 = canvas.create_rectangle(step_x * 3 + step_x//2, step_y * 3 + step_y//2,
                                              size_canvas_x + menu_x + size_canvas_x - step_x * 3-step_x//2,
                                              size_canvas_y - step_y - step_y//2, fill="yellow")
                list_ids.append(id2)
                id3 = canvas.create_text(step_x*8, step_y*4, text=winner, font=("Arial", 40), justify=CENTER)
                list_ids.append(id3)
        #print(len(list_ids))

    # второе игровое поле
    if ip_x >= s_x + delta_menu_x and ip_x <= s_x + s_x + delta_menu_x and ip_y < s_y and not hod_igrovomu_polu_1:    # Проверка, что клик в пределах игр. области компьютера
        if points2[ip_y][ip_x - s_x - delta_menu_x] == -1:
            points2[ip_y][ip_x - s_x - delta_menu_x] = _type
            hod_igrovomu_polu_1 = True
            draw_point2(ip_x - s_x - delta_menu_x, ip_y)
            if check_winner2_igrok_2():
                hod_igrovomu_polu_1 = False
                winner = "Победа ИГРОКА!!!"
                print(winner)
                points2 = [[10 for i in range(s_x)] for i in range(s_y)]
                id1 = canvas.create_rectangle(step_x * 3, step_y * 3,
                                              size_canvas_x + menu_x + size_canvas_x - step_x * 3,
                                              size_canvas_y - step_y, fill="green")  # банер победителя
                list_ids.append(id1)
                id2 = canvas.create_rectangle(step_x * 3 + step_x // 2, step_y * 3 + step_y // 2,
                                              size_canvas_x + menu_x + size_canvas_x - step_x * 3 - step_x // 2,
                                              size_canvas_y - step_y - step_y // 2, fill="yellow")
                list_ids.append(id2)
                id3 = canvas.create_text(step_x * 8, step_y * 4, text=winner, font=("Arial", 40), justify=CENTER)
                list_ids.append(id3)
            if computer_vs_human:
                mark_igrok(hod_igrovomu_polu_1)
                hod_computer()
    mark_igrok(hod_igrovomu_polu_1)
canvas.bind_all("<Button-1>", add_to_all)  # ЛКМ
canvas.bind_all("<Button-3>", add_to_all)  # ПКМ


def generate_ship_list():
    global ships_list
    ships_list = []
    # генерируем список случайных длин кораблей
    for i in range(0, ships):
        ships_list.append(random.choice([ship_len1, ship_len2, ship_len3]))
    # print(ships_list)


def generate_enemy_ships():
    global ships_list
    # подсчет суммарной длины кораблей
    sum_1_all_ships = sum(ships_list)
    sum_1_enemy = 0

    while sum_1_enemy != sum_1_all_ships:
        # обнуляем массив кораблей врага
        enemy_ships = [[0 for i in range(s_x + 1)] for i in
                       range(s_y + 1)]  # +1 для доп. линии справа и снизу, для успешных проверок генерации противника

        for i in range(0, ships):
            len = ships_list[i]
            horizont_vertikal = random.randrange(1, 3)  # 1- горизонтальное 2 - вертикальное

            primerno_x = random.randrange(0, s_x)
            if primerno_x + len > s_x:
                primerno_x = primerno_x - len

            primerno_y = random.randrange(0, s_y)
            if primerno_y + len > s_y:
                primerno_y = primerno_y - len

            # print(horizont_vertikal, primerno_x,primerno_y)
            if horizont_vertikal == 1:
                if primerno_x + len <= s_x:
                    for j in range(0, len):
                        try:
                            check_near_ships = 0
                            check_near_ships = enemy_ships[primerno_y][primerno_x - 1] + \
                                               enemy_ships[primerno_y][primerno_x + j] + \
                                               enemy_ships[primerno_y][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y + 1][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y - 1][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y + 1][primerno_x + j] + \
                                               enemy_ships[primerno_y - 1][primerno_x + j]
                            # print(check_near_ships)
                            if check_near_ships == 0:  # записываем в том случае, если нет ничего рядом
                                enemy_ships[primerno_y][primerno_x + j] = i + 1  # записываем номер корабля
                        except Exception:
                            pass
            if horizont_vertikal == 2:
                if primerno_y + len <= s_y:
                    for j in range(0, len):
                        try:
                            check_near_ships = 0
                            check_near_ships = enemy_ships[primerno_y - 1][primerno_x] + \
                                               enemy_ships[primerno_y + j][primerno_x] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x + 1] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x - 1] + \
                                               enemy_ships[primerno_y + j][primerno_x + 1] + \
                                               enemy_ships[primerno_y + j][primerno_x - 1]
                            # print(check_near_ships)
                            if check_near_ships == 0:  # записываем в том случае, если нет ничего рядом
                                enemy_ships[primerno_y + j][primerno_x] = i + 1  # записываем номер корабля
                        except Exception:
                            pass

        # делаем подсчет 1ц
        sum_1_enemy = 0
        for i in range(0, s_x):
            for j in range(0, s_y):
                if enemy_ships[j][i] > 0:
                    sum_1_enemy = sum_1_enemy + 1

        # print(sum_1_enemy)
        # print(ships_list)
        # print(enemy_ships)
    return enemy_ships

generate_ship_list()
#print(ships_list)

enemy_ships1 = generate_enemy_ships()
enemy_ships2 = generate_enemy_ships()
# print("****************************")
# print(enemy_ships1)
# print("****************************")
# print(enemy_ships2)
# print("****************************")

generate_enemy_ships()

while app_running:
    if app_running:
        tk.update_idletasks()
        tk.update()
    time.sleep(0.05)
