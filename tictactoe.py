m = [[' ', ' ', ' '],
     [' ', ' ', ' '],
     [' ', ' ', ' ']]


def print_grid():
    print("---------")
    print("| " + m[0][0] + " " + m[0][1] + " " + m[0][2] + " |")
    print("| " + m[1][0] + " " + m[1][1] + " " + m[1][2] + " |")
    print("| " + m[2][0] + " " + m[2][1] + " " + m[2][2] + " |")
    print("---------")


def check_state():
    result = ""
    counter_x, counter_o = 0, 0
    for row in m:
        for cell in row:
            if cell == 'X':
                counter_x += 1
            elif cell == 'O':
                counter_o += 1
    if abs(counter_x - counter_o) > 1:
        result = "Impossible"

    if result != "Impossible":
        counter_x, counter_o = 0, 0
        for row in m:
            if row == ['X', 'X', 'X']:
                counter_x += 1
                result = "X wins"
            if row == ['O', 'O', 'O']:
                counter_o += 1
                result = "O wins"
        if counter_x + counter_o > 1:
            result = "Impossible"

    if result != "Impossible":
        counter_x, counter_o = 0, 0
        for col in range(3):
            if m[0][col] == 'X' and m[1][col] == 'X' and m[2][col] == 'X':
                counter_x += 1
                result = "X wins"
            if m[0][col] == 'O' and m[1][col] == 'O' and m[2][col] == 'O':
                counter_o += 1
                result = "O wins"
        if counter_x + counter_o > 1:
            result = "Impossible"

    if result != "Impossible":
        if m[0][0] == 'X' and m[1][1] == 'X' and m[2][2] == 'X':
            result = "X wins"
        if m[0][0] == 'O' and m[1][1] == 'O' and m[2][2] == 'O':
            result = "O wins"
        if m[0][2] == 'X' and m[1][1] == 'X' and m[2][0] == 'X':
            result = "X wins"
        if m[0][2] == 'O' and m[1][1] == 'O' and m[2][0] == 'O':
            result = "O wins"

    if result == "":
        count_empty_cells = 0
        for row in m:
            for cell in row:
                if cell == ' ':
                    count_empty_cells += 1
        result = "Draw" if count_empty_cells == 0 else "Game not finished"

    return result


def enter_coordinates(letter):
    global m
    error = True
    coord_list = []
    while error:
        error = False
        coord_list = input("Enter the coordinates: ").split()
        if not ''.join(coord_list).isdigit():
            print("You should enter number!")
            error = True
        else:
            for coord in coord_list:
                if int(coord) > 3 or int(coord) < 1:
                    print("Coordinates should be from 1 to 3!")
                    error = True
    if m[int(coord_list[0]) - 1][int(coord_list[1]) - 1] == ' ':
        m[int(coord_list[0]) - 1][int(coord_list[1]) - 1] = letter
        return True
    else:
        print("This cell is occupied! Choose another one!")
        enter_coordinates(letter)


player = 'X'
while check_state() == "Game not finished":
    print_grid()
    if enter_coordinates(player):
        player = 'O' if player == 'X' else 'X'

print_grid()
print(check_state())

