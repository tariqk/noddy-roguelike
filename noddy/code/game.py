#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os

from tiles import Wall, Floor
from constants import *


class Level(object):
    """Represents the current level.

    Try and avoid referencing stuff that only matters to the viewport
    (i.e. paths to render images.)

    EXPECTED WONKY BEHAVIOUR: Obviously if the test map is uneven,
    it'll treat the game size as (longest line length, number of
    rows). Dunno if it'll fuck up anything. This shit is temporary
    anyway.

    """

    def __init__(self):
        """Initialize. Currently just loads a test level."""
        self.grid = []
        self.level_gen()

    def level_gen(self):
        """Stub for level-generation code. Right now reads a test-file."""
        tmp = []
        
        test_level_file = open(os.path.join(RES_DIR, 'txt',
                                            'test-chambers.map'), 'r')

        for line in test_level_file.readlines():
            tmp.append(list(line.strip()))

        test_level_file.close()

        maplegend = {"#": Wall(),
                     ".": Floor()}
        
        for row in tmp:
            tmp_row = []
            for cell in row:
                tmp_row.append(maplegend[cell])
            self.grid.append(tmp_row)

    def return_viewport(self, start=(0, 0), size=(1, 1)):
        """Return viewport to render."""
        result = []
        for row in self.grid[start[1]:start[1]+size[1]]:
            result.append(row[start[0]:start[0]+size[0]])
        return result

    def get_size(self):
        """Returns a the size of the level, represented in a tuple
        (width, height)."""
        y = len(self.grid)
        columns = []
        for row in self.grid:
            columns.append(len(row))
        x = max(columns)
        return ((x, y))

    def is_passable(self, coordinates=(0, 0)):
        """Temporary stub function for determining whether a space is
           passable or not."""
        x, y = coordinates[0], coordinates[1]
        return self.grid[y][x].is_passable()

    def within_bounds(self, coordinates=(0, 0)):
        """ Is the location within bounds? """
        x, y = coordinates[0], coordinates[1]
        if x < 0 or y < 0:
            return False
        elif x == self.get_size()[0] or y == self.get_size()[1]:
            return False
        else:
            return True


class Actor(object):
    """Represents everyone who can act within the game, including the
    player."""

    def __init__(self, Level, coordinates=(0, 0)):
        self.location, self.coordinates = Level, coordinates
        memory_size = Level.get_size()
        self.memory = [[0 for columns in range(memory_size[0])] for
                       rows in range(memory_size[1])]
        self.remember(coordinates[0], coordinates[1])

    def remember(self, x=0, y=0):
        """Remember a place in the memory grid."""
        if self.memory[y][x] == 0:
            self.memory[y][x] == 1

    def move(self, dx=0, dy=0):
        """ Move the actor."""
        dest_x = self.coordinates[0] + dx
        dest_y = self.coordinates[1] + dy

        passable = self.location.is_passable((dest_x, dest_y))
        in_bounds = self.location.within_bounds((dest_x, dest_y))

        if passable and in_bounds:
            self.coordinates = (dest_x, dest_y)
        else:
            pass
