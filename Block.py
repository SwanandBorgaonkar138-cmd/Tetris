from colors import colors
import pygame

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {} # this dictionary is to store the occupied cells in the bounding grid for each rotation state of the block
        self.cell_size = 30
        self.rotation_state = 0
        self.colors = colors.get_cell_colors()
    
    def draw(self, screen):
        tiles = self.cells[self.rotation_state] # retrives the list of positions for the current rotation state of the termino
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size +1, tile.row * self.cell_size +1, self.cell_size -1, self.cell_size -1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
