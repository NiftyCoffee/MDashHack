import tile

"""
Implementation of robot that moves the packages
"""

class Robot:
    robot_character = "R"

    def __init__(self, current_tile: tile.Tile):
        # Sets to R by default
        self.character = Robot.robot_character
        self.inventory = None # shoud contain package
        pass

