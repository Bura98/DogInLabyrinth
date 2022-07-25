from Models.MoveResult import MoveResult
from Models.Position import Position

class Cell(object):
    def __init__(self, position: Position, moveUp: MoveResult, moveRight: MoveResult, moveDown: MoveResult,
                 moveLeft: MoveResult):
        self.position = position
        self.moveUp = moveUp
        self.moveRight = moveRight
        self.moveDown = moveDown
        self.moveLeft = moveLeft

    def createCorrectStepsArray(resultWall: MoveResult,
                                resultBack: MoveResult,
                                resultNonOptimal: MoveResult,
                                resultSuccess: MoveResult,
                                resultFinish: MoveResult):
        return [
            Cell(position=Position(0,0), moveUp=resultWall, moveRight=resultSuccess, moveDown=resultWall,
                 moveLeft=resultBack),
            Cell(position=Position(1, 0), moveUp=resultWall, moveRight=resultWall, moveDown=resultSuccess,
                 moveLeft=resultBack),
            Cell(position=Position(1, 1), moveUp=resultBack, moveRight=resultWall, moveDown=resultWall,
                 moveLeft=resultSuccess),
            Cell(position=Position(0, 1), moveUp=resultWall, moveRight=resultBack, moveDown=resultSuccess,
                 moveLeft=resultWall),
            Cell(position=Position(0, 2), moveUp=resultBack, moveRight=resultSuccess, moveDown=resultWall,
                 moveLeft=resultWall),
            Cell(position=Position(1, 2), moveUp=resultWall, moveRight=resultSuccess, moveDown=resultNonOptimal,
                 moveLeft=resultBack),
            Cell(position=Position(2, 2), moveUp=resultWall, moveRight=resultSuccess, moveDown=resultWall,
                 moveLeft=resultBack),
            Cell(position=Position(3, 2), moveUp=resultNonOptimal, moveRight=resultSuccess, moveDown=resultWall,
                 moveLeft=resultBack),
            Cell(position=Position(4, 2), moveUp=resultNonOptimal, moveRight=resultWall, moveDown=resultSuccess,
                 moveLeft=resultBack),
            Cell(position=Position(4, 3), moveUp=resultBack, moveRight=resultWall, moveDown=resultSuccess,
                 moveLeft=resultNonOptimal),
            Cell(position=Position(4, 4), moveUp=resultBack, moveRight=resultSuccess, moveDown=resultWall,
                 moveLeft=resultWall),
            Cell(position=Position(5, 4), moveUp=resultWall, moveRight=resultSuccess, moveDown=resultNonOptimal,
                 moveLeft=resultBack),
            Cell(position=Position(6, 4), moveUp=resultWall, moveRight=resultSuccess, moveDown=resultWall,
                 moveLeft=resultBack),
            Cell(position=Position(7, 4), moveUp=resultWall, moveRight=resultSuccess, moveDown=resultWall,
                 moveLeft=resultBack),
            Cell(position=Position(8, 4), moveUp=resultWall, moveRight=resultWall, moveDown=resultSuccess,
                 moveLeft=resultBack),
            Cell(position=Position(8, 5), moveUp=resultBack, moveRight=resultWall, moveDown=resultWall,
                 moveLeft=resultSuccess),
            Cell(position=Position(7, 5), moveUp=resultWall, moveRight=resultBack, moveDown=resultSuccess,
                 moveLeft=resultWall),
            Cell(position=Position(7, 6), moveUp=resultBack, moveRight=resultNonOptimal, moveDown=resultSuccess,
                 moveLeft=resultWall),
            Cell(position=Position(7, 7), moveUp=resultBack, moveRight=resultWall, moveDown=resultWall,
                 moveLeft=resultSuccess),
            Cell(position=Position(6, 7), moveUp=resultWall, moveRight=resultBack, moveDown=resultSuccess,
                 moveLeft=resultWall),
            Cell(position=Position(6, 8), moveUp=resultBack, moveRight=resultSuccess, moveDown=resultWall,
                 moveLeft=resultNonOptimal),
            Cell(position=Position(7, 8), moveUp=resultWall, moveRight=resultWall, moveDown=resultSuccess,
                 moveLeft=resultBack),
            Cell(position=Position(7, 9), moveUp=resultBack, moveRight=resultFinish, moveDown=resultWall,
                 moveLeft=resultWall)
        ]