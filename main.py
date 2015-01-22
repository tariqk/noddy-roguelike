#! /usr/bin/env python

import pygame, math, sys, os, traceback
from pygame.locals import *

sys.path.append("noddy/code")

from constants import *
from game import Level
from viewport import Game

# CLASSES


# UTILITY FUNCTIONS

def main():
    """ 
    main loop 
    """
    game = Game()

# THE RUNNING PROGRAM
        
if __name__ == "__main__":
    try:
        pygame.init()
        main()
    except Exception, e:
        tb = sys.exc_info()[2]
        traceback.print_exception(e.__class__, e, tb)
    pygame.quit()
