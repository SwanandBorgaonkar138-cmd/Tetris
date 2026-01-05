import pygame
import sys
from game import Game

pygame.init()
Dark_Blue = (44,44,125)
screen = pygame.display.set_mode((300,600)) #defines the display of the game
pygame.display.set_caption("Tetris game")

clock = pygame.time.Clock() #controls the frame rate of the game ie:how fast the game will run

game = Game()

Game_UPDATE = pygame.USEREVENT # userevent is a special event type that can be used to create custom events
pygame.time.set_timer(Game_UPDATE, 200)

while True: #crate a loop which will ein the game
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #breakes the loop when quit
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  # CHECKS if the key is pressed
            if game.game_over and event.key == pygame.K_r:
                game.reset()
            
            if event.key == pygame.K_LEFT and game.game_over == False:  #checks if the event.key constant is equal to left arrow key
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
            if event .key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == Game_UPDATE:
            if not game.game_over:
                   game.move_down()

        
    #drawing bg
    screen.fill(Dark_Blue)
    game.draw(screen)
   
    
    pygame.display.update()
    clock.tick(60)      #sets FPS to 60

