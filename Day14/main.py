## we would represent the space using a class 
## we assume here that the grid is created

## cur_position = [x, y] of the sand grain
## if it can it will fit the particle otherwise it would return -1
import ast 

def occupied(position):
    if (position=="#" or position=="o"):
        return True
    else:
        False


## -1 indicates particle falls off 
## else return None and attahces the particle 
def move_sand_particle(grid, cur_position):
    
    cur_row, cur_column = cur_position

    if(occupied(grid[cur_row][cur_column])):
        return -1
   
    if(cur_row+1>=len(grid)):
        return -1
        
    else:
        if(occupied(grid[cur_row+1][cur_column])):
            if(occupied(grid[cur_row+1][cur_column-1])):
                if(occupied(grid[cur_row+1][cur_column+1])):
                    grid[cur_row][cur_column]="o"
                    #print(cur_row, cur_column)
                    return
                else:
                    return move_sand_particle(grid, [cur_row+1, cur_column+1])
            else:
                return move_sand_particle(grid, [cur_row+1, cur_column-1])

        else:
            return move_sand_particle(grid, [cur_row+1, cur_column])
                

class Grid():

    def __init__(self, grid) -> None:
        self.grid = grid
        self.grain_of_sand = 0
        self.sand_still = False

    ## this would return -1 if grain of sand falls off otherwise it adds the grain
    def drop_sand(self):
        if(self.sand_still):
            return -1
        else:
            if(move_sand_particle(self.grid, [0,500]) is None):
                self.grain_of_sand +=1
            else: 
                self.sand_still = True

    def print_sand(self):
        print(self.grain_of_sand)

    def saturation(self):
        while(self.drop_sand() is None):
            pass

        self.print_sand()

#game.saturation()

def form_grid():
    max_row = 0 
    max_column = 0 

    with open("sample.in") as f:
        for line in f:
            line = line.strip()
            lst = line.split("->")
            for i in range(len(lst)):
               lst[i]=lst[i].strip()
               column,row = ast.literal_eval(lst[i])

               if(column>max_column):
                max_column=column

               if(row>max_row):
                max_row = row
    
    grid = [["." for i in range(max_column+2)] for j in range(max_row+3)]


    with open("sample.in") as f:
        for line in f:
            line = line.strip()
            lst = line.split("->")
            for i in range(len(lst)):
               lst[i]=lst[i].strip()
               lst[i]=ast.literal_eval(lst[i])

            prev_column, prev_row = 0,0    
            for i in range(len(lst)):
                if(i==0):
                    column,row = lst[i]
                    prev_column,prev_row=column,row
                    grid[row][column]="#"
                else: 
                    column,row = lst[i]
                    if(prev_column==column):
                        print("here")
                        if(prev_row<row):
                            for j in range(prev_row,row+1):
                                grid[j][column]="#"

                        else:
                            for j in range(row, prev_row+1):
                                grid[j][column]="#"

                    else:
                        if(column<prev_column):
                            for j in range(column, prev_column+1):
                                grid[row][j]="#"
                        else:
                            for j in range(prev_column, column+1):
                                grid[row][j]="#"
                    
                    prev_column,prev_row=column,row

    return grid
                            
grid = form_grid()

game = Grid(grid)

game.saturation()