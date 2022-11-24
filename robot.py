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
        self.display_char = Robot.DEFAULT_CHAR
        self.package = None # should contain package
    
    def get_display_char(self) -> str:
        if self.holding_package():
            self.display_char = self.package.get_display_char()
        return self.display_char

    def pick_up_package(self, package: Package) -> None:
        if not self.holding_package():
            self.package = package

    def drop_off_package(self) -> None:
        self.package = None
        self.display_char = Robot.DEFAULT_CHAR
    
    def holding_package(self) -> bool:
        return self.package is not None
    
    def calculate_distance(self, origin: Tile, destination: Tile) -> int:
        return abs(destination.get_x() - origin.get_x()) + abs(destination.get_y() - origin.get_y())
    
    def travel(self, destination: Tile) -> None:
        if destination is not None:
            # Check if destination tile is a valid exit and has no occupant
            if destination in self.current_tile.get_exits() and not destination.has_occupant():
                # Set occupant for destination tile to robot
                destination.set_occupant(self)
                # Remove robot from current tile
                self.current_tile.remove_occupant()
                # Update current tile to the destination tile
                self.current_tile = destination
    
    """            
    def travel_shortest_distance(self, destination: Tile):
        if destination is not None:
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
                    distance = self.calculate_distance(exit, destination)
                    if min_distance is None or min_distance > distance:
                        min_distance = distance
                        nearest_exit = exit
            # Travel to the exit closest to destination
            self.travel(nearest_exit)
            return self.travel_shortest_distance(destination)
    """

    def travel_nearest_exit(self, destination: Tile) -> None:
        """
        Return true if destination is reached; false otherwise
        """
        if destination is not None:
            min_distance = None
            nearest_exit = None

            # Loop through all exits
            for exit in self.current_tile.get_exits():
                if not exit.has_occupant():
                    if destination == exit:
                        self.travel(destination)
                        return True
                    distance = self.calculate_distance(exit, destination)
                    if min_distance is None or min_distance > distance:
                        min_distance = distance
                        nearest_exit = exit
            self.travel(nearest_exit)
        return False
    
    def nearest_destination(self, destinations: list) -> Tile:
        min_distance = None
        destination = None
        for tile in destinations:
            if not tile.has_occupant():
                distance = self.calculate_distance(self.current_tile, tile)
                if min_distance is None or min_distance > distance:
                    min_distance = distance
                    destination = tile
        return destination
    
    """
    def nearest_pick_up_tile(self, pick_up_tiles: list) -> PickUpTile:
        min_distance = None
        nearest_tile = None
        for tile in pick_up_tiles:
            if tile.has_package() and not tile.has_occupant():
                distance = self.calculate_distance(self.current_tile, tile)
                if min_distance is None or min_distance > distance:
                    min_distance = distance
                    nearest_tile = tile
        return nearest_tile
    """