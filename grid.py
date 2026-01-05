import pygame
from colors import colors

class Grid: #creates a class name grid
    def __init__(self):
        self.num_rows = 20  # set no. of rows to 20
        self.num_cols = 10  #set no. of cols to 10
        self.cell_size =  30 # set cell size to 30 px
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)] #creats a grid/matrix using the list in list method , having 20 rows and 10 cols 
        self.colors = colors.get_cell_colors()
    def print_grid(self):              # this code
        for row in range(self.num_rows):  # iterates over every cell
            for column in range(self.num_cols):  # in the grid
                print(self.grid[row][column], end = " ")  # and print outs its value
            print()

    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False
    
    def is_empty(self,row, column):
        if self.grid[row][column] == 0:
            return True
        return False
    
    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True
    
    def clear_row(self, row):
        for column in range(self.num_cols):
          self.grid[row][column] ==  0

    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed
    
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0
        
    def draw(self, screen):
        for row in range(self.num_rows):#                                                                                       |      
           for column in range (self.num_cols):#                                                                                |          
               cell_value = self.grid[row][column]#                                                                             | creates a mesh
               cell_rect = pygame.Rect(column*self.cell_size +1 , row*self.cell_size +1, self.cell_size -1, self.cell_size -1)# |
               pygame.draw.rect(screen, self.colors[cell_value], cell_rect)#                                                    |
    
