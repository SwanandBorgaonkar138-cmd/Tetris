import pygame
import sys
from grid import Grid

pygame.init()
Dark_Blue = (44,44,125)
screen = pygame.display.set_mode((300,600)) #defines the display of the game
pygame.display.set_caption("Tetris game")

clock = pygame.time.Clock() #controls the frame rate of the game ie:how fast the game will run

game_grid = Grid()
game_grid.print_grid()

while True: #crate a loop which will ein the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #breakes the loop when quit
            pygame.quit()
            sys.exit()
    #derawing bg
    screen.fill(Dark_Blue)
    pygame.display.update()
    clock.tick(60)      #sets FPS to 60
