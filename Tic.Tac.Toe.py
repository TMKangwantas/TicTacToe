#Thanathip Kangwantas
#CS100-H03, Fall
#December 8, 2014

#################################################
#Triplets
#################################################
triplets = []
x = 0
while x < 1:
    for col in range (3):
        rowWin = []
        for row in range(3):
            rowWin.append([row,col])
        triplets.append(rowWin)
    x += 1
while x < 2:
    for col in range(3):
        colWin = []
        for row in range(3):
            colWin.append([col,row])
        triplets.append(colWin)
    x+=1
while x < 3:
    diagWin1 = []
    for colRows in range (3):
        diagWin1.append([colRows, colRows])
    diagWin2 = []
    for colRows in range(3):
        diagWin2.append([(2-colRows),colRows])
    triplets.append(diagWin1)
    triplets.append(diagWin2)
    x += 1
    
#################################################
#List to store moves and global variables
#################################################
    
check = []
playerX = []
playerO = []
xWinner = ''
oWinner = ''
drawn = ''

#################################################    
#Problem 1
#################################################

def isDraw(triplets):
    xWin(triplets)
    oWin(triplets)
    global drawn
    if xWinner == True:
        drawn = False
        return False
    if oWinner == True:
        drawn = False
        return False
    else:
        drawn = True
        return True

#################################################
#Defining all the functions
#################################################
    
def drawGrid(t, size):
    #draw 2 horizontal lines
    t.width(5)
    for i in range(2):
        t.up()
        t.goto(0, size/3*(i+1))
        t.setheading(0)
        t.down()
        t.forward(size)
        t.backward(size)
    #draw 2 vertical lines
    for i in range(2):
        t.up()
        t.goto(size/3*(i+1), 0)
        t.setheading(90)
        t.down()
        t.forward(size)
        t.backward(size)

def drawXfromMid(t, side, midX, midY):
    import math
    #Length of X
    lengthX = math.sqrt(2*(side**2))
    t.up()
    t.goto(midX, midY)
    t.down()
    t.setheading(45)
    t.color('red')
    for i in range(2):
        t.forward(lengthX/2)
        t.backward(lengthX)
        t.forward(lengthX/2)
        t.left(90)

def tttDrawMove(t, colNum, rowNum, symbol, cellLength):
    cellX = colNum * cellLength
    cellY = cellLength * rowNum
    difference = 0.6
    if symbol == 'x':
        midX = cellX + cellLength/2
        midY = cellY + cellLength/2
        drawXfromMid(t, 0.6*cellLength, midX, midY)
    elif symbol == 'o':
        startX = cellX + cellLength/2
        startY = cellY + ((1 - difference)/2*cellLength)
        t.color('blue')
        t.up()
        t.goto(startX, startY)
        t.setheading(0)
        t.down()
        radius = (difference/2)*cellLength
        t.circle(radius)

def tttGetMove(t, name, symbol, cellLength):
    row = name + ', what row would you like to put your ' + symbol + "? "
    column = name + ', what column would you like to put your ' + symbol + "? "
    x = 0
    while x < 1:
        userInX = int(input(column))
        userInY = int(input(row))
        if (0 < userInX > 2) or (0 < userInY > 2):
            print("Sorry, that is not a valid coordinate point, please choose another one")
            continue
        elif [userInX,userInY] in check:
            print("Sorry that coordinate point is alread taken, please choose another one.")
            continue
        else:
            check.append([userInX,userInY])
            if symbol == 'x':
                playerX.append([userInX,userInY])
                tttDrawMove(t, userInX, userInY, 'x', cellLength)
            else:
                playerO.append([userInX,userInY])
                tttDrawMove(t, userInX, userInY, 'o', cellLength)
            x += 1

def xWin(triplets):
    global xWinner
    for sets in triplets:
        count = 0
        for coord in sets:
            if coord in playerX:
                count += 1
        if count == 3:
            xWinner = True
            break
        else:
            xWinner = False

def oWin(triplets):
    global oWinner
    for sets in triplets:
        count = 0
        for coord in sets:
            if coord in playerO:
                count += 1
        if count == 3:
            oWinner = True
            break
        else:
            oWinner = False

def isDraw2(triplets):
    xWin(triplets)
    oWin(triplets)
    global drawn
    if xWinner == True:
        drawn = False
    elif oWinner == True:
        drawn = False
    else:
        drawn = True
        
def winner(triplets, name1, name2):
    xWin(triplets)
    oWin(triplets)
    isDraw2(triplets)
    if xWinner == True:
        print('Congrats! ' + name1 + ' has won!')
        return True
    if oWinner == True:
        print('Congrats! ' + name2 + ' has won!')
        return True
    elif len(check) == 9:
        print('The game is a tie!')
        return True

