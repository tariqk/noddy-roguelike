#! /usr/bin/env python

import os

# colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# sizes

TILESIZE = 16  # ASSUMPTION: icons are square
WINDOW_SIZE = (800,600) # placeholder
MAPSIZE = (WINDOW_SIZE[0]/TILESIZE, (WINDOW_SIZE[1]/TILESIZE)-2)
LARGETEXT = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# resource locations

RES_DIR = os.path.join(os.getcwd(), 'noddy', 'res')
