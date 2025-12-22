import pygame
import sys

pygame.init()

pygame = pygame.display.set_mode((300,600)) #defines the display of the game
pygame.display.set_caption("Tetris game")

clock = pygame.time.Clock() #controls the frame rate of the game ie:how fast the game will run

while True: #crate a loop which will ein the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #breakes the loop when closed
            pygame.quit()
            sys.exit()
