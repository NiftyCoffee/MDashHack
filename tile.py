from abc import ABC, abstractmethod
from enum import Enum
from robot import Robot

"""
Implementation of a tile on the grid
"""

class TileType(Enum):
    """
    Enum constants mapping each type of tile to its respective int
    """
    NORMAL = 0
    OBSTACLE = 1
    PICK_UP = 2
    DROP_OFF = 3
    SPAWNING = 4

class Tile(ABC):
    def __init__(self, x: int, y: int, robot: Robot):
        self.x = x
        self.y = y
    
    def get_location(self):
        return (self.x, self.y)
    
    def get_type(self):
        return self.TILE_TYPE

class NormalTile(Tile):
    def __init__(self):
        super()
        self.TILE_TYPE = TileType.NORMAL

class ObstacleTile(Tile):
    def __init__(self):
        super()
        self.TILE_TYPE = TileType.OBSTACLE

class PickUpTile(Tile):
    def __init__(self):
        super()
        self.TILE_TYPE = TileType.PICK_UP

class DropOffTile(Tile):
    def __init__(self):
        super()
        self.TILE_TYPE = TileType.DROP_OFF

class SpawningTile(Tile):
    def __init__(self):
        super()
        self.TILE_TYPE = TileType.SPAWNING
    
    def spawnRobot(self):
        pass