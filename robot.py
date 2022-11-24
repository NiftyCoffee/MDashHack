from tile import *
from package import *

"""
Implementation of robot that moves the packages
"""

class Robot:

    DEFAULT_CHAR = "R"

    def __init__(self, current_tile: Tile) -> None:
        # Sets to R by default
        self.current_tile = current_tile
        self.current_tile.set_occupant(self)
        self.display_char = Robot.DEFAULT_CHAR
        self.inventory = None # should contain package
    
    def get_display_char(self) -> str:
        if self.holding_package():
            self.display_char = self.inventory.get_display_char()
        return self.display_char

    def pick_up_package(self, package: Package) -> None:
        self.inventory = package
    
    def holding_package(self) -> bool:
        return self.inventory is not None
    
    def travel(self, destination: Tile) -> None:
        # Check if destination tile is a valid exit and has no occupant
        if destination in self.current_tile.get_exits() and not destination.has_occupant():
            # Set occupant for destination tile to robot
            destination.set_occupant(self)
            # Remove robot from current tile
            self.current_tile.remove_occupant()
            # Update current tile to the destination tile
            self.current_tile = destination
    
    def travel_shortest_distance(self, destination: Tile, grid):
        min_distance = None
        nearest_exit = None

        # Loop through all exits
        for exit in self.current_tile.get_exits():
            # Base case: if destination is an exit
            if destination == exit:
                self.travel(destination)
                return
            # Calculate distance for every exit with no occupant
            if not exit.has_occupant():
                distance = abs(destination.get_x() - exit.get_x()) + abs(destination.get_y() - exit.get_y())
                if min_distance is None or min_distance > distance:
                    min_distance = distance
                    nearest_exit = exit
        # Travel to the exit closest to destination
        self.travel(nearest_exit)
        return self.travel_shortest_distance(destination, grid)