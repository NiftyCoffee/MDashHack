from grid import *
from tile import *
from robot import *
from package import *
import time

# Setting up the grid
world_grid = Grid('test_file_1.csv')
robots_on_grid = []
num_robots_on_grid = None

num_robots = int(input("Number of robots: "))
num_packages = int(input("Number of packages: "))

packages_to_deliver = num_packages

# main system loop
while packages_to_deliver > 0 or num_robots_on_grid != 0:

    # move all robots currently on the grid
    for index in range(len(robots_on_grid)):
        if robots_on_grid[index] is not None:
            if robots_on_grid[index].holding_package():
                destination = robots_on_grid[index].nearest_destination(world_grid.drop_off_tiles)
                if robots_on_grid[index].travel_nearest_exit(destination):
                    packages_to_deliver -= 1
            elif num_packages > 0:
                destination = robots_on_grid[index].nearest_destination(world_grid.pick_up_tiles)
                if robots_on_grid[index].travel_nearest_exit(destination):
                    robots_on_grid[index].pick_up_package(Package())
                    num_packages -= 1
            else:
                destination = robots_on_grid[index].nearest_destination(world_grid.spawning_tiles)
                if robots_on_grid[index].travel_nearest_exit(destination) and num_packages == 0:
                    robots_on_grid[index].current_tile.remove_occupant()
                    robots_on_grid[index] = None
                    num_robots_on_grid -= 1

    # spawn remaining robots
    for tile in world_grid.spawning_tiles:
        if num_robots > 0:
            if tile.set_occupant(Robot(tile)):
                robots_on_grid.append(tile.get_occupant())
                if num_robots_on_grid is None:
                    num_robots_on_grid = 0
                num_robots_on_grid += 1
                num_robots -= 1
        else:
            break
    
    time.sleep(0.2)
    world_grid.display_grid()
    print()