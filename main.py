#!/usr/bin/env python

import pygame, math, sys
from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255, 255, 255)
MAPSIZE = (20,15)

class Level(object):
    """
    Represents the current level.
    """
    def __init__(self):
        self.map = [] # right now it's empty; later we'll load or generate our own
        for spam in range(MAPSIZE[0]):
            row = []
            for eggs in range (MAPSIZE[1]):
                row.append(0) # assumption: 0 is empty floor?
            self.map.append(row)

    def print_ascii_map(self):
        for row in self.map:
            print row

class Game(object):
    def __init__(self):
        self.current_level = Level()
        self.current_level.print_ascii_map()

def main():
        game = Game()

if __name__ == "__main__":
    main()
