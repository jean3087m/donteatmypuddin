#!/usr/bin/bash/python3

import pygame 
from pygame.locals import *

import PIL
import json
import sys 
import os 

#local import
from utillib import *
from gamelib import *


def update_game(onpause=False): #encapsulates the action funtions for the game
	if not onpause:
		pygame.display.update()
		

def draw(): #draw all the elements to the screen 
	pass 


def main():

	pygame.init() #starts pygame 
	pygame.font.init() #starts fonts for pygame 

	#screen settings 
	SCREEN_SIZE = (800, 600)
	screen = pygame.display.set_mode(SCREEN_SIZE) #makes the main screen surface 
	pygame.display.set_caption("Don't eat my PUDDIN!") #text above game 

	#clock settings 
	FPS = 60
	clock = pygame.time.Clock() #pygame internal clock
	time_counter = 0 #counts total game time 


	#image settings 
	IMAGE_PATH = '' #path to load the images 
	image_pool_main = image_loader()#pool of images to be drawn onto the main surface 'screen'
	
	#game settings 


if __name__ == '__main__':
	main()
