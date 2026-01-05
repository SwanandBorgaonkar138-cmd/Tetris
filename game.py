from grid import Grid
from blocks import *
import random
from colors import colors

class Game:
    def __init__(self):
       self.grid = Grid() 
       self.blocks = [IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
       self.current_block = self.get_random_block()
       self.next_block = self.get_random_block()
       self.game_over = False

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]

        block = random.choice(self.blocks)
        self.blocks.remove(block)

         # ✅ RESET SPAWN POSITION
        block.row_offset = -2    # spawn above grid
        block.column_offset = 3  # center
        block.rotation_state = 0

        return block

    
    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_fits():
            self.current_block.move(0,1)

    def move_right(self):
        self.current_block.move(0,1)
        if not self.block_fits():
            self.current_block.move(0,-1)


    def move_down(self):
        self.current_block.move(1,0)
        if not self.block_fits():
            self.current_block.move(-1,0)
            self.lock_block()

    def lock_block(self):
        tiles = self.current_block.get_cell_positions()

        for tile in tiles:
            self.grid.grid[tile.row][tile.column] = self.current_block.id

        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        self.grid.clear_full_rows()

        if not self.block_fits():
            self.game_over = True


    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False 

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()

        for tile in tiles:
        # wall collision
            if tile.column < 0 or tile.column >= self.grid.num_cols:
               return False

        # floor collision
            if tile.row >= self.grid.num_rows:
               return False

        # grid collision (ONLY if inside visible grid)
            if tile.row >= 0 and not self.grid.is_empty(tile.row, tile.column):
               return False

        return True


    
    def rotate(self):
        self.current_block.rotate()
        if not self.block_fits():       
            self.current_block.undo_rotate()
  
    


    
    
    
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)
