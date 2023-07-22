'''Not incorpoated the default limit of recursion and stacksize which might break with higher values of grid and players
more information on
1. https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-in-python-and-how-to-increase-it
2. https://stackoverflow.com/questions/5061582/setting-stacksize-in-a-python-script'''

#importing required modules
import random
from os import name, system

#List storing all the inputs
inputs = []

def user_inp_num(string):
    """This takes input from user and handle edge cases."""
    try:
        size = int(input(string))
        if size > 0:
            return size
        else:
            print('Put a positive non-zero number. ')
            return user_inp_num(string)
    except ValueError:
        print('Try again! Put an integral value. ')
        return user_inp_num(string)

def conv_str(string, grid_str_len):
    """Adds extra spaces to the start of digits whose length is less than that of maximum digits...
        Example: if maximum number of grid is 49(if grid size is 7x7) i.e. 2 digits,
        it adds " " to every leading digit of numbers having less than 2 digits."""
    string = str(string)
    if len(string) == grid_str_len:
        return string
    else:
        return (' '*(grid_str_len-len(str(string)))+ string)

def make_grid(size, grid_elm, grid_str_len, grid):
    """ This function makes the grid according to the size of the grid input from user."""
    temp = [conv_str(i, grid_str_len) for i in range (1, grid_elm+1)]
    random.shuffle(temp)
    count = 0
    for i in range(size):
        for j in range(count*size, (count+1)*size):
            grid[i].append(temp[j])
        count += 1
    return grid

def design(grid_str_len_p1):
    """ Stylize the printing of the grid, in each row for the user to follow."""
    print('+', end = '')
    for j in range(size):
            print('-'*grid_str_len_p1, end = '+')
    print()

def show_grid(k,grid_str_len_p1, message = None):
    """ Handles the whole printing of the grid to the user. """
    if message:
        print(str(message))
    design(grid_str_len_p1)
    for i in range(size):
        print('| ', end = '')
        for j in range(size):
            print(players[k].grid[i][j], end = '| ')
        print()
        design(grid_str_len_p1)

def check_column(num1, num2, l):
    """ Checks if the whole column is cut in the grid. """
    if ((num1 > 1) and (players[l].grid[num1][num2] == players[l].grid[num1-1][num2])):
        return check_column(num1-1, num2, l)
    #handling edge cases
    elif (((num1 == 1) and (players[l].grid[1][num2] == players[l].grid[0][num2])) or (num1 == 0)):
        return True
    else:
        return False

def check_main_diagonal(i, l):
    """ Checks the main diagonal if its cut of the grid(the one that goes from top left to bottom right). """
    if i < size_m1:
        if players[l].grid[i][i] == players[l].grid[i+1][i+1]:
            return check_main_diagonal(i+1, l)
        else:
            return False
    elif i == size_m1:
        return True

def check_other_diagonal(i, l):
    """ Checks the other diagonal of the grid(the one that goes from top right to bottom left). """    
    if i > 0:
        if players[l].grid[(size_m1)-i][i] == players[l].grid[(size_m1)-(i-1)][i-1]:
            return check_other_diagonal(i-1, l)
        else:
            return False
    elif i == 0:
        return True

def user_inp_num_cut(grid_elm, grid_str_len, inputs):
    """ Function handling to cut an input number from the grid generated taking user input. """
        temp1 = user_inp_num('The number to cut: ')
        temp2 = str(temp1)
        if ((temp1 > grid_elm) or (temp2 in inputs)):
            print('Enter a number from the given grid and not cut!')
            return user_inp_num_cut(grid_elm, grid_str_len, inputs)
        else:
            inputs.append(temp2)
            temp2 = conv_str(temp2, grid_str_len)
            return temp2


