#!/usr/bin/bash/python3 

import pygame 


#local import
import puddinlib

class Anime():
    """A class to animates them all!"""
    def __init__(self, anime_time=1):
        self.anime_time = anime_time
        self.time_count = 0
    
    def setup(self, folder_path, image_tag, image_format='.png'):
        #get a list of images
        self.image_list = puddinlib.get_image_group(folder_path, image_tag, image_format)
        #makes the image list to a linked list
        self.image_list = puddinlib.LinkedList(self.image_list) 

    def simple_anime(self, time, surface, pos):
        self.time_count += time #adds time 
        if self.time_count > self.anime_time:
            self.time_count = 0 #changes the count back to zero
            if self.image_list.pointer.value != None: #checks if its points to anything
                #moves the pointer to the next image 
                self.image_list.next()
            else:
                #points back to the begining of the list
                self.image_list.head()
        #draws the image to the choosen surface
        surface.blit(self.image_list.pointer.value, pos) 

    
    def resize_all(self, new_size):
        #resizes all the images in the animation list
        for image in self.image_list.this:
            pygame.transform.scale(image.value, new_size)


class AnimationHandler():
    """Handles multiple animations"""
    def __init__(self):
        #dictionary must follow { 'action name' : Anime() }
        self.anime_dict = {}
    
    def add_animation_dict(self, action, config):
        """adds an animation by a dictionary configuration"""
        self.add_animation(action, config['folder_path'], config['image_tag'], config['anime_time'], config['image_format'])

    def add_animation(self, action, folder_path, image_tag, anime_time=1, image_format=".png"):
        """adds an animation to the animation dictionary"""
        self.anime_dict[action] = Anime(anime_time) #adds a anime class to the dictionaty
        self.anime_dict[action].setup(folder_path, image_tag, image_format) #sets the animation 
    
    def anime(self, action, time, surface, pos): #animates according to the action specified 
        self.anime_dict[action].simple_anime(time, surface, pos)
    

