# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Models.Position import Position
from Models.ResultName import ResultName
from Models.MoveResult import MoveResult
from Models.Cell import Cell

currentDogPosition = Position(0, 0)
currentDogStep = 0
resultWall = MoveResult(name=ResultName.WALL, text='You are in the wall. Game over!')
resultBack = MoveResult(name=ResultName.BACK, text='You already was there. Game over!')
resultNonOptimal = MoveResult(name=ResultName.NONOPTIMAL, text='Non optimal move. Game over!')
resultSuccess = MoveResult(name=ResultName.SUCCESS, text='Good job! Please continue!')
resultFinish = MoveResult(name=ResultName.FINISH, text='Finish! Congratulations you win!')

def checkMove():
    global currentDogPosition
    global currentDogStep

    if symbol == 'u':
        print(f'{correctStepsArray[currentDogStep].moveUp.text}')
        if correctStepsArray[currentDogStep].moveUp == resultSuccess or \
                correctStepsArray[currentDogStep].moveUp == resultFinish:
            currentDogPosition.y -= 1
            currentDogStep += 1
        else:
            currentDogPosition = Position(0, 0)
            currentDogStep = 0

    elif symbol == 'r':
        print(f'{correctStepsArray[currentDogStep].moveRight.text}')
        if correctStepsArray[currentDogStep].moveRight == resultSuccess or \
                correctStepsArray[currentDogStep].moveRight == resultFinish:
            currentDogPosition.x += 1
            currentDogStep += 1
        else:
            currentDogPosition = Position(0, 0)
            currentDogStep = 0

    elif symbol == 'd':
        print(f'{correctStepsArray[currentDogStep].moveDown.text}')
        if correctStepsArray[currentDogStep].moveDown == resultSuccess or \
                correctStepsArray[currentDogStep].moveDown == resultFinish:
            currentDogPosition.y += 1
            currentDogStep += 1
        else:
            currentDogPosition = Position(0, 0)
            currentDogStep = 0

    elif symbol == 'l':
        print(f'{correctStepsArray[currentDogStep].moveLeft.text}')
        if correctStepsArray[currentDogStep].moveLeft == resultSuccess or \
                correctStepsArray[currentDogStep].moveLeft == resultFinish:
            currentDogPosition.x -= 1
            currentDogStep += 1
        else:
            currentDogPosition = Position(0, 0)
            currentDogStep = 0
    else:
        print('Wrong symbol. Try one more time')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    correctStepsArray = Cell.createCorrectStepsArray(resultWall, resultBack, resultNonOptimal, resultSuccess, resultFinish)

    while currentDogStep != len(correctStepsArray):
        print(f'Current dog position: x={currentDogPosition.x} y={currentDogPosition.y}')
        print('Where do you want to move next?')
        print('Press \'u\' if you want to go up')
        print('Press \'d\' if you want to go down')
        print('Press \'l\' if you want to go left')
        print('Press \'r\' if you want to go right')
        symbol = input("Enter symbol:")
        print(f'You pressed: {symbol}')

        checkMove()

        print()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
