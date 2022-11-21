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
                self.grid_list[(line[1] + self.increment_y) * -1 - 1][line[0] + self.increment_x] = NormalTile(line[0], line[1])
            elif line[2] == 1:
                self.grid_list[(line[1] + self.increment_y) * -1 - 1][line[0] + self.increment_x] = ObstacleTile(line[0], line[1])
            elif line[2] == 2:
                self.grid_list[(line[1] + self.increment_y) * -1 - 1][line[0] + self.increment_x] = PickUpTile(line[0], line[1])
            elif line[2] == 3:
                self.grid_list[(line[1] + self.increment_y) * -1 - 1][line[0] + self.increment_x] = DropOffTile(line[0], line[1])
            elif line[2] == 4:
                self.grid_list[(line[1] + self.increment_y) * -1 - 1][line[0] + self.increment_x] = SpawningTile(line[0], line[1])
            else:
                raise ValueError("Invalid tile type")
    
    def display_grid(self) -> None:
        """
        Displays the grid
        """
        for line in self.grid_list:
            for tile in line:
                if tile is None:
                    print(" ", end="")
                else:
                    print(tile.TILE_TYPE.value, end="")
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