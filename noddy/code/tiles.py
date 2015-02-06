#! /usr/bin/env python
# -*- coding: utf-8 -*-

from constants import *

"""This module implements the tiles interface, and serves as a bridge
between both viewport.py and game.py. Or something. I'm still figuring
this out.

The design of this class currently comes from Yannick Loiseau's
“Design Patterns and Python: Flyweight page:

http://yloiseau.net/articles/DesignPatterns/flyweight/

Specifically, this is the Mixin class version, which should allow me
to easily subclass and introspect better than other version.

"""


class Tiles(object):
    """Represents all Tiles within the game.

    Abstract class. Is subclassed before can be used properly.

    """
    _instances = dict()  # alternatively, use weakref

    def __init__(s, *a, **kwa):
        raise NotImplementedError

    def __new__(c, *a, **kwa):
        return c._instances.setdefault(
            (c, a, tuple(kwa.items())),
            super(type(c), c).__new__(c, *a, **kwa))

    @classmethod
    def is_passable(self):
        """Returns whether this tile is passable by solid Actors or not."""
        return self._passable

    @classmethod
    def is_blocking(self):
        """Returns whether this tile blocks Actor's vision or not."""
        return self._blocking

    def when_enter(self, Actor):
        """Actions to actor when entering a tile."""
        pass

    def when_leave(self, Actor):
        """Actions when leaving a tile."""
        pass

    def when_stay(self, Actor):
        """Action when Actor decides to stay."""
        pass


"""Tile Definitions"""


class Floor(Tiles):
    """The default floor type."""
    _passable = True
    _blocking = False

    def __init__(self):
        pass


class Wall(Tiles):
    """The default wall type."""
    _passable = False
    _blocking = True

    def __init__(self):
        pass
