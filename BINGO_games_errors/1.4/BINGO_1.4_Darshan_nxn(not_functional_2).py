
"""
GO TO THE LINE NO.128,129, 134,135 TO SEE THE ERROR
a)error being changing mutable variables in a class instance changes its value in class along with all other class instance.

    MORE ON THIS HERE:
    1. https://stackoverflow.com/questions/2424451/compound-assignment-to-python-class-and-instance-variables
    2. https://stackoverflow.com/questions/2681243/how-should-i-declare-default-values-for-instance-variables-in-python

b)using difference between '==' and 'is' keyword:
    '==' IS USED TO CHECK THE VALUE OF THE THINGS IN THE TWO SIDES, E.G.,X == Y
    'is' KEYWORD USED TO CHECK THE ID OF THE THINGS ON TWO SIDES, EQUIVALENT TO id(X)== id(Y), NOSTLY USED IN BOOLEAN VALUES CHECKING

c)problem with using default value of a variable while defining a function
    E.G.    def append(a, l=[]):
                l.append(a)
                return l
            a = append(10)
        #>>>a = [10]#AS INTENDED
        b = append(20)
        #>>>a = [10,20]#NOT INTENDED
    THIS HAPPENS BECAUSE DEFAULT VALUE ARE MADE NOT WHEN THE FUNCTION CALL BUT WHEN THE FUNCTION IS DEFINED.
    
"""


import random
# Copyright (C) 2012, Hariharan Srinath, Robbie Matthews
#from androidhelper import Android
#Android = Android()

def user_inp_num(string):
    try:
        size = int(input(string))
        if size > 0:
            return size
        else:
            return user_inp_num(string)
    except ValueError:
        print('Try again! Put an integral value. ')
        return user_inp_num(string)

def conv_str(string, grid_str_len):
    if len(str(string)) == grid_str_len:
        return str(string)
    else:
        return ('0'*(grid_str_len-len(str(string)))+str(string))

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
            print(players[k].grid[i][j], end = '  ')
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
        temp = user_inp_num('The number to cut: ')
        if (temp > grid_elm):
            print('Enter a number from the grid')
            return user_inp_num_cut(grid_elm, grid_str_len, inputs)
        else:
            temp = str(temp)
            inputs.append(temp)
            temp = conv_str(temp, grid_str_len)
            return temp


class Player:
    def __init__(self, name, grid=[], horz=[], vert=[], md=0, od=0, score=0):
        self.grid = grid
        self.name = name
        self.horz = horz
        self.vert = vert
        self.md = md
        self.od = od
        self.score = score

print('Enter the size of the grid : ', end = '')
size = user_inp_num('')

grid_elm = size ** 2
grid_str_len = len(str(grid_elm))

player_num = user_inp_num('Enter the number of players : ')
players = [Player(input('Enter the name of player : ')) for k in range(player_num)]
for k in range(player_num):
    players[k].grid = [[] for i in range (size)]
    players[k].grid = make_grid(size, grid_elm, grid_str_len, players[k].grid)
    
inputs = []
game_over = False
print('\nPlay\n')
while(game_over == False):
    for k in range(player_num):
        print('\n',players[k].name,"'s turn\nNo need to put 0 before numbers ;) ")
        show_grid(k, 'Grid of '+players[k].name+"'s right now : ")
        temp1 = user_inp_num_cut(grid_elm, grid_str_len, inputs)
        for l in range(player_num):
            for i in range(size):
                if temp1 in players[l].grid[i]:
                    temp2 = players[l].grid[i].index(temp1)
                    players[l].grid[i][temp2] = '0'*grid_str_len
                    
                    if i not in players[l].horz:
                        if len(set(players[l].grid[i])) == 1:
                            players[l].score += 1
                            players[l].horz.append(i)#THIS IS CHANGING THE  ATTRIBUTE VALUE OF THE CLASS INSTEAD OF THE INSTANCE ATTRIBUTE
                            #SEE MORE ABOUT ON THIS TOPIC IN THE LINKS ABOVE TO STACK OVERFLOW.
                            
                    if temp2 not in players[l].vert:
                        if check_column(size-1, temp2, l) == True:
                            players[l].score += 1
                            players[l].vert.append(temp2)#THIS IS CHANGING THE  ATTRIBUTE VALUE OF THE CLASS INSTEAD OF THE INSTANCE ATTRIBUTE
                            #SEE MORE ABOUT ON THIS TOPIC IN THE LINKS ABOVE TO STACK OVERFLOW.
                                  
                    if players[l].md == 0:
                        if check_main_diagonal(0, l) == True:
                            players[l].score += 1
                            players[l].md += 1
                                  
                    if players[l].od == 0:

                        if check_other_diagonal(size-1, l) == True:
                            players[l].score += 1
                            players[l].od += 1


                    #a check
                    print(players[l].grid)
                    print(players[l].horz)
                    print(players[l].vert)
                    print(check_column(size-1, temp2, l))
                    print(players[l].md)
                    print(players[l].od)
                    print(players[l].score)


                    
                    
            print('The score of', players[l].name, 'is', players[l].score)
            if players[l].score >= size:
                game_over = True
                    
        show_grid(k, '\nAfter cutting the input, '+players[k].name+"'s grid : ")
        if game_over == True:
            break
                
#Android.ttsSpeak('You won')
print('These were the values cut during the whole session : ', inputs)
'''inputs.insert(0, 'These were the values cut during the whole session')
for i in range(len(inputs)):
    Android.ttsSpeak(inputs[i])'''

    
'''Version 1.2 changes:
1. Some aesthetic changes.
2. Changed things to definitions as much as possible for impoving readability.'''
'''Version 1.3 changes:
1. Added voice assistance supported in android versions of python(QPython3L).'''
