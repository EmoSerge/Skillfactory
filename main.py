def open_field():
    print()
    print("   | x0 | x1 | x2 |")
    print("*" * 19)
    for i in range(3):
        row = f"y{i} "
        for j in range(3):
            row += f"| {field[i][j]}  "
        row += "|"
        print(row)
        print("*" * 19)

def move():
    while True:
        hod = input(' Введите координаты вашего хода через пробел, сначала строка Y, затем столбец X: ').split()

        if (len(hod) != 2):
            print("Данные введены не верно ")
            continue

        x, y = hod[0], hod[1]

        if not ((x.isdigit()) and (y.isdigit())):
            print("Введены не числа")
            continue

        x, y = int(x), int(y)

        if (x not in {0, 1, 2}) or (y not in {0, 1, 2}):
            print("Введены координаты вне диапазона")
            continue

        if field[x][y] != " ":
            print("Клетка занята, ход не возможен ")
            continue

        return x, y

def victory():
    for line in winline:
        sum = []
        for s in line:
            if field[s[0]][s[1]] == " ":
                continue
            sum.append(field[s[0]][s[1]])

        if (sum == ["X", "X", "X"]) or (sum == [0, 0, 0]):
            return True
    return False


field = [[" "] * 3 for q in range(3)]
kon = 0
winline = [[[0, 0], [0, 1], [0, 2]],
           [[1, 0], [1, 1], [1, 2]],
           [[2, 0], [2, 1], [2, 2]],
           [[0, 0], [1, 0], [2, 0]],
           [[0, 1], [1, 1], [2, 1]],
           [[0, 2], [1, 2], [2, 2]],
           [[0, 0], [1, 1], [2, 2]],
           [[2, 0], [1, 1], [0, 2]]]
print("Игра Крестики-нолики")
print()

while True:
    open_field()
    if kon % 2 == 0:
        print()
        print("Ход - X")
        x, y = move()
        field[x][y] = "X"
        if victory():
            open_field()
            print("=====Победа Х=====")
            break
    else:
        print()
        print("Ход - 0")
        x, y = move()
        field[x][y] = 0
        if victory():
            open_field()
            print("=====Победа 0=====")
            break

    kon += 1

    if kon == 9:
        open_field()
        print("Ничья")
        break
