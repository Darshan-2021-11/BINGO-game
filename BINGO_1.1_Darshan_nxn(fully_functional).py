import random

#Initialising setup of grid by taking user input
def user_inp(string):
    try:
        size = int(input(string))
        if size > 0:
            return size
        else:
            return user_inp(string)
    except ValueError:
        print('Try again! Put an integral value. ')
        return user_inp(string)
    
#Making grid main rows with ugly brakets and inverted commas
#Step 1: All the elements
size = user_inp('Enter the size of the grid: ')
grid = size ** 2
temp1 = [[] for i in range (size)]

gridn = len(str(grid))
temp2 = [str(i) if len(str(i)) == gridn else ('0'*(gridn-len(str(i)))+str(i)) for i in range (1, grid+1)]
random.shuffle(temp2)
#Step 2: Element in different sets
count = 0
for i in range(size):
    for j in range(count*size, (count+1)*size):
        temp1[i].append(temp2[j])
    count += 1

#For showing the grid without ugly brackets and inverted commas
def show_rows():
    for i in range(size):
        for j in range(size):
            print(temp1[i][j], end = '  ')
        print()

#For checking column
def cond_equal_col(num1, num2):
    if (num1 > 1 and temp1[num1][num2] == temp1[num1-1][num2]):
        return cond_equal_col(num1-1, num2)
    elif ((num1 == 1 and temp1[1][num2] == temp1[0][num2]) or num1 == 0):
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

# To not give score to the one already given
horz = []
vert = []
md = 0
od = 0
#The real game code
score = 0

print('Play\nNo need to put 0 before numbers ;) ')
while (score < size):
    #showing grid
    show_rows()
    
    #Taking user input
    temp = str(user_inp('The number to cut: '))
    tl = len(temp)
    if tl < gridn:
        temp = '0'*(gridn - tl) + temp
    if int(temp) > grid:
        print('Enter a number from the grid')
        continue
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
            if temp3 not in vert:
                cond2 = cond_equal_col(size-1, temp3)
                if cond2 == True:
                    score += 1
                    vert.append(temp3)
  
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
            
if score >= size:
    print('BINGO! You won!')