def bestXMove(t, i, cellLength):
    import random
    move = ''
    corners = [[0,2],[2,0]]
    edges = [[1,0],[0,1],[1,2],[2,1]]
    if i == 0:
        move = [0,0]
        check.append(move)
        playerX.append(move)
        tttDrawMove(t, 0, 0, 'x', cellLength)
    elif i == 2:
        if [0,1] in playerO:
            check.append([2,0])
            playerX.append([2,0])
            tttDrawMove(t, 2, 0, 'x', cellLength)
        elif [1,0] in playerO:
            check.append([0,2])
            playerX.append([0,2])
            tttDrawMove(t, 0, 2, 'x', cellLength)
        elif [1,2] in playerO or [2,1] in playerO:
            check.append([1,1])
            playerX.append([1,1])
            tttDrawMove(t, 1, 1, 'x', cellLength)
        elif [2,2] not in check:
            check.append([2,2])
            playerX.append([2,2])
            tttDrawMove(t, 2, 2, 'x', cellLength)
        elif [0,2] not in check:
            check.append([0,2])
            playerX.append([0,2])
            tttDrawMove(t, 0, 2, 'x', cellLength)
    elif i == 4:
        if [1,1] in playerX and [2,2] not in check:
            check.append([2,2])
            playerX.append([2,2])
            tttDrawMove(t, 2, 2, 'x', cellLength)
            #Win by positive diagonal
        elif [0,2] in playerX and [0,1] not in check:
            check.append([0,1])
            playerX.append([0,1])
            tttDrawMove(t, 0, 1, 'x', cellLength)
        elif [1,1] not in check and [2,2] in playerX:
            check.append([1,1])
            playerX.append([1,1])
            tttDrawMove(t, 1, 1, 'x', cellLength)
            #Win by positive diagonal
        elif [2,0] in playerX and [1,0] not in check:
            check.append([1,0])
            playerX.append([1,0])
            tttDrawMove(t, 1, 0, 'x', cellLength)
        elif playerO[1] in corners:
            corners.remove(playerO[1])
            check.append(corners[0])
            playerX.append(corners[0])
            tttDrawMove(t, corners[0][0], corners[0][1], 'x', cellLength)
            #Next turn win by top row or left column
        elif [2,1] in playerO and [2,2] in playerO and [2,0] not in check:
            check.append([2,0])
            playerX.append([2,0])
            tttDrawMove(t, 2, 0, 'x', cellLength)
        elif [1,1] in playerO and [2,1] in playerO and [0,1] not in check:
            check.append([0,1])
            playerX.append([0,1])
            tttDrawMove(t, 0, 1, 'x', cellLength)
        elif [0,2] in playerX and [1,1] not in check:
            check.append([1,1])
            playerX.append([1,1])
            tttDrawMove(t, 1, 1, 'x', cellLength)
        elif [1,1] in playerO and [0,1] in playerO and [2,1] not in check:
            check.append([2,1])
            playerX.append([2,1])
            tttDrawMove(t, 2, 1, 'x', cellLength)
        elif [0,2] in playerO and [1,1] in playerO and [2,0] not in check:
            check.append([2,0])
            playerX.append([2,0])
            tttDrawMove(t, 2, 0, 'x', cellLength)
        elif [1,2] in playerO and [2,2] in playerO and [0,2] not in check:
            check.append([0,2])
            playerX.append([0,2])
            tttDrawMove(t, 0, 2, 'x', cellLength)
        elif [1,0] in playerO[1]:
            check.append([0,2])
            playerX.append([0,2])
            tttDrawMove(t, 0, 2, 'x', cellLength)
        elif [0,1] in playerO and [1,0] in playerO and [1,1] not in check:
            check.append([1,1])
            playerX.append([1,1])
            tttDrawMove(t, 1, 1, 'x', cellLength)
        elif [1,1] in playerO and [1,2] in playerO:
            check.append([1,0])
            playerX.append([1,0])
            tttDrawMove(t, 1, 0, 'x', cellLength)
        elif [1,1] in playerO and [2,1] in playerO:
            check.append([0,2])
            playerX.append([0,2])
            tttDrawMove(t, 0, 2, 'x', cellLength)
    elif i == 6:
        if [1,2] not in check and [0,2] in playerX and [2,2] in playerX:
            check.append([1,2])
            playerX.append([1,2])
            tttDrawMove(t, 1, 2, 'x', cellLength)
            #Win by top row
        elif [2,0] in playerX and [1,0] not in check:
            check.append([1,0])
            playerX.append([1,0])
            tttDrawMove(t, 1, 0, 'x', cellLength)
        elif [0,1] not in check and [0,2] in playerX:
            check.append([0,1])
            playerX.append([0,1])
            tttDrawMove(t, 0, 1, 'x', cellLength)
            #Win by left column
        elif [0,1] in playerX and [0,2] not in check:
            check.append([0,2])
            playerX.append([0,2])
            tttDrawMove(t, 0, 2, 'x', cellLength)
            #Win by left column
        elif [1,0] in playerX and [2,0] not in check:
            check.append([2,0])
            playerX.append([2,0])
            tttDrawMove(t, 2, 0, 'x', cellLength)
            #Win by bottom row
        elif [1,1] in playerX and [0,2] in playerX and [2,0] not in check:
            check.append([2,0])
            playerX.append([2,0])
            tttDrawMove(t, 2, 0, 'x', cellLength)
            #Win by negative diagonal
        elif [1,1] in playerX and [0,2] in playerX and [2,2] not in check:
            check.append([2,2])
            playerX.append([2,2])
            tttDrawMove(t, 2, 2, 'x', cellLength)
            #Win by positive diagonal
        elif [1,1] in playerX and [2,0] in playerX and [0,2] not in check:
            check.append([0,2])
            playerX.append([0,2])
            tttDrawMove(t, 0, 2, 'x', cellLength)
            #Win by negative diagonal
        elif [1,0] in playerX and [2,0] not in check:
            check.append([2,0])
            playerX.append([2,0])
            tttDrawMove(t, 2, 0, 'x', cellLength)
            #Win by bottom row
        elif [2,1] in playerX and [2,2] in playerX and [2,0] not in check:
            check.append([2,0])
            playerX.append([2,0])
            tttDrawMove(t, 2, 0, 'x', cellLength)
        elif [2,2] in playerX and [2,0] in playerX and [2,1] not in check:
            check.append([2,1])
            playerX.append([2,1])
            tttDrawMove(t, 2, 1, 'x', cellLength)
        elif [1,1] in playerO and [2,2] in playerO and [2,0] not in check:
            check.append([2,0])
            playerX.append([2,0])
            tttDrawMove(t, 2, 0, 'x', cellLength)
        elif [2,1] in playerX and [2,2] in playerX and [2,1] not in check:
            check.append([2,1])
            playerX.append([2,1])
            tttDrawMove(t, 2, 1, 'x' ,cellLength)
        elif [0,2] in playerO and [1,1] in playerO and [2,0] not in check:
            check.append([2,0])
            playerX.append([2,0])
            tttDrawMove(t, 2, 0, 'x', cellLength)
        elif [2,0] in playerO and [1,1] in playerO and [0,2] not in check:
            check.append([0,2])
            playerX.append([0,2])
            tttDrawMove(t, 0, 2, 'x', cellLength)
    elif i ==8:
        if [0,1] not in check:
            check.append([0,1])
            playerX.append([0,1])
            tttDrawMove(t, 0, 1, 'x', cellLength)
        elif [2,1] not in check:
            check.append([2,1])
            playerX.append([2,1])
            tttDrawMove(t, 2, 1, 'x', cellLength)
        elif [1,0] not in check:
            check.append([1,0])
            playerX.append([1,0])
            tttDrawMove(t, 1, 0, 'x', cellLength)
        elif [1,2] not in check:
            check.appen([1,2])
            playerX,append([1,2])
            tttDrawMove(t, 1, 2, 'x', cellLength)
