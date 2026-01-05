from Block import Block
from position import position

class LBlock(Block):
    def __init__(self):
       super().__init__(1)
       self.id = 1
       self.cells = {
           0:[position(0,2), position(1,0), position(1,1), position(1,2)],
           1:[position(0,1), position(2,1), position(1,1), position(2,2)],
           2:[position(2,0), position(1,0), position(1,1), position(1,2)],
           3:[position(0,0), position(0,1), position(1,1), position(2,1)],
       }
       self.move(0,3)

class IBlock(Block):
    def __init__(self):
        super().__init__(2)
        self.id = 2
        self.cells = {
            0:[position(1,0), position(1,3), position(1,1), position(1,2)],
            1:[position(0,2), position(1,2), position(3,2), position(2,2)],
            2:[position(2,0), position(2,1), position(2,2), position(2,3)],
            3:[position(3,1), position(0,1), position(1,1), position(2,1)],
        }
        self.move(-1,3)

class OBlock(Block):
    def __init__(self):
        super().__init__(3)
        self.id = 3
        self.cells = {
            0:[position(0,0), position(0,1), position(1,1), position(1,0)],
            1:[position(0,0), position(0,1), position(1,1), position(1,0)],
            2:[position(0,0), position(0,1), position(1,1), position(1,0)],
            3:[position(0,0), position(0,1), position(1,1), position(1,0)]
        }
        self.move(0,4)

class SBlock(Block):
    def __init__(self):
        super().__init__(4)
        self.id = 4
        self.cells = {
            0:[position(0,2), position(0,1), position(1,1), position(1,0)],
            1:[position(2,2), position(0,1), position(1,1), position(1,2)],
            2:[position(2,0), position(2,1), position(1,1), position(1,2)],
            3:[position(0,0), position(2,1), position(1,1), position(1,0)]
        }
        self.move(0,3)

class TBlock(Block):
    def __init__(self):
        super().__init__(5)
        self.id = 5
        self.cells = {
            0:[position(1,2), position(0,1), position(1,1), position(1,0)],
            1:[position(2,1), position(0,1), position(1,1), position(1,2)],
            2:[position(1,2), position(2,1), position(1,1), position(1,0)],
            3:[position(2,1), position(0,1), position(1,1), position(1,0)]
        }
        self.move(0,3)

class ZBlock(Block):
    def __init__(self):
        super().__init__(6)
        self.id = 6
        self.cells = {
            0:[position(0,0), position(0,1), position(1,1), position(1,2)],
            1:[position(0,2), position(2,1), position(1,1), position(1,2)],
            2:[position(2,2), position(2,1), position(1,1), position(1,0)],
            3:[position(2,0), position(0,1), position(1,1), position(1,0)]
        }
        self.move(0,3)

class JBlock(Block):
    def __init__(self):
        super().__init__(7)
        self.id = 7
        self.cells = {
            0:[position(0,0), position(0,1), position(1,1), position(1,0)],
            1:[position(0,2), position(0,1), position(1,1), position(2,1)],
            2:[position(2,2), position(1,2), position(1,1), position(1,0)],
            3:[position(2,1), position(0,1), position(1,1), position(2,0)]
        }
        self.move(0,3)
