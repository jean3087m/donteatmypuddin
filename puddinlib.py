#!/usr/bin/bash/python3 

import pygame 
from pygame.locals import *

import os 
import json 
import sys 



#############################################################
###image 

def get_image_group(folder_path, image_tag, image_format='.png'):
    """takes images from a folder and returns a list of images"""
    token = os.listdir(folder_path) #list the name of the files in the folder 
    new = [] #empty list for images 
    for name in token:
        if image_tag in name and image_format in name:
            new.append(pygame.image.load(os.path.join(folder_path, name))) 
    return new 

##############################################################
###computer stuff 

class Node():
    """Node for linked list"""
    def __init__(self, value):
        self.value = value
        self.next = None 


class LinkedList():
    """Linked list class"""
    def __init__(self, other_list):
        """takes a list and tranforms it to a linked list"""

        self.this = [Node(other_list[i]) for i in range(len(other_list))] #makes a list of nodes 
        for i in range(len(other_list) - 1):
            self.this[i].next = self.this[i + 1] #points to the next element 
        
        self.pointer = self.this[0] #points to the first element 
        
            
    def next(self):
        if self.pointer.next != None:
            self.pointer = self.pointer.next #changes the pointer to the next
        else:
            self.head()
        
    
    def head(self): #points to the begining 
        self.pointer = self.this[0]
    
################################################################################
