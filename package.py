from tile import *

"""
Implementation of a package
"""

class Package:

    DEFAULT_CHAR = 'P'

    def __init__(self):
        self.display_char = Package.DEFAULT_CHAR
    
    def get_display_char(self) -> str:
        return self.display_char