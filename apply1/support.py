import os


def show_board(position):
    board = (f"|{position[1]}|{position[2]}|{position[3]}|\n"
             f"|{position[4]}|{position[5]}|{position[6]}|\n"
             f"|{position[7]}|{position[8]}|{position[9]}|")
    #  print(position)
    print(board)


def placement(xCoordinates, yCoordinate):
    if xCoordinates == '0' and yCoordinate == '0':
        place = 1
    elif xCoordinates == '0' and yCoordinate == '1':
        place = 2
    elif xCoordinates == '0' and yCoordinate == '2':
        place = 3
    elif xCoordinates == '1' and yCoordinate == '0':
        place = 4
    elif xCoordinates == '1' and yCoordinate == '1':
        place = 5
    elif xCoordinates == '1' and yCoordinate == '2':
        place = 6
    elif xCoordinates == '2' and yCoordinate == '0':
        place = 7
    elif xCoordinates == '2' and yCoordinate == '1':
        place = 8
    elif xCoordinates == '2' and yCoordinate == '2':
        place = 9
    else:
        print("choose the right coordinates")
        place = 0
    return place


def mark(turn):
    if turn % 2 == 0:
        return 'x'
    else:
        return 'o'


def check(position, choice):
    # row check used slicing method of list by casting dictionary to list and again getting keys value by casting
    # list to dictionary first_three_items\
    row1 = dict(list(position.items())[:3])
    print(row1[1], row1[2], row1[3])
    # items from 4 to 6
    row2 = dict(list(position.items())[3:6])
    print(row2[4], row2[5], row2[6])
    # items from 7 till end
    row3 = dict(list(position.items())[5:])
    print(row3[7], row3[8], row3[9])
    if row1[1] == row1[2] == row1[3] or row2[4] == row2[5] == row2[6] or row3[7] == row3[8] == row3[9]:
        print(f"Player {choice} won the game row wise")
        return 1
    elif position[1] == position[4] == position[7] or position[2] == position[5] == position[8] or position[3] == \
            position[6] == position[9]:
        print(f"Player {choice} won the game by column wise")
        return 1
    elif position[1] == position[5] == position[9] or position[3] == position[5] == position[7]:
        print(f"Player {choice} won the game diagonally")
        return 1
    else:
        return 0
