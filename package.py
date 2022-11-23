from tile import *

"""
Implementation of a package
"""

class Package:

    DISPLAY_CHAR = 'P'

    def __init__(self, current_tile):
        self.current_tile = current_tile
        self.character = Package.DISPLAY_CHAR