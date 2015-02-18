#! /usr/bin/env python

import pygame
import sys
import traceback
from pygame.locals import *

sys.path.append("noddy/code")

from constants import *
from viewport import Game


def main():
    """
    main loop
    """
    game = Game()

# THE RUNNING PROGRAM

if __name__ == "__main__":
    try:
        pygame.init()
        pygame.key.set_repeat(200, 50)
        main()
    except Exception, e:
        tb = sys.exc_info()[2]
        traceback.print_exception(e.__class__, e, tb)
    pygame.quit()
