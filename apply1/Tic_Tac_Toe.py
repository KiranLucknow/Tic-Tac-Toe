import os

import support

global choice

global game
game = True
turn = 0

global position
position = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

support.show_board(position)
# Choice = input("Welcome to Tic-Tac-Toe game, please choose your letter,(x,o)")


while game:
    choice = support.mark(turn)
    xspot = input("choose x coordinates of board where you want to enter")
    yspot = input("choose y coordinates of board where you want to enter")
    print(xspot, yspot)
    nextPosition = int(support.placement(xspot, yspot))
    print(position[nextPosition])
    if (position[nextPosition] != 'o') and (position[nextPosition] != 'x'):
        position[nextPosition] = choice
        print(position[nextPosition])
        os.system("cls")
        support.show_board(position)
        win = support.check(position, choice)
        if win:
            anotherGame = input("Would you like to go for another round or just end this game?(y for yes)")
            if anotherGame != 'y':
                game = False
        if turn >= 8:
            print("No one won in this round")
            break
        else:
            turn += 1
    else:
        print(f'Unfortunately, the {xspot,yspot} move you have entered is already used, please enter a new move?')



'''
play = True
global place
turn = 0
place = 0

while play:
    os.system('cls' if os.name == 'nt' else 'clear')
    while place not in position:
        coordinates = input("Enter the coordinates for your place ex:2,1")
        place = support.placement(coordinates)
    print(place)

    sign = support.mark(turn)
    turn += 1
    position[place] = sign

'''
