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

    def get_size(self):
        return (max(len(spam) for spam in self.grid), len(self.grid))

            
class Actor(object):
    """Represents everyone who can act within the game, including the
    player."""

    def __init__(self, Level, coordinates):
        self.location, self.coordinates = Level, coordinates
        memory = [[0 for rows in Level.get_size[1]] for columns in
                  Level.get_size[0]]
        memory[coordinates[0], coordinates[1]] = 1  # You always know
                                                    # where you are in
                                                    # a level.
