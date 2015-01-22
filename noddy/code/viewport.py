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
        self.font = pygame.font.SysFont(None, 18)
        self.small_font = pygame.font.SysFont(None, 12)

        pxFontHeight = self.font.size(LARGETEXT)[1]
        pxSmallFontHeight = self.small_font.size(LARGETEXT)[1]
        
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.viewport = self.screen.subsurface([0,pxFontHeight,
                                                WINDOW_SIZE[0],
                                                WINDOW_SIZE[1]-(2 * pxSmallFontHeight)])

        self.player_pos = (MAPSIZE[0]/2,MAPSIZE[1]/2)

        self.update()
        self.run()

    def update(self):
        pygame.draw.rect(self.screen, BLACK, [0,0,WINDOW_SIZE[0],WINDOW_SIZE[1]], 0)
        game_title = self.font.render("@tariqk's stupid noddy roguelike exercise",
                                      True, WHITE, BLACK)
        coordinates = self.small_font.render("Noddy's location: (%d, %d)" %
                                             (self.player_pos[0],self.player_pos[1]),
                                             True, WHITE, BLACK)
        self.screen.blit(game_title, (WINDOW_SIZE[0]-game_title.get_size()[0],0))
        self.screen.blit(coordinates, (WINDOW_SIZE[0]-coordinates.get_size()[0],
                                        WINDOW_SIZE[1]-coordinates.get_size()[1]))
        self.display_level(self.viewport)
        self.display_player(self.viewport)

        pygame.display.flip()
    
    def display_level(self, surface):
        x, y = 0, 0
        for row in self.current_level.map:
            for cell in row:
                if cell == 0:
                    surface.blit(self.bg, (x*TILESIZE, y*TILESIZE))
                    y += 1
            y = 0
            x += 1

    def display_player(self, surface):
        surface.blit(self.player, (self.player_pos[0]*TILESIZE,self.player_pos[1]*TILESIZE))

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
