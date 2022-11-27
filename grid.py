import csv
from tile import *

class Grid:

    # <======== GUIDE ========>
    """
        0 -> NORMAL     -> .
        1 -> OBSTACLE   -> _
        2 -> PICK UP    -> ^
        3 -> DROP OFF   -> #
        4 -> SPAWNING   -> +
    """

    def __init__(self, file_name: csv) -> None:
        self.csv_file = file_name
        self.csv_list = self.csv_to_list()
        self.increment_x = self.get_increment_x()
        self.increment_y = self.get_increment_y()
        self.grid_list = self.initialise_empty_grid()
        self.spawning_tiles = []
        self.pick_up_tiles = []
        self.drop_off_tiles = []

        # Convert csv to grid
        self.csv_to_grid()
    
    def csv_to_list(self) -> list:
        """
        Convert csv file into an array of arrays containing int values
        """
        with open(self.csv_file, 'r') as csv_file:
            csv_reader = list(csv.reader(csv_file))
            csv_list = []
            for line in csv_reader:
                csv_list.append(list(map(int, line)))
            return csv_list
    
    def get_x_range(self) -> int:
        """
        Returns the range of x values
        """
        max = self.csv_list[0][0]
        min = self.csv_list[0][0]
        for line in self.csv_list:
            if line[0] > max:
                max = line[0]
            elif line[0] < min:
                min = line[0]
        return max - min + 1
    
    def get_y_range(self) -> int:
        """
        Returns the range of y values
        """
        max = self.csv_list[0][1]
        min = self.csv_list[0][1]
        for line in self.csv_list:
            if line[1] > max:
                max = line[1]
            elif line[1] < min:
                min = line[1]
        return max - min + 1
    
    def get_increment_x(self) -> int:
        """
        Returns the value to increment x by when inserting into the grid
        so the smallest x value is at 0
        """
        min = self.csv_list[0][0]
        for line in self.csv_list:
            if line[0] < min:
                min = line[0]
        return 0 if min >= 0 else min * -1
    
    def get_increment_y(self) -> int:
        """
        Returns the value to increment y by when inserting into the grid
        so the smallest y value is at 0
        """
        min = self.csv_list[0][1]
        for line in self.csv_list:
            if line[1] < min:
                min = line[1]
        return 0 if min >= 0 else min * -1
    
    def initialise_empty_grid(self) -> list:
        """
        Returns a default array of arrays containing None with the
        grid's height and width corresponding to the x and y ranges
        """
        arr = []
        x_range = self.get_x_range()
        y_range = self.get_y_range()

        for y_value in range(y_range):
            sub_arr = []
            for x_value in range(x_range):
                sub_arr.append(None)
            arr.append(sub_arr)
        
        return arr

    def csv_to_grid(self) -> None:
        """
        Initializes the values in the grid with Tile objects
        """
        for line in self.csv_list:
            if line[2] == 0:
                new_tile = NormalTile(line[0], line[1])
            elif line[2] == 1:
                new_tile = ObstacleTile(line[0], line[1])
            elif line[2] == 2:
                new_tile = PickUpTile(line[0], line[1])
                self.pick_up_tiles.append(new_tile)
            elif line[2] == 3:
                new_tile = DropOffTile(line[0], line[1])
                self.drop_off_tiles.append(new_tile)
            elif line[2] == 4:
                new_tile = SpawningTile(line[0], line[1])
                self.spawning_tiles.append(new_tile)
            else:
                raise ValueError("Invalid tile type")
            self.grid_list[(line[1] + self.increment_y) * -1 - 1][line[0] + self.increment_x] = new_tile
        
        # add exits for each tile
        self.set_exits()
    
    def set_exits(self) -> None:
        """
        Initializes the exits of each tile
        """
        # first row
        for col_num in range(len(self.grid_list[0])):
            if self.grid_list[0][col_num] is not None:
                if col_num == 0:
                    self.grid_list[0][col_num].add_exit(self.grid_list[0][col_num + 1])
                    self.grid_list[0][col_num].add_exit(self.grid_list[1][col_num + 1])
                    self.grid_list[0][col_num].add_exit(self.grid_list[1][col_num])
                elif col_num == len(self.grid_list[0]) - 1:
                    self.grid_list[0][col_num].add_exit(self.grid_list[1][col_num])
                    self.grid_list[0][col_num].add_exit(self.grid_list[1][col_num - 1])
                    self.grid_list[0][col_num].add_exit(self.grid_list[0][col_num - 1])
                else:
                    self.grid_list[0][col_num].add_exit(self.grid_list[0][col_num + 1])
                    self.grid_list[0][col_num].add_exit(self.grid_list[1][col_num + 1])
                    self.grid_list[0][col_num].add_exit(self.grid_list[1][col_num])
                    self.grid_list[0][col_num].add_exit(self.grid_list[1][col_num - 1])
                    self.grid_list[0][col_num].add_exit(self.grid_list[0][col_num - 1])

        # second row - second-last row
        for row_num in range(1,len(self.grid_list) - 1):
            for col_num in range(len(self.grid_list[row_num])):
                if self.grid_list[row_num][col_num] is not None:
                    if col_num == 0:
                        self.grid_list[row_num][col_num].add_exit(self.grid_list[row_num - 1][col_num])
                        self.grid_list[row_num][col_num].add_exit(self.grid_list[row_num - 1][col_num + 1])
                        self.grid_list[row_num][col_num].add_exit(self.grid_list[row_num][col_num + 1])
                        self.grid_list[row_num][col_num].add_exit(self.grid_list[row_num + 1][col_num + 1])
                        self.grid_list[row_num][col_num].add_exit(self.grid_list[row_num + 1][col_num])
                    elif col_num == len(self.grid_list[row_num]) - 1:
                        self.grid_list[row_num][col_num].add_exit(self.grid_list[row_num - 1][col_num])
                        self.grid_list[row_num][col_num].add_exit(self.grid_list[row_num + 1][col_num])
                        self.grid_list[row_num][col_num].add_exit(self.grid_list[row_num + 1][col_num - 1])
                        self.grid_list[row_num][col_num].add_exit(self.grid_list[row_num][col_num - 1])
                        self.grid_list[row_num][col_num].add_exit(self.grid_list[row_num - 1][col_num - 1])
                    else:
                        self.grid_list[row_num][col_num].add_exit(self.grid_list[row_num - 1][col_num])
                        self.grid_list[row_num][col_num].add_exit(self.grid_list[row_num - 1][col_num + 1])
                        self.grid_list[row_num][col_num].add_exit(self.grid_list[row_num][col_num + 1])
                        self.grid_list[row_num][col_num].add_exit(self.grid_list[row_num + 1][col_num + 1])
                        self.grid_list[row_num][col_num].add_exit(self.grid_list[row_num + 1][col_num])
                        self.grid_list[row_num][col_num].add_exit(self.grid_list[row_num + 1][col_num - 1])
                        self.grid_list[row_num][col_num].add_exit(self.grid_list[row_num][col_num - 1])
                        self.grid_list[row_num][col_num].add_exit(self.grid_list[row_num - 1][col_num - 1])
        
        # last row
        for col_num in range(len(self.grid_list[-1])):
            if self.grid_list[-1][col_num] is not None:
                if col_num == 0:
                    self.grid_list[-1][col_num].add_exit(self.grid_list[-1 - 1][col_num])
                    self.grid_list[-1][col_num].add_exit(self.grid_list[-1 - 1][col_num + 1])
                    self.grid_list[-1][col_num].add_exit(self.grid_list[-1][col_num + 1])
                elif col_num == len(self.grid_list[-1]) - 1:
                    self.grid_list[-1][col_num].add_exit(self.grid_list[-1][col_num - 1])
                    self.grid_list[-1][col_num].add_exit(self.grid_list[-1 - 1][col_num - 1])
                    self.grid_list[-1][col_num].add_exit(self.grid_list[-1 - 1][col_num])
                else:
                    self.grid_list[-1][col_num].add_exit(self.grid_list[-1 - 1][col_num])
                    self.grid_list[-1][col_num].add_exit(self.grid_list[-1 - 1][col_num + 1])
                    self.grid_list[-1][col_num].add_exit(self.grid_list[-1][col_num + 1])
                    self.grid_list[-1][col_num].add_exit(self.grid_list[-1][col_num - 1])
                    self.grid_list[-1][col_num].add_exit(self.grid_list[-1 - 1][col_num - 1])

    def display_grid(self) -> None:
        """
        Displays the grid
        """
        for line in self.grid_list:
            for tile in line:
                if tile is None:
                    print(" ", end="")
                else:
                    print(tile.get_display_char(), end="")
            print()

if __name__ == '__main__':

    # <======== TESTS ========>
    print("Test 1")
    grid1 = Grid('test_file_1.csv')
    grid1.display_grid()

    print()

    print("Test 2")
    grid2 = Grid('test_file_2.csv')
    grid2.display_grid()

    print()

    print("Test 3")
    grid3 = Grid('video_example.csv')
    grid3.display_grid()

    print()

    print("Test 4")
    grid4 = Grid('factory_demo.csv')
    grid4.display_grid()