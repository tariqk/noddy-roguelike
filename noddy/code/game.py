#! /usr/bin/env python

from constants import *

class Level(object):
    """
    Represents the current level.
    """
    def __init__(self, size=MAPSIZE):
        self.new_map(size)

    def new_map(self, size):
        """
        Generate new map -- currently only creates an empty map.

        Right now it assumes that map = fog of war. 

        TODO: separate map geometry and fog of war. By rights, fog of
              war tells the game what to display; but the map remains
              the map.
        """
        self.map = [[0 for rows in range(size[1])] for columns in range(size[0])]
        
    def print_ascii_map(self):
        for row in self.map:
            print row

            