class Player:
    """ Player having attributes such as name, their individual grid, and other elements
        necessary for checking for their score. """
    def __init__(self, name, grid=[], horz=None, vert=None, md=0, od=0, score=0):
        self.grid = grid
        self.name = name
        self.horz = horz
        self.vert = vert
        self.md = md
        self.od = od
        self.score = score

    def add_to_horz(self, value):
        if self.horz:
            self.horz.append(value)
        elif self.horz is None:
            self.horz = []
            self.horz.append(value)
            
    def add_to_vert(self, value):
        if self.vert:
            self.vert.append(value)
        elif self.vert is None:
            self.vert = []
            self.vert.append(value)

# Lambda function to clear the screen after each input
# Note: This does not work when executed in the python IDLE.
cls = lambda: system('cls' if name in ('nt','dos') else 'clear')


""" Main execution of the program starts """

print('Enter the size of the grid : ', end = '')
size = user_inp_num('')
# Declared some variabls for stopping repeated execution of subtraction or multiplication.
size_m1= size - 1
grid_elm = size ** 2
grid_str_len = len(str(grid_elm))
grid_str_len_p1 = grid_str_len + 1
grid_str_len_m1 = grid_str_len - 1

# Initializing all the players in memory
player_num = user_inp_num('Enter the number of players : ')
players = [Player(input('Enter the name of player : ')) for k in range(player_num)]
for k in range(player_num):
    players[k].grid = [[] for i in range (size)]
    players[k].grid = make_grid(size, grid_elm, grid_str_len, players[k].grid)

# flag to stop game execution when someone wins
game_over = False

print('\nPlay\n')

while(game_over is False):
    for k in range(player_num):
        show_grid(k,grid_str_len_p1, f"\nGrid of {players[k].name}'s right now : ")
        temp1 = user_inp_num_cut(grid_elm, grid_str_len, inputs)
        
        # Checks for all the cancellation and possible wins of the players
        for l in range(player_num):
            for i in range(size):
                if temp1 in players[l].grid[i]:
                    temp2 = players[l].grid[i].index(temp1)
                    players[l].grid[i][temp2] = (' '*(grid_str_len_m1)+ 'X')
                    
                    if ((players[l].horz is None) or (i not in players[l].horz)):
                        # Checks for row cacellation by turning it into set
                        # (can be made faster but I amm  lazy ;) )
                        if len(set(players[l].grid[i])) == 1:
                            players[l].score += 1
                            players[l].add_to_horz(i)
                    
                    if ((players[l].vert is None) or (temp2 not in players[l].vert)):
                        if check_column(size_m1, temp2, l) is True:
                            players[l].score += 1
                            players[l].add_to_vert(temp2)
                                  
                    if players[l].md == 0:
                        if check_main_diagonal(0, l) is True:
                            players[l].score += 1
                            players[l].md += 1
                                  
                    if players[l].od == 0:
                        if check_other_diagonal(size_m1, l) is True:
                            players[l].score += 1
                            players[l].od += 1
            """ Can be made to be displayed at the end of the grid showing but not done it
                IamLazy """
            if players[l].score >= size:
                game_over = True
                print('congratulations,', players[l].name, 'won!')
                      
        # Show grid of the current player
        show_grid(k, grid_str_len_p1, f"\nAfter cutting {temp1} from {players[k].name}'s grid : ")
        temp3 = input('Enter any key...')
        cls()
        
        # Shows score of every player after each value is cut.
        for l in range(player_num):
            print('The score of', players[l].name, 'is', players[l].score)
            
        if game_over is True:
            break

# Finally print all the values cut during session.
print('These were the values cut during the whole session : ', inputs)

    
'''Version 1.2 changes:
1. Some aesthetic changes.
2. Changed things to definitions as much as possible for impoving readability.'''
'''Version 1.3 changes:
1. Added voice assistance supported in android versions of python(QPython3L).'''
'''Version 1.4 changes:
1. Removed annoying voice assistance supported in android versions of python(QPython3L).
2. Added multiplayer support.
3. Changed annoying zeroes(0) to spaces( ).
4. Added some bug fixes.
5. Removed comments.'''
'''Version 1.5 changes:
1. Made the grid more decorative.
2. Made the console to override itself during each players' turn.
3. Quality of life changes.
4. Optimized program.'''
