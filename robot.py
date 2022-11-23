from tile import *
from package import *

"""
Implementation of robot that moves the packages
"""

class Robot:
    DISPLAY_CHAR = "R"

    def __init__(self, current_tile: Tile) -> None:
        # Sets to R by default
        self.current_tile = current_tile
        self.character = Robot.DISPLAY_CHAR
        self.inventory = None # shoud contain package

    def pick_up_package(self, package: Package) -> None:
        self.inventory = package
        self.character = package.character
    
    def travel(self, destination: Tile) -> None:
        # Check if destination tile is a valid exit and has no occupant
        if destination in self.current_tile.get_exits() and not destination.has_occupant():
            # Set occupant for destination tile to robot
            destination.set_occupant(self)
            # Remove robot from current tile
            self.current_tile.remove_occupant()
            # Update current tile to the destination tile
            self.current_tile = destination
    
    def travel_shortest_distance(self, destination: Tile):
        min_distance = None
        nearest_exit = None
        for exit in self.current_tile.get_exits():
            if destination == exit:
                self.travel(destination)
                return
            if not exit.has_occupant():
                distance = (destination.get_x() - exit.get_x()) + (destination.get_y() - exit.get_y())
                if min_distance > distance or min_distance is None:
                    min_distance = distance
                    nearest_exit = exit
        return self.travel_shortest_distance(nearest_exit)