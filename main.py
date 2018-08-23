#!/usr/bin/bash/python3 

import pygame 
from pygame.locals import *

import sys

#local imports 
import puddinlib
import anime

def main():
    
    pygame.init() #starts pygame 
    pygame.font.init() #starts font module 

    #screen setup
    SCREEN_SIZE = (800, 600)
    screen = pygame.display.set_mode(SCREEN_SIZE) #makes a main screen

    #clock setup
    FPS = 60
    clock = pygame.time.Clock() #game's time 

    #anime test
    new_anime = anime.Anime(2)
    new_anime.setup("images", "temer_shoot")
    new_anime.resize_all((200, 200))

    other_anime = anime.Anime(1.5)
    other_anime.setup("images", "temer_hurt")
    other_anime.resize_all((100, 100))



    #game settings 
    game_over = False #game over checker 
    while not game_over:
        time = clock.tick() / 100 #gets time in seconds (s)

        for event in pygame.event.get():
            if event.type == QUIT: #quits the game 
                pygame.quit()
                sys.exit()
        
        screen.fill((50, 200, 100)) #fills screen with color 
        new_anime.simple_anime(time, screen, (300, 300))
        
        pygame.display.update() #updates screen

if __name__ == "__main__":
    main() 