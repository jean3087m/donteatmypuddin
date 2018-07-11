#this is the main.py 
#the main game script 


import pygame 
from pygame.locals import *

import sys 

#local imports
from util import *

class Game():

	def __init__(self):
	 	self.setup()

	def setup(self):
		
		pygame.init()
		pygame.font.init()

		#screen settings 
		SCREEN_SIZE = (800, 600)
		self.screen  = pygame.display.set_mode(SCREEN_SIZE)
		pygame.display.set_caption("Don't eat my puddin")

		#clock settings 
		self.FPS = 60
		self.clock = pygame.time.Clock()
		self.time_counter = 0

		#game settings 
		self.game_over = False

		#player settings 
		PLAYER_ATTRS = {'size':(50, 50), 'color':(30, 100, 200), 'pos':(120, 400), 'speed':5, }
		self.player = Player(0, PLAYER_ATTRS)
		self.player_move_tag = 'i' #default move tag 'idle'



	def event_handler(self): #manages events in pygame 
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit(0)

	def sound_handler(self): #manages sounds
		pass 

	def draw_handler(self): #manages the drawing 
		self.screen.fill(pygame.color.Color('green')) 

		self.player.draw(self.screen)

		pygame.display.update()


	def main(self):


		while not self.game_over:

			time = self. clock.tick(self.FPS) / 100 #time in seconds 
			self.time_counter += time #counts the total time 

			self.player.move(time, self.player_move_tag)

			self.event_handler()

			self.sound_handler()

			self.draw_handler()



if __name__ == '__main__':
	game = Game()
	game.main()