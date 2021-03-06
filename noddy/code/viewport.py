#! /usr/bin/env python

import os
import sys
import pygame

from pygame.locals import *
from constants import *
from game import *
from tiles import Wall, Floor


class Game(object):
    """ Represents the current game display, right now. """
   
    def __init__(self):
        
        self.current_level = Level()
        self.player = Actor(self.current_level, (15, 15))
        
        self.font = pygame.font.SysFont(None, 18)
        self.small_font = pygame.font.SysFont(None, 12)

        pxFontHeight = self.font.size(LARGETEXT)[1]
        pxSmallFontHeight = self.small_font.size(LARGETEXT)[1]

        self.maplegend = {type(Floor()):
                          pygame.image.load(os.path.join(RES_DIR,
                                                         "img",
                                                         "floor-dot.png")),
                          type(Wall()):
                          pygame.image.load(os.path.join(RES_DIR,
                                                         "img",
                                                         "wall-hatch.png"))}

        self.actorlegend = {self.player:
                            pygame.image.load(os.path.join(RES_DIR, "img",
                                                           "avg-humanoid.png"))}

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.viewport = self.screen.subsurface([0, pxFontHeight,
                                                WINDOW_SIZE[0],
                                                WINDOW_SIZE[1]-(2 *
                                                                pxSmallFontHeight)])
        self.viewsize = tuple(x/TILESIZE for x in self.viewport.get_size())

        self.update()
        self.run()

    def fill_surface_with_color(self, Surface2Blank, color):
        pygame.draw.rect(Surface2Blank, color, Surface2Blank.get_rect())
        
    def update(self):
        self.fill_surface_with_color(self.screen, BLACK)

        title_text = "@tariqk's crappy roguelike"
        game_title = self.font.render(title_text, True, WHITE, BLACK)
        coordinates = self.small_font.render("Noddy's location: (%d, %d)" %
                                             (self.player.coordinates[0],
                                              self.player.coordinates[1]),
                                             True, WHITE, BLACK)

        self.screen.blit(game_title,
                         (WINDOW_SIZE[0]-game_title.get_size()[0], 0))
        self.screen.blit(coordinates,
                         (WINDOW_SIZE[0]-coordinates.get_size()[0],
                          WINDOW_SIZE[1]-coordinates.get_size()[1]))

        self.update_viewport(self.player)

        self.display_level(self.viewport)
        self.display_actor(self.viewport, self.player)

        pygame.display.flip()

    def update_viewport(self, player):
        self.viewport_cursor = (player.coordinates[0]-(self.viewsize[0]/2),
                                player.coordinates[1]-self.viewsize[1]/2)
        if self.viewport_cursor[0] < 0:
            self.viewport_cursor = (0, self.viewport_cursor[1])

        if self.viewport_cursor[1] < 0:
            self.viewport_cursor = (self.viewport_cursor[0], 0)
    
    def display_level(self, surface):
        x, y = 0, 0
        cursor = self.viewport_cursor
        size = self.viewsize
        grid2render = self.current_level.return_viewport(cursor, size)
            
        for row in grid2render:
            for cell in row:
                render_image = self.maplegend[type(cell)]
                surface.blit(render_image, (x*TILESIZE, y*TILESIZE))
                x += 1
            x = 0
            y += 1

    def display_actor(self, surface, actor):
        renderloc = (actor.coordinates[0]-self.viewport_cursor[0],
                     actor.coordinates[1]-self.viewport_cursor[1])
        x = renderloc[0] * TILESIZE
        y = renderloc[1] * TILESIZE
        surface.blit(self.actorlegend[actor], (x, y))

    def move_actor(self, actor, dx=0, dy=0):
        actor.move(dx, dy)
        self.update()

    def run(self):
        """Right now, just running things and listens to key presses for the
           exit key."""
        
        while True:
            self.clock.tick(30)
            for event in pygame.event.get():
                if not hasattr(event, 'key'): continue
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE: sys.exit()
                    if event.key == K_LEFT: self.move_actor(self.player, dx=-1)
                    if event.key == K_RIGHT: self.move_actor(self.player, dx=1)
                    if event.key == K_UP: self.move_actor(self.player, dy=-1)
                    if event.key == K_DOWN: self.move_actor(self.player, dy=1)
