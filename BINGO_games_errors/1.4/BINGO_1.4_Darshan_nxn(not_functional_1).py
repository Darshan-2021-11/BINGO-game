
"""
GO TO THE LINE NO.60,61, 63,64 TO SEE THE ERROR

1. ALWAYS USE BRACKETS IN EVERY CONDITION BETWEEN 'AND' OR 'OR'
2. ALSO IN TRY EXCEPT BLOCK, ELSE CANNOT BE USED IN THIS EXAMPLE
    (I.E. DO NOT HOPE ALL THE EXCEPTIONS WILL BE HANDLED HERE!)
    ''
    def user_inp(string):
        try:
            size = int(input(string))
            return size
        else:
            print('Try again! Put an integral value. ')
            return user_inp(string)
    ''
    THIS MUST HAVE SOME VALUE LIKE VALUEERROR OR SOMETHING WITH EXCEPT
"""


import random
# Copyright (C) 2012, Hariharan Srinath, Robbie Matthews
#from androidhelper import Android
#Android = Android()
#Note androidhelper module is only for users in android

#Initialising setup of grid by taking user input

def player_info(player, no_of_players):
    for i in range(no_of_players):
        temp = input('Enter the player name : ')
        player[str(temp)] = {'horz' : [], 'vert' : [], 'md' : 0,
                             'od' : 0, 'score' : 0}
        (player[str(temp)])['temp1'] = make_grid(size, grid, gridn)

def user_inp(string):
    try:
        size = int(input(string))
        return size
    except ValueError:
        print('Try again! Put an integral value. ')
        return user_inp(string)

def enter_size():
    print('Enter the size of the grid : ', end = '')
    #Android.ttsSpeak('Enter the size of the grid')
    size = user_inp('')
    return size

#Making grid main rows with ugly brakets and inverted commas
def make_grid(size, grid, gridn, temp1 = [i for i in range(size)]):
    #Step 1: All the elements
    temp2 = [str(i) if len(str(i)) == gridn else ('0'*(gridn-len(str(i)))+str(i)) for i in range (1, grid+1)]
    random.shuffle(temp2)
    #Step 2: Element in different sets
    count = 0
    for i in range(size):
        for j in range(count*size, (count+1)*size):
            temp1[i].append(temp2[j])
        count += 1
    return temp1

#For showing the grid without ugly brackets and inverted commas
def show_rows(message = None):
    if message:
        print(str(message))
    for i in range(size):
        for j in range(size):
            print(temp1[i][j], end = '  ')
        print()

#For checking column
def cond_equal_col(num1, num2):
    if (num1 > 1 and temp1[num1][num2] == temp1[num1-1][num2]):#THIS IS WRONG ALWAYS USE BRACKETS IN EVERY CONDITION BETWEEN 'AND' OR 'OR'
    #LIKE THIS if( (num1 > 1) and (temp1[num1][num2] == temp1[num1-1][num2]) ):  instead of if (num1 > 1 and temp1[num1][num2] == temp1[num1-1][num2]):
        return cond_equal_col(num1-1, num2)
    elif ((num1 == 1 and temp1[1][num2] == temp1[0][num2]) or num1 == 0):#THIS IS WRONG ALWAYS USE BRACKETS IN EVERY CONDITION BETWEEN 'AND' OR 'OR'
    #LIKE THIS elif( ((num1 == 1) and (temp1[num1][num2] == temp1[num1-1][num2])) or (num == 0) ):  instead of elif ((num1 == 1 and temp1[1][num2] == temp1[0][num2]) or num1 == 0):
        return True
    else:
        return False

#For checking main diagonal
def cond_equal_diar(i):
    if i < size-1:
        if temp1[i][i] == temp1[i+1][i+1]:
            return cond_equal_diar(i+1)
        else:
            return False
    elif i == size-1:
        return True

#For cheecking the other diagonal
def cond_equal_dial(i):
    if i > 0:
        if temp1[(size-1)-i][i] == temp1[(size-1)-(i-1)][i-1]:
            return cond_equal_dial(i-1)
        else:
            return False
    elif i == 0:
        return True

def check_score():
    if score >= size:
        print('You won!')
        #Android.ttsSpeak('You won')
        print('These were the values cut during the whole session : ', inputs)
        inputs.insert(0, 'These were the values cut during the whole session')
        #for i in range(len(inputs)):
            #Android.ttsSpeak(inputs[i])


def game():
    print('Play\nNo need to put 0 before numbers ;) ')
    #showing grid
    show_rows('Grid right now : ')
    Android.ttsSpeak('Enter the number to cut: ')
    temp = str(user_inp('The number to cut: '))
    inputs.append(temp)
    tl = len(temp)
    if tl < gridn:
        temp = '0'*(gridn - tl) + temp
    if int(temp) > grid or int(temp) <= 0:
        print('Enter a number from the grid')
        return game()
    else:
        #Replacing the given number
        for i in range(size):
            if temp in (temp1[i]):
                temp3 = temp1[i].index(temp)
                (temp1[i])[temp3] = '0'*gridn

        #Checking the condition if to increase score in horizontal or rows
                if i not in horz:
                    cond1 = set(temp1[i])
                    if len(cond1) == 1:
                        score += 1
                        horz.append(i)
                    if temp not in vert:
                        cond2 = cond_equal_col(size-1, temp3)
                        if cond2 == True:
                            score += 1
                            vert.append(i)
        # Still room for impovement in checking of diagonal, task for reader ;),
            if md == 0:
                cond3 = cond_equal_diar(0)
                if cond3 == True:
                    score += 1
                    md += 1
            if od == 0:
                cond4 = cond_equal_dial(size-1)
                if cond4 == True:
                    score += 1
                    od += 1
        print('Score: ', score)
        show_rows('After cutting the input : ')
        check_score()




















size = enter_size()
player = {}
inputs = []


grid = size ** 2
gridn = len(str(grid))
no_of_players = user_inp('Enter the number of players : ')
player_info(player, no_of_players)
game_over = False

while(game_over == False):
    game()




'''Version 1.2 changes:
1. Some aesthetic changes.
2. Changed things to definitions as much as possible for impoving readability.'''
'''Version 1.3 changes:
1. Added voice assistance supported in android versions of python(QPython3L).'''
