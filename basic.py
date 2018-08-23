#!/usr/bin/bash/python3 


import pygame 


import sys

class Basic():
    """Basic biulding blocks"""
    def __init__(self, _id, attrs):
        self.setup(_id, attrs)

    def setup(self, _id, attrs): #sets the game object 
        
        self._id = _id 
        self.attrs = attrs
        #the given attributes must be a dictionary were the arguments have the specifications 
        #in case of the basic arguments are not found it throws an assert error 
        assert  self.attrs['color'] , "[!] attrs argument must have a 'color' "
        assert  self.attrs['size'] , "[!] attrs argument must have a 'size' "
        assert  self.attrs['pos'] , "[!] attrs argument must have a 'pos' "
        assert  self.attrs['speed'] , "[!] attrs argument must have a 'speed' "
        
        #this makes the game be played in 'Tofu Mode'

        self.rect = pygame.Rect(self.attrs['pos'], self.attrs['size']) #makes an rectangle 

    
    def collide(self, other): #checks if game objects collide
        #the other is a Base class or child 
        if self.rect.colliderect(other.rect): #checks if the base collide with another 
            return True
        return False

    def blit(self, time, surface):
        pass 

    def move(self, time, surface):
        pass