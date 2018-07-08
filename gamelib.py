#!/usr/bin/bash/python3 
import pygame 





class GameObject():
	""""this is the basic game object class for all things in the game"""

	def __init__(self, _id, attrs):
		self.attrs = attrs 
		self._id = _id

		assert 'speed' in self.attrs, "[!] speed attribute not in self.attrs" #px per time passed 
		assert 'size' in self.attrs, "[!] size attribute not in self.attrs" #rectangle size
		assert 'pos' in self.attrs, "[!] pos attribute not in self.attrs" #initial position attribute 
		assert 'color' in self.attrs, "[!] color attribute not in attrs" #works in case of no image

		self.rect = pygame.Rect(self.attrs['pos'], self.attrs['size'])
		self.images = self.attrs['images']



	def move(self, time):
		pass 

	def blit(self, surface, image=None, filter=False):
		if image:
			surface.blit(image, self.rect.center)
		else:
			pygame.draw.rect(surface, self.attrs['color'], self.rect)
		



class Player(GameObject):

	"""this is the game class"""
	def __init__(self, _id, attrs):
		super().__init__(_id, attrs)

		assert self._id == 0, "[!] Player id must be 0"

	def move(self, time, move_tag='i'):
		#move tags are:
		#'r' -> right 
		#'l' -> left
		#'u' -> up
		#'d' -> down
		#'i' -> idle
		#combinations: 'ru', 'rd', 'lu', 'ld'

		new = list(self.rect.center) #gets the center of the rectangle parameter 
		if move_tag == 'u':
			new[1] -= time*self.attrs['speed']

		elif move_tag == 'd':
			new[1] += time*self.attrs['speed']

		elif move_tag == 'r':
			new[0] += time*self.attrs['speed']

		elif move_tag == 'l':
			new[0] -= time*self.attrs['speed']

		elif move_tag == 'ru':
			new[0] += time*self.attrs['speed']
			new[1] -= time*self.attrs['speed']

		elif move_tag == 'rd':
			new[0] += time*self.attrs['speed']
			new[1] += time*self.attrs['speed']

		elif move_tag == 'lu':
			new[0] -= time*self.attrs['speed']
			new[1] -= time*self.attrs['speed']

		elif move_tag == 'ld':
			new[0] -= time*self.attrs['speed']
			new[1] += time*self.attrs['speed']


		self.rect.center = tuple(new) #updates the rectangle center 




