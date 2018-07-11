import pygame
from pygame.locals import *

class Basic(): #basic object of the game 

	def __init__(self, _id, attrs):

		self._id = _id
		self.attrs = attrs

		try:
			assert 'size' in self.attrs, "[!] there are no attribute size in attrs"
			assert 'pos' in self.attrs, "[!] there are no attribute pos in attrs"
			assert 'color' in self.attrs, "[!] there are no attribute color in attrs"
			assert 'speed' in self.attrs, "[!] there are no attribute speed in attrs"
		except AssertionError:
			print("[!] Fail on anttribute assignment\n\tAll set to default mode")
			#set all attributes to default 
			self.attrs = {'size':(10, 10), 'color':(0, 0, 0), 'pos':(0, 0), 'speed':5}
		finally:
			self.rect = pygame.Rect(self.attrs['pos'], self.attrs['size'])

	def draw(self, surface): #draw rect to surface 
		pygame.draw.rect(surface, self.attrs['color'], self.rect)

	def move(self, time, move_tag): #each Basic moves diferently
		pass 

	def check_collision(self, other):
		if isinstance(other, Basic): #objects can only collide with Basic type 
			return self.rect.colliderect(other.rect) #returns True if overlaps 

		else:
			raise TypeError("[!] the collision object must be type Basic or child")

	def pool_collision(self, collision_pool): #checks the collision of the object with an specific pool 
		if not isinstance(collision_pool, list):
			raise TypeError("[!] The collision container must be a list ")
		for enemy in collision_pool:
			if self.check_collision(enemy):
				return True

		return False




class Player(Basic):

	def __init__(self, _id, attrs):
		super().__init__(_id, attrs) #gets stuff from parents 


			
	def move(self, time, move_tag):
		x, y = self.rect.center

		if move_tag == 'r':
			x += time*self.attrs['speed']

		elif move_tag == 'l':
			x -= time*self.attrs['speed']

		elif move_tag == 'u':
			y -= time*self.attrs['speed']

		elif move_tag == 'd':
			y += time*self.attrs['speed']

		elif move_tag == 'ru':
			x += time*self.attrs['speed']
			y -= time*self.attrs['speed']

		elif move_tag == 'rd':
			x += time*self.attrs['speed']
			y += time*self.attrs['speed']

		elif move_tag == 'lu':
			x -= time*self.attrs['speed']
			y -= time*self.attrs['speed']

		elif move_tag == 'ld':
			x -= time*self.attrs['speed']
			y += time*self.attrs['speed']

		#y += (time**2)*10 #gravitational pull

		self.rect.center = x, y
		self.mouse_move(time)
		return x, y #returns the central position of the player 

	def mouse_move(self, time):
		x, y = self.rect.center 

		mouse_x, mouse_y = pygame.mouse.get_pos()
		x += (mouse_x - x)*time*self.attrs['speed']
		y += (mouse_y - y)*time*self.attrs['speed']
		self.rect.center = x, y


	

		

