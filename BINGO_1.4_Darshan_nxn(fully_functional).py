'''Not incorpoated the default limit of recursion and stacksize which might break with higher values of grid and players
more information on
1. https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-in-python-and-how-to-increase-it
2. https://stackoverflow.com/questions/5061582/setting-stacksize-in-a-python-script'''
import random
inputs = []

def user_inp_num(string):
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
    string = str(string)
    if len(string) == grid_str_len:
        return string
    else:
        return (' '*(grid_str_len-len(str(string)))+ string)

def make_grid(size, grid_elm, grid_str_len, grid):
    temp = [conv_str(i, grid_str_len) for i in range (1, grid_elm+1)]
    random.shuffle(temp)
    count = 0
    for i in range(size):
        for j in range(count*size, (count+1)*size):
            grid[i].append(temp[j])
        count += 1
    return grid

def show_grid(k, message = None):
    if message:
        print(str(message))
    for i in range(size):
        for j in range(size):
            print(players[k].grid[i][j], end = ' ')
        print()

def check_column(num1, num2, l):
    if ((num1 > 1) and (players[l].grid[num1][num2] == players[l].grid[num1-1][num2])):
        return check_column(num1-1, num2, l)
    elif (((num1 == 1) and (players[l].grid[1][num2] == players[l].grid[0][num2])) or (num1 == 0)):
        return True
    else:
        return False

def check_main_diagonal(i, l):
    if i < size-1:
        if players[l].grid[i][i] == players[l].grid[i+1][i+1]:
            return check_main_diagonal(i+1, l)
        else:
            return False
    elif i == size-1:
        return True

def check_other_diagonal(i, l):
    if i > 0:
        if players[l].grid[(size-1)-i][i] == players[l].grid[(size-1)-(i-1)][i-1]:
            return check_other_diagonal(i-1, l)
        else:
            return False
    elif i == 0:
        return True

def user_inp_num_cut(grid_elm, grid_str_len, inputs):
        temp1 = user_inp_num('The number to cut: ')
        temp2 = str(temp1)
        if ((temp1 > grid_elm) or (temp2 in inputs)):
            print('Enter a number from the given grid!')
            return user_inp_num_cut(grid_elm, grid_str_len, inputs)
        else:
            inputs.append(temp2)
            temp2 = conv_str(temp2, grid_str_len)
            return temp2


class Player:
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
        
print('Enter the size of the grid : ', end = '')
size = user_inp_num('')

grid_elm = size ** 2
grid_str_len = len(str(grid_elm))

player_num = user_inp_num('Enter the number of players : ')
players = [Player(input('Enter the name of player : ')) for k in range(player_num)]
for k in range(player_num):
    players[k].grid = [[] for i in range (size)]
    players[k].grid = make_grid(size, grid_elm, grid_str_len, players[k].grid)
    
game_over = False
print('\nPlay\n')
while(game_over is False):
    for k in range(player_num):
        show_grid(k, '\nGrid of '+players[k].name+"'s right now : ")
        temp1 = user_inp_num_cut(grid_elm, grid_str_len, inputs)
        for l in range(player_num):
            for i in range(size):
                if temp1 in players[l].grid[i]:
                    temp2 = players[l].grid[i].index(temp1)
                    players[l].grid[i][temp2] = (' '*(grid_str_len-1)+ 'X')
                    
                    if ((players[l].horz is None) or (i not in players[l].horz)):
                        if len(set(players[l].grid[i])) == 1:
                            players[l].score += 1
                            players[l].add_to_horz(i)
                            
                    if ((players[l].vert is None) or (temp2 not in players[l].vert)):
                        if check_column(size-1, temp2, l) is True:
                            players[l].score += 1
                            players[l].add_to_vert(temp2)
                                  
                    if players[l].md == 0:
                        if check_main_diagonal(0, l) is True:
                            players[l].score += 1
                            players[l].md += 1
                                  
                    if players[l].od == 0:
                        if check_other_diagonal(size-1, l) is True:
                            players[l].score += 1
                            players[l].od += 1

            print('The score of', players[l].name, 'is', players[l].score)
            if players[l].score >= size:
                game_over = True
                print('congratulations,', players[l].name, 'won!')
                    
        show_grid(k, '\nAfter cutting the input, '+players[k].name+"'s grid : ")
        if game_over == True:
            break
        
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
