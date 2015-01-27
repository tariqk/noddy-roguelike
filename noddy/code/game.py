#! /usr/bin/env python

import os

from constants import *

class Level(object):
    """Represents the current level.

    Try and avoid referencing stuff that only matters to the viewport
    (i.e. paths to render images.)

    EXPECTED WONKY BEHAVIOUR: Obviously if empty-chamber.map is
    uneven, it'll treat the game size as (longest line length, number
    of rows). Dunno if it'll fuck up anything. This shit is temporary
    anyway."""
    
    grid = []
    
    def __init__(self):
        """Initialize. Currently just loads a test level."""
        test_level_file = open(os.path.join(RES_DIR, 'txt',
                                            'empty-chamber.map'), 'r')

        for line in test_level_file.readlines():
            self.grid.append(list(line.strip()))

        test_level_file.close()

    def print_ascii_map(self):
        for row in self.grid:
            for column in self.grid:
                print cell,

    def return_viewport(self, start=(0,0), size=(1,1)):
        result = []
        for row in self.grid[start[1]:start[1]+size[1]]:
            result.append(row[start[0]:start[0]+size[0]])
        return result

    def get_size(self):
        y = len(self.grid)
        columns = []
        for row in self.grid:
            columns.append(len(row))
        x = max(columns)
        return ((x, y))

            
class Actor(object):
    """Represents everyone who can act within the game, including the
    player."""

    def __init__(self, Level, coordinates=(0,0)):
        self.location, self.coordinates = Level, coordinates
        memory_size = Level.get_size()
        self.memory = [[0 for columns in range(memory_size[0])] for
                       rows in range(memory_size[1])]
        self.memory[self.coordinates[1]][self.coordinates[0]] = 1  # You always know where you are in a level.
