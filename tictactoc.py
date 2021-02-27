from time import sleep
import os
from keyboard import read_key
from random import randrange


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def waitForKeyPress():
    while True:
        return(read_key())


def showHeader():
    cls()
    print("\n\t TicTacToc")
    print("\t-----------")


def showFooter():
    print("\nPress any Key to continue...")
    sleep(.2)
    waitForKeyPress()
    cls()


def pvcPlaceholder():
    showHeader()
    print("\nFunction not implemented yet.")
    print("Find an Human Beeing 2 play with!")
    print("You loneley Fuck <3")
    showFooter()


def showInfo():
    showHeader()
    print("\nExample Game made by the 1 and only")
    print("\n   69BootyWizard420BlazeIt")
    print("  -------------------------\n")
    print("While playing, press the Numbers on the")
    print("Numbpad to fill the associated Fields.")
    print("Press Q to return to Menue.")
    showFooter()


def showField(field):
    print(f"\t {field[0][0]} | {field[0][1]} | {field[0][2]}")
    print("\t-----------")
    print(f"\t {field[1][0]} | {field[1][1]} | {field[1][2]}")
    print("\t-----------")
    print(f"\t {field[2][0]} | {field[2][1]} | {field[2][2]}")


def showWin(player, field):
    showHeader()
    print(f"\t   {player} won!\n")
    showField(field)
    print(f"\n\tGet rekt {'X' if player == 'O' else 'O'} :D\n")
    sleep(1)
    showFooter()


def showEven(field):
    showHeader()
    print(f"\t   bruh\n")
    showField(field)
    sleep(1)
    showFooter()


def checkMove(field, y, x, currentPlayer):
    if field[y][x] == ' ':
        field[y][x] = currentPlayer
        return 'O' if currentPlayer == 'X' else 'X'
    return currentPlayer


def checkWin(field, currentPlayer):
    if (field[0][0] != ' ' and field[0][0] == field[0][1] and field[0][0] == field[0][2]) or (field[1][0] != ' ' and field[1][0] == field[1][1] and field[1][0] == field[1][2]) or (field[2][0] != ' ' and field[2][0] == field[2][1] and field[2][0] == field[2][2]) or (field[0][0] != ' ' and field[0][0] == field[1][0] and field[0][0] == field[2][0]) or (field[0][1] != ' ' and field[0][1] == field[1][1] and field[0][1] == field[2][1]) or (field[0][2] != ' ' and field[0][2] == field[1][2] and field[0][2] == field[2][2]) or (field[0][0] != ' ' and field[0][0] == field[1][1] and field[0][0] == field[2][2]) or (field[0][2] != ' ' and field[0][2] == field[1][1] and field[0][2] == field[2][0]):
        showWin(currentPlayer, field)
        return True
    return False


def checkEven(field):
    fieldsLeft = 0
    for i in field:
        for j in i:
            if j == ' ':
                fieldsLeft += 1
    if fieldsLeft == 0:
        showEven(field)
        return True
    return False


def playerVsPlayer():
    field = [[' ' for i in range(3)] for j in range(3)]
    currentPlayer = 'X' if randrange(2) == 0 else 'O'

    while True:
        showHeader()
        print(f"\t {currentPlayer}'s Turn\n")
        showField(field)
        sleep(.2)
        choice = waitForKeyPress()

        if choice == '1':
            currentPlayer = checkMove(field, 2, 0, currentPlayer)
        elif choice == '2':
            currentPlayer = checkMove(field, 2, 1, currentPlayer)
        elif choice == '3':
            currentPlayer = checkMove(field, 2, 2, currentPlayer)
        elif choice == '4':
            currentPlayer = checkMove(field, 1, 0, currentPlayer)
        elif choice == '5':
            currentPlayer = checkMove(field, 1, 1, currentPlayer)
        elif choice == '6':
            currentPlayer = checkMove(field, 1, 2, currentPlayer)
        elif choice == '7':
            currentPlayer = checkMove(field, 0, 0, currentPlayer)
        elif choice == '8':
            currentPlayer = checkMove(field, 0, 1, currentPlayer)
        elif choice == '9':
            currentPlayer = checkMove(field, 0, 2, currentPlayer)
        elif choice == 'q':
            break

        if checkWin(field, currentPlayer):
            break
        if checkEven(field):
            break


def showMenue():
    while True:
        cls()
        showHeader()
        print("\nPlease press a number to continue:")
        print("1: Player vs Player")
        print("2: Player vs Computer")
        print("3: Info")
        print("4: Exit Game")

        sleep(.2)
        choice = waitForKeyPress()

        if choice == '1':
            playerVsPlayer()
        elif choice == '2':
            pvcPlaceholder()
        elif choice == '3':
            showInfo()
        elif choice == '4':
            break


showMenue()
