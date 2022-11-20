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

class NormalTile(Tile):
    def __init__(self, x: int, y: int):
        Tile(x, y)
        self.TILE_TYPE = TileType.NORMAL

class ObstacleTile(Tile):
    def __init__(self, x: int, y: int):
        Tile(x, y)
        self.TILE_TYPE = TileType.OBSTACLE

class PickUpTile(Tile):
    def __init__(self, x: int, y: int):
        Tile(x, y)
        self.TILE_TYPE = TileType.PICK_UP

class DropOffTile(Tile):
    def __init__(self, x: int, y: int):
        Tile(x, y)
        self.TILE_TYPE = TileType.DROP_OFF

class SpawningTile(Tile):
    def __init__(self, x: int, y: int):
        Tile(x, y)
        self.TILE_TYPE = TileType.SPAWNING
    
    def spawnRobot(self):
        pass