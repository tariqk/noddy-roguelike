#!/usr/bin/env python

import pygame, math, sys, os
from pygame.locals import *

# CONSTANTS

# colors

BLACK = (0,0,0)
WHITE = (255, 255, 255)

# sizes

TILESIZE = 16 # ASSUMPTION: icons are square
WINDOW_SIZE = (800,608) # placeholder
MAPSIZE = (WINDOW_SIZE[0]/TILESIZE,WINDOW_SIZE[1]/TILESIZE)

# resource locations

RES_DIR = os.getcwd() + '/noddy/res/'

# CLASSES

class Level(object):
    """
    Represents the current level.
    """
    def __init__(self):
        self.new_map()

    def new_map(self, isEmpty=True):
        """
        Generate new map -- currently only creates an empty map.

        Right now it assumes that map = fog of war. 

        TODO: separate map geometry and fog of war. By rights, fog of
              war tells the game what to display; but the map remains
              the map.
        """
        self.map = [] # right now it's empty; later we'll load or generate our own
        for spam in range(MAPSIZE[0]): # fill everything with zeroes.
            row = []
            for eggs in range (MAPSIZE[1]):
                row.append(0)
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

        self.player = pygame.image.load(os.path.join(RES_DIR, "img", "avg-humanoid.png"))
        self.bg = pygame.image.load(os.path.join(RES_DIR, "img", "floor-dot.png"))
        
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode(WINDOW_SIZE)

        self.player_pos = (MAPSIZE[0]/2,MAPSIZE[1]/2)

        print self.player_pos

        self.update()
        self.run()

    def update(self):
        self.display_level()
        self.display_player()
        pygame.display.flip()
    
    def display_level(self):
        x, y = 0, 0
        for row in self.current_level.map:
            for cell in row:
                if cell == 0:
                    self.display.blit(self.bg, (x*TILESIZE, y*TILESIZE))
                    y += 1
            y = 0
            x += 1

    def display_player(self):
        self.display.blit(self.player, (self.player_pos[0]*TILESIZE,self.player_pos[1]*TILESIZE))
    def move_player(self,delta=(0,0)):
        x, y = self.player_pos
        x += delta[0]        
        y += delta[1]
        if x > MAPSIZE[0]-1 or x < 0 or y > MAPSIZE[1]-1 or y < 0:
            return
        self.player_pos = x, y
        self.update()

    def run(self):
        """
        Right now, just running things and listens to key presses for the exit key.
        """
        while 1:
            self.clock.tick(30)
            for event in pygame.event.get(): # potential improvement -- use dict?
                if not hasattr(event, 'key'): continue
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE: sys.exit()
                    if event.key == K_LEFT: self.move_player((-1,0))
                    if event.key == K_RIGHT: self.move_player((1,0))
                    if event.key == K_UP: self.move_player((0,-1))
                    if event.key == K_DOWN: self.move_player((0,1))

# UTILITY FUNCTIONS

def main():
    """ 
    main loop 
    """
    game = Game()

# THE RUNNING PROGRAM
        
if __name__ == "__main__":
    main()
