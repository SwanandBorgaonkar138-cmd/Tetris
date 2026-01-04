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