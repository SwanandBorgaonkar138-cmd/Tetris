class Grid: #creates a class name grid
    def __init__(self):
        self.num_rows = 20  # set no. of rows to 20
        self.num_cols = 10  #set no. of cols to 10
        self.cell_size =  30 # set cell size to 30 px
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)] #creats a grid/matrix using the list in list method , having 20 rows and 10 cols 

    def print_grid(self):              # this code
        for row in range(self.num_rows):  # iterates over every cell
            for column in range(self.num_cols):  # in the grid
                print(self.grid[row][column], end = " ")  # and print outs its value
            print()
 