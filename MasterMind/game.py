import random

class pin:
    RED = 0
    GREEN = 1
    BLUE = 2
    YELLOW = 3
    BLACK = 4
    WHITE = 5

class board:
    def __init__(self, code=None):
        self.pins = [
            pin.RED,
            pin.GREEN,
            pin.BLUE,
            pin.YELLOW,
            pin.BLACK,
            pin.WHITE
        ]
        self.board = [['X'*4]*10]
        if code:
            self.code = code
        else:
            self.code = random.choices(self.pins, k=4)

    def guess(self, guess):
        cc = self.code.copy()
        gc = guess.copy()
        w = 0; b = 0
        for i in range(4):
            if gc[i] == cc[i]:
                b += 1
                cc[i] = -1
                gc[i] = -1
        for v in gc:
            if v in cc:
                w += 1
                cc.remove[v]
