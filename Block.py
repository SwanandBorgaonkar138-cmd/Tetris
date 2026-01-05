import pygame
from colors import colors
from position import position


class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}              # rotation_state -> list[Position]
        self.cell_size = 30
        self.row_offset = -2
        self.column_offset = 3
        self.rotation_state = 0
        self.colors = colors.get_cell_colors()

    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []

        for tile in tiles:
            moved_tiles.append(
                position(
                    tile.row + self.row_offset,
                    tile.column + self.column_offset
                )
            )

        return moved_tiles

    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):  # resets the rotation state to 0 after every complete rotation
            self.rotation_state = 0

    def undo_rotate(self):
        self.rotation_state -= 1
        if self.rotation_state < 0:
            self.rotation_state = len(self.cells) -1

    def draw(self, screen):
        tiles = self.get_cell_positions()  

        for tile in tiles:
            tile_rect = pygame.Rect(
                tile.column * self.cell_size + 1,
                tile.row * self.cell_size + 1,
                self.cell_size - 1,
                self.cell_size - 1
            )
            pygame.draw.rect(
                screen,
                self.colors[self.id],
                tile_rect
            )
