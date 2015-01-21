#! /usr/bin/env python

import os, sys, pygame
from pygame.locals import *

from constants import *
from game import Level

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
    def move_player(self,dx=0,dy=0):
        x, y = self.player_pos
        x += dx        
        y += dy
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
                    if event.key == K_LEFT: self.move_player(dx=-1)
                    if event.key == K_RIGHT: self.move_player(dx=1)
                    if event.key == K_UP: self.move_player(dy=-1)
                    if event.key == K_DOWN: self.move_player(dy=1)
