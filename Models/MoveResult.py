from Models.ResultName import ResultName

class MoveResult(object):
    def __init__(self, name: ResultName, text: str):
        self.name = name
        self.text = text