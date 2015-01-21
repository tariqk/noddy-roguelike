#! /usr/bin/env python

from constants import *

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