def tttPlayGame(length):
    import turtle
    t = turtle.Turtle()
    cellLength = length/3
    drawGrid(t, length)
    global triplets
    global check
    global playerX
    global playerO
    while True:
        
#################################################
#Problem 2
#################################################
    
        player1 = input('Is Player 1, x, a computer or a human? ')
        player2 = input('Is Player 2, o, a computer or a human? ')
    
#################################################
#Problem 3
#################################################
        
        if player1 == 'human':
            p1 = input('Player 1, what is your name? ')
        if player2 == 'human':
            p2 = input('Player 2, what is your name? ')
        
#################################################
#Both players are human
#################################################
            
        pp1 = 'x'
        pp2 = 'o'
        if player1 == 'human' and player2 == 'human':
            for i in range(10):
                ####################################
                #Part of Problem 4 is 'winner'
                ####################################
                if winner(triplets, p1, p2) == True:
                    break
                if i%2 == 0:
                    tttGetMove(t, p1, pp1, cellLength)
                if i%2 == 1:
                    tttGetMove(t, p2, pp2, cellLength)

#################################################
#Player 1 is computer
#################################################

        if player1 == 'computer' and player2 == 'human':
            p1 = 'Computer'
            for i in range(10):
                
                ####################################
                #Part of Problem 4 is 'winner'
                ####################################
                
                if winner(triplets, p1, p2) == True:
                    break
                if i%2 == 0:
                    bestXMove(t, i, cellLength)
                if i%2 == 1:
                    tttGetMove(t, p2, pp2, cellLength)
                    
#################################################
#The other part of Problem 4 is below
#################################################
                  
        userIn = input('Would you like to play again or exit? ')
        if userIn == 'play again':
            del playerX[:]
            del playerO[:]
            del check[:]
            global oWinner
            global xWinner
            global drawn
            oWinner = ''
            xWinner = ''
            drawn = ''
            t.reset()
            drawGrid(t, length)
            continue
        if userIn == 'exit':
            exit()

print(tttPlayGame(300))
