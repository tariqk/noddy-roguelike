#!/usr/bin/env python

import pygame, math, sys, os
from pygame.locals import *

# CONSTANTS

# colors

BLACK = (0,0,0)
WHITE = (255, 255, 255)

# sizes

MAPSIZE = (20,15) # placeholder; decision to be made -- dynamic map sizes or fixed?
TILESIZE = 16 # ASSUMPTION: icons are square
WINDOW_SIZE = (320,240) # placeholder

# resource locations

RES_DIR = os.getcwd() + '/noddy/res/'

# CLASSES

class Level(object):
    """
    Represents the current level.
    """
    def __init__(self):
        self.map = [] # right now it's empty; later we'll load or generate our own
        for spam in range(MAPSIZE[0]): # fill everything with zeroes.
            row = []
            for eggs in range (MAPSIZE[1]):
                row.append(0) # assumption: 0 is empty floor?
            self.map.append(row)

    def print_ascii_map(self):
        for row in self.map:
            print row

class Game(object):
    """
    Represents the current game display, right now.
    """
    def __init__(self):
        self.current_level = Level()

        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode(WINDOW_SIZE)
        
        self.run()

    def run(self):
        """
        Right now, just running things and listens to key presses for the exit key.
        """
        while 1:
            self.clock.tick(30)
            for event in pygame.event.get(): # potential improvement -- use dict?
                if not hasattr(event, 'key'): continue
                if event.key == K_ESCAPE: pygame.quit()

# UTILITY FUNCTIONS

def main():
    """ 
    main loop 
    """
    game = Game()

# THE RUNNING PROGRAM
        
if __name__ == "__main__":
    main()
