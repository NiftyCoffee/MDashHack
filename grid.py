import csv

class Grid:

    CHAR_DICT = {0:".", 1:"_", 2:"^", 3:"#", 4:"+"}

    def __init__(self, file_name: csv):
        self.csv_file = file_name
        self.csv_list = self.csv_to_list()
        self.x_min = self.get_x_min()
        self.y_min = self.get_y_min()
        self.increment_x = 0 if self.x_min > 0 else abs(self.x_min)
        self.increment_y = 0 if self.y_min > 0 else abs(self.y_min)
        self.grid_list = self.initialise_empty_grid()
    
    def csv_to_list(self):
        with open(self.csv_file, 'r') as csv_file:
            csv_reader = list(csv.reader(csv_file))
            csv_list = []
            for line in csv_reader:
                csv_list.append(list(map(int, line)))
            return csv_list
    
    def get_x_range(self) -> int:
        max = self.csv_list[0][0]
        min = self.csv_list[0][0]
        for line in self.csv_list:
            if line[0] > max:
                max = line[0]
            elif line[0] < min:
                min = line[0]
        return max - min + 1
    
    def get_y_range(self) -> int:
        max = self.csv_list[0][1]
        min = self.csv_list[0][1]
        for line in self.csv_list:
            if line[1] > max:
                max = line[1]
            elif line[1] < min:
                min = line[1]
        return max - min + 1
    
    def get_x_min(self):
        min = self.csv_list[0][0]
        for line in self.csv_list:
            if line[0] < min:
                min = line[0]
        return min
    
    def get_y_min(self):
        min = self.csv_list[0][1]
        for line in self.csv_list:
            if line[1] < min:
                min = line[1]
        return min
    
    def initialise_empty_grid(self) -> list:
        arr = []
        x_range = self.get_x_range()
        y_range = self.get_y_range()

        for y_value in range(y_range):
            sub_arr = []
            for x_value in range(x_range):
                sub_arr.append(Grid.CHAR_DICT[0])
            arr.append(sub_arr)
        
        return arr

    def csv_to_grid(self):
        """with open(self.csv_file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            
            for line in csv_reader:
                if self.grid_list[line[1] + self.increment_y] is None: """
        
        for line in self.csv_list:
            self.grid_list[(line[1] + self.increment_y) * -1 - 1][line[0] + self.increment_x] = Grid.CHAR_DICT[line[2]]
    
    def display_grid(self):
        for line in self.grid_list:
            for char in line:
                print(char, end="")
            print()
    
    ##### GUIDE #####
    """
        0 -> .
        1 -> _
        2 -> ^
        3 -> #
        4 -> +
    """

if __name__ == '__main__':
    grid = Grid('test.csv')

    assert grid.get_x_range() == 10
    assert grid.get_y_range() == 8
    assert grid.x_min == -5
    assert grid.y_min == -4

    grid.csv_to_grid()
    grid.display_grid()