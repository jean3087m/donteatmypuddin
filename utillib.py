#!/usr/bin/bash/python3

import pygame 
from pygame.locals import *

import PIL
import json
import sys 
import os 

def image_apply_filter(image, filter_type=None): #apply filter to images 
	pass 

def image_loader(path=''):
	#loads the image and returns a image dictionarie 
	#way to name image: firstaname_action_imagepos.png
	#example: enemyx_move_3.png
	#returns: {'firstname': {'action': [imagepos1, imagepos2, ..]}, ..}
	get = {}
	namelist = []
	for image in os.listdir(path): #image is he nme of the image 
		token = image.split('_')[:-4] #gets takes out the '.png' stuff and split 
		#token[0]:firstaname #token[1]:action #token[2]: position
		namelist.append(token) #append to the namelist

	get = {namelist[i][0]:{namelist[j][1]:[] for j in range(len(namelist))} for i in range(len(namelist))} #makes a dictionary with an empty list
	for image in sorted(os.listdir(path)):
		token = image.split('_')[:-4] #splits again
		get[token[0]][token[1]].append(pygame.image.load(os.path.join(image))) #appends the image to a list in a dictionary

	return get returns the list of images loaded 

		