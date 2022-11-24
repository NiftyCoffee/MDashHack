from abc import ABC, abstractmethod
from enum import Enum

"""
Implementation of a tile on the grid
"""

class TileType(Enum):
    """
    Enum constants mapping each type of tile to its respective display character
    """
    NORMAL = '.'
    OBSTACLE = '_'
    PICK_UP = '^'
    DROP_OFF = '#'
    SPAWNING = '+'

class Tile(ABC):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.occupant = None
        self.tile_type = None
        self.display_char = None
        self.exits = []

    def get_display_char(self) -> str:
        if self.has_occupant():
            self.display_char = self.get_occupant().get_display_char()
        return self.display_char

    def has_occupant(self) -> bool:
        return self.occupant is not None

    def get_occupant(self):
        return self.occupant

    def set_occupant(self, occupant):
        self.occupant = occupant
    
    def remove_occupant(self):
        self.occupant = None
        self.display_char = self.tile_type.value
    
    def get_x(self) -> int:
        return self.x
    
    def get_y(self) -> int:
        return self.y
    
    def add_exit(self, exit: 'Tile'):
        if exit is not None and exit.tile_type != TileType.OBSTACLE:
            self.exits.append(exit)
    
    def get_exits(self) -> list:
        return self.exits

class NormalTile(Tile):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.tile_type = TileType.NORMAL
        self.display_char = self.tile_type.value

class ObstacleTile(Tile):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.tile_type = TileType.OBSTACLE
        self.display_char = self.tile_type.value

class PickUpTile(Tile):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.tile_type = TileType.PICK_UP
        self.display_char = self.tile_type.value

    def spawn_package(self):
        pass

class DropOffTile(Tile):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.tile_type = TileType.DROP_OFF
        self.display_char = self.tile_type.value

class SpawningTile(Tile):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.tile_type = TileType.SPAWNING
        self.display_char = self.tile_type.value
    
    def spawn_robot(self):
        pass