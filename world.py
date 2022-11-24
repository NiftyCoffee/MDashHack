from grid import *
from tile import *
from robot import *
from package import *

"""
tile1 = NormalTile(3, 6)
robot1 = Robot(tile1)
package1 = Package(tile1)
tile1.set_occupant(robot1)

grid1 = Grid('test_file_1.csv')
grid1.grid_list[2][2] = tile1
grid1.display_grid()
robot1.pick_up_package(package1)
grid1.display_grid()
"""

"""
grid1 = Grid('test_file_1.csv')
for exit in grid1.grid_list[-2][6].get_exits():
    print(exit.x, exit.y, exit.tile_type)
print(grid1.grid_list[-2][6].tile_type)
"""

grid1 = Grid('test_file_1.csv')
robot1 = Robot(grid1.grid_list[6][7])
grid1.display_grid()
#robot1.travel(grid1.grid_list[5][6])
robot1.travel_shortest_distance(grid1.grid_list[4][8], grid1)
grid1.display_grid()
