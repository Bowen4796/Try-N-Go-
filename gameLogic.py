import random
import copy

# Print Board
print("Try-N-Go\n---------------------------------------")

claimedTriangles = [
    [0],
    [0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
]

board = [
    [0],
    [0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
]


# Make Board
rows = 6
x = 0
y = rows*3


def printBoard(x, y):
    for i in range(rows):
        print(" " * y, end="")
        print(board[x])
        y -= 3
        x += 1

# User Input changes2 board


global p, turnCounter
turnCounter = 0
p = 0


def inputMove(board, botMove = False):
    # Player 0
    global r, c
    while True:
        # CPU chooses a tile
        r = aiMove[0]
        c = aiMove[1]

        # Updates tile and catch exceptions
        try:
            if board[r][c] == 0:
                board[r][c] = (2)
                print(f"CPU Input: [{r+1}, {c+1}]")
            else:
                raise ValueError
        except ValueError:
            pass
        except IndexError:
            pass

        # When an empty spot is chosen and updated, break
        else:
            return (r, c)


# Player Points Data and Who to assign points
assignTo = 0
pointsA = 0
pointsB = 0

# Takes in value of a triangle and the current player and gives points if claimed choice is yes


def claimTriangle(pointVal):
    if assignTo == 1:
        global pointsA
        pointsA += pointVal
    elif assignTo == 2:
        global pointsB
        pointsB += pointVal 
    return 1

# Checks completed rightside down small triangles, if player claims then it will empty the tiles


def checkForT1A(p, board, playerTurn = False):
    print("testing")
    a = 0
    b = 0
    try:
        # For each row
        while a < len(board):
            b = 0
            # For each column
            while b < len(board[a]):
                if (board[a][b] and board[a+1][b] and board[a+1][b+1] and board[a+1][b+2]) != 0:
                    print(
                        f"Triangle [{a+1},{b+1}] [{a+2},{b+1}] [{a+2},{b+2}] [{a+2},{b+3}] Filled")
                    list = [board[a][b], board[a+1][b],
                            board[a+1][b+1], board[a+1][b+2]]
                    if list.count(1) > list.count(2) and playerTurn:
                        print("Player 1 winning")
                        global assignTo
                        assignTo = 1
                        if claimTriangle(2) == 1:
                            board[a][b] = board[a+1][b] = board[a +
                                                                1][b+1] = board[a+1][b+2] = 0
                            return True
                    elif list.count(2) > list.count(1):
                        assignTo = 2
                        if claimTriangle(2) == 1:
                            print("ai claims")
                            board[a][b] = board[a+1][b] = board[a +
                                                                1][b+1] = board[a+1][b+2] = 0
                            return False
                        else:
                            print("WHAT?")

                b += 2
            a += 1
    except:
        pass

# Checks completed upside down small triangles, if player claims then it will empty the tiles


def checkForT1B(p, board, playerTurn = False):
    a = 3
    b = 3
    try:
        while a < (len(board)):
            b = 3
            while b < (len(board[a])-2):
                if (board[a][b] and board[a-1][b] and board[a-1][b-1] and board[a-1][b-2]) != 0:
                    print(
                        f"Triangle [{a},{b-1}] [{a},{b}] [{a},{b+1}] [{a+1},{b+1}] Filled")
                    list = [board[a][b], board[a-1][b],
                            board[a-1][b-1], board[a-1][b-2]]
                    if list.count(1) > list.count(2) and playerTurn:
                        print("Player 1:")
                        global assignTo
                        assignTo = 1
                        if claimTriangle(2) == 1:
                            board[a][b] = board[a-1][b] = board[a -
                                                                1][b-1] = board[a-1][b-2] = 0
                            return True
                    elif list.count(2) > list.count(1):
                        print("Player 2:")
                        assignTo = 2
                        if claimTriangle(2) == 1:
                            print("ai claims")
                            board[a][b] = board[a-1][b] = board[a -
                                                                1][b-1] = board[a-1][b-2] = 0
                            return False
                b += 2
            a += 1
    except:
        pass

# Checks completed rightside down big triangles, if player claims then it will empty the tiles


def checkForT2A(p, board, playerTurn = False):
    a = 0
    b = 0
    while a < (len(board)-2):
        b = 0
        while b < len(board[a]):
            if (board[a][b] and board[a+1][b] and board[a+1][b+1] and board[a+1][b+2] and board[a+2][b] and board[a+2][b+1] and board[a+2][b+2] and board[a+2][b+3] and board[a+2][b+4]) != 0:
                print(
                    f"Triangle [{a+1},{b+1}] [{a+2},{b+1}] [{a+2},{b+2}] [{a+2},{b+3}] [{a+3},{b+1}] [{a+3},{b+2}] [{a+3},{b+3}] [{a+3},{b+4}] [{a+3},{b+5}] Filled")
                list = [board[a][b], board[a+1][b], board[a+1][b+1], board[a+1][b+2], board[a+2]
                        [b], board[a+2][b+1], board[a+2][b+2], board[a+2][b+3], board[a+2][b+4]]
                if list.count(1) > list.count(2) and playerTurn:
                    print("Player 1:")
                    global assignTo
                    assignTo = 1
                    if claimTriangle(5) == 1:
                        board[a][b] = board[a+1][b] = board[a+1][b+1] = board[a+1][b+2] = board[a +
                                                                                                2][b] = board[a+2][b+1] = board[a+2][b+2] = board[a+2][b+3] = board[a+2][b+4] = 0
                        return True
                elif list.count(2) > list.count(1):
                    print("Player 2:")
                    assignTo = 2
                    if claimTriangle(5) == 1:
                        print("ai claims")
                        board[a][b] = board[a+1][b] = board[a+1][b+1] = board[a+1][b+2] = board[a +
                                                                                                2][b] = board[a+2][b+1] = board[a+2][b+2] = board[a+2][b+3] = board[a+2][b+4] = 0
                        return False
            b += 2
        a += 1

# Checks completed upside down big triangles, if player claims then it will empty the tiles


def checkForT2B(p, board, playerTurn = False):
    if (board[3][5] and board[3][4] and board[3][3] and board[3][2] and board[3][1] and board[4][4] and board[4][5] and board[4][3] and board[5][5]) != 0:
        print(
            "Triangle [4,2] [4,3] [4,4] [4,5] [4,6] [5,4] [5,5] [5,6] [6,6] Filled")
        list = [board[3][5], board[3][4], board[3][3], board[3][2],
                board[3][1], board[4][4], board[4][5], board[4][3], board[5][5]]
        if list.count(1) > list.count(2) and playerTurn:
            print("Player 1:")
            global assignTo
            assignTo = 1
            if claimTriangle(5) == 1:
                board[3][5] = board[3][4] = board[3][3] = board[3][2] = board[
                    3][1] = board[4][4] = board[4][5] = board[4][3] = board[5][5] = 0
                return True
        elif list.count(2) > list.count(1):
            print("Player 2:")
            assignTo = 2
            if claimTriangle(5) == 1:
                print("ai claims")
                board[3][5] = board[3][4] = board[3][3] = board[3][2] = board[
                    3][1] = board[4][4] = board[4][5] = board[4][3] = board[5][5] = 0
                return False

# Starts game


def evaluate():
    evalList = []
    majList = []
    a = 0
    b = 0
    majA1 = 0
    majA2 = 0
    majB1 = 0
    majB2 = 0
    while a < len(board):
        b = 0
        try:
            while b < len(board[a]):
                majList = [board[a][b], board[a+1][b],
                           board[a+1][b+1], board[a+1][b+2]]
                if majList.count(1) >= 3:
                    majA1 += 1
                if majList.count(2) >= 3:
                    majA2 += 1
                evalList.append(board[a][b])
                evalList.append(board[a+1][b])
                evalList.append(board[a+1][b+1])
                evalList.append(board[a+1][b+2])
                b += 2
        except:
            pass
        a += 1
    a = 3
    b = 3
    while a < (len(board)):
        b = 3
        try:
            while b < (len(board[a])-2):
                majList = [board[a][b], board[a-1][b],
                           board[a-1][b-1], board[a-1][b-2]]
                if majList.count(1) >= 3:
                    majA1 += 1
                if majList.count(2) >= 3:
                    majA2 += 1
                evalList.append(board[a][b])
                evalList.append(board[a-1][b])
                evalList.append(board[a-1][b-1])
                evalList.append(board[a-1][b-2])
                b += 2
        except:
            pass
        a += 1
    a = 0
    b = 0
    while a < (len(board)-2):
        b = 0
        try:
            while b < len(board[a]):
                majList = [board[a][b], board[a+1][b], board[a+1][b+1], board[a+1][b+2], board[a+2]
                           [b], board[a+2][b+1], board[a+2][b+2], board[a+2][b+3], board[a+2][b+4]]
                if majList.count(1) >= 5:
                    majB1 += 1
                if majList.count(2) >= 5:
                    majB2 += 1
                evalList.append(board[a][b])
                evalList.append(board[a+1][b])
                evalList.append(board[a+1][b+1])
                evalList.append(board[a+1][b+2])
                evalList.append(board[a+2][b])
                evalList.append(board[a+2][b+1])
                evalList.append(board[a+2][b+2])
                evalList.append(board[a+2][b+3])
                evalList.append(board[a+2][b+4])
                b += 2
        except:
            pass
        a += 1
    majList = [board[3][5], board[3][4], board[3][3], board[3][2],
               board[3][1], board[4][4], board[4][5], board[4][3], board[5][5]]
    if majList.count(1) >= 5:
        majB1 += 1
    if majList.count(2) >= 5:
        majB2 += 1
    evalList.append(board[3][5])
    evalList.append(board[3][4])
    evalList.append(board[3][3])
    evalList.append(board[3][2])
    evalList.append(board[3][1])
    evalList.append(board[4][4])
    evalList.append(board[4][5])
    evalList.append(board[4][3])
    evalList.append(board[5][5])
    pos1 = evalList.count(1)
    pos2 = evalList.count(2)
    return pos1, pos2, majA1, majA2, majB1, majB2


def evalTest(board):
    evalList = []
    majList = []
    a = 0
    b = 0
    majA1 = 0
    majA2 = 0
    majB1 = 0
    majB2 = 0
    while a < len(board):
        b = 0
        try:
            while b < len(board[a]):
                majList = [board[a][b], board[a+1][b],
                           board[a+1][b+1], board[a+1][b+2]]
                if majList.count(1) >= 3:
                    majA1 += 1
                if majList.count(1) == 4:
                    majA1 += 1
                if majList.count(2) >= 3:
                    majA2 += 1
                if majList.count(2) == 4:
                    majA2 += 1
                evalList.append(board[a][b])
                evalList.append(board[a+1][b])
                evalList.append(board[a+1][b+1])
                evalList.append(board[a+1][b+2])
                b += 2
        except:
            pass
        a += 1
    a = 3
    b = 3
    while a < (len(board)):
        b = 3
        try:
            while b < (len(board[a])-2):
                majList = [board[a][b], board[a-1][b],
                           board[a-1][b-1], board[a-1][b-2]]
                if majList.count(1) >= 3:
                    majA1 += 1
                if majList.count(1) == 4:
                    majA1 += 1
                if majList.count(2) >= 3:
                    majA2 += 1
                if majList.count(2) == 4:
                    majA2 += 1
                evalList.append(board[a][b])
                evalList.append(board[a-1][b])
                evalList.append(board[a-1][b-1])
                evalList.append(board[a-1][b-2])
                b += 2
        except:
            pass
        a += 1
    a = 0
    b = 0
    while a < (len(board)-2):
        b = 0
        try:
            while b < len(board[a]):
                majList = [board[a][b], board[a+1][b], board[a+1][b+1], board[a+1][b+2], board[a+2]
                           [b], board[a+2][b+1], board[a+2][b+2], board[a+2][b+3], board[a+2][b+4]]
                if majList.count(1) >= 5:
                    majB1 += 1
                if majList.count(2) >= 5:
                    majB2 += 1
                evalList.append(board[a][b])
                evalList.append(board[a+1][b])
                evalList.append(board[a+1][b+1])
                evalList.append(board[a+1][b+2])
                evalList.append(board[a+2][b])
                evalList.append(board[a+2][b+1])
                evalList.append(board[a+2][b+2])
                evalList.append(board[a+2][b+3])
                evalList.append(board[a+2][b+4])
                b += 2
        except:
            pass
        a += 1
    majList = [board[3][5], board[3][4], board[3][3], board[3][2],
               board[3][1], board[4][4], board[4][5], board[4][3], board[5][5]]
    if majList.count(1) >= 5:
        majB1 += 1
    if majList.count(2) >= 5:
        majB2 += 1
    evalList.append(board[3][5])
    evalList.append(board[3][4])
    evalList.append(board[3][3])
    evalList.append(board[3][2])
    evalList.append(board[3][1])
    evalList.append(board[4][4])
    evalList.append(board[4][5])
    evalList.append(board[4][3])
    evalList.append(board[5][5])
    pos1 = evalList.count(1)
    pos2 = evalList.count(2)
    return pos1, pos2, majA1, majA2, majB1, majB2


def minimax():
    global boardTest
    global moveList
    moveList = []
    boardTest = copy.deepcopy(board)
    x = 0
    x1 = 0
    tree = []
    z = 0
    while x < 6:
        x1 = 0
        y = 0
        while (y <= (x*2)):
            boardTest = copy.deepcopy(board)
            try:
                while boardTest[x][y] != 0:
                    y += 1
                boardTest[x][y] = 2
                x1 = 0
                layer2 = []
                while x1 < 6:
                    y1 = 0
                    while (y1 <= (x1 * 2)):
                        boardTest1 = copy.deepcopy(boardTest)
                        try:
                            while boardTest1[x1][y1] != 0:
                                y1 += 1
                            boardTest1[x1][y1] = 1
                            x2 = 0
                            layer3 = []
                            while x2 < 6:
                                y2 = 0
                                while (y2 <= (x2 * 2)):
                                    boardTest2 = copy.deepcopy(boardTest1)
                                    try:
                                        while boardTest2[x2][y2] != 0:
                                            y2 += 1
                                        boardTest2[x2][y2] = 2
                                        layer3.append(boardScore(
                                            evalTest(boardTest2)))
                                    except:
                                        pass
                                    y2 += 1
                                x2 += 1
                            layer2.append(layer3)
                        except:
                            pass
                        y1 += 1
                    x1 += 1
                layer1 = [layer2, [x, y]]
                tree.append(layer1)
            except:
                pass
            y += 1
        x += 1
    a = 0
    while a < len(tree):
        b = 0
        while b < len(tree[a][0]):
            tree[a][0][b] = max(tree[a][0][b])
            b += 1
        a += 1
    a = 0
    while a < len(tree):
        tree[a][0] = min(tree[a][0])
        a += 1
    a = 0
    maxVal = -99999999999
    while a < len(tree):
        if tree[a][0] > maxVal:
            maxVal = tree[a][0]
        a += 1
    for i in tree:
        if i[0] == maxVal:
            moveList.append(i[1])
    global aiMove
    aiMove = random.choice(moveList)


def boardScore(eval):
    pointsWeight = 50
    positionWeight = 1
    bWeight = 40
    aWeight = 20
    pos1, pos2, majA1, majA2, majB1, majB2 = eval
    score = (((pointsB * pointsWeight) + (pos2 * positionWeight) + (majB2 * bWeight) + (majA2 * aWeight)) -
             ((pointsA * pointsWeight) + (pos1 * positionWeight) + (majB1 * bWeight) + (majA1 * aWeight)))
    return score


def playGame(botMove=False):
    global turnCounter

    for i in range(1):

        # Make board
       # printBoard(x, y)

        # Store the current turn
        p =   2
        if botMove:
            minimax()


        # Print that is a player's turn
        print(f"Turn {turnCounter+1}")
        print(f"Player {p+1}'s Move")
        turnCounter += 1

        # Input moves and check for triangles and give claim options if possible.
        inputMove(board)
        checkForT1A(p, board)
        checkForT1B(p, board)
        checkForT2A(p, board)
        checkForT2B(p, board)
        printBoard(x, y)


def checkforTriangles(claimedTiles, targetTriangle=None, playerTurn = False):
    global turnCounter
    i = 0
    if targetTriangle == 4:
        if checkForT1A(p, claimedTiles, playerTurn):
            i = 1

        if checkForT1B(p, claimedTiles, playerTurn):
            i = 1

    if targetTriangle == 9:
        if checkForT2A(p, claimedTiles, playerTurn):
            i = 1

        if checkForT2B(p, claimedTiles, playerTurn):
            i = 1

    if targetTriangle == None:
        if checkForT1A(p, claimedTiles, playerTurn):
            i = 1
        if checkForT1B(p, claimedTiles, playerTurn):
            i = 1
        if checkForT2A(p, claimedTiles, playerTurn):
            i = 1
        if checkForT2B(p, claimedTiles, playerTurn):
            i = 1

    # Display current amount of point and update turnCounter
    print(f"P1 Points: {pointsA}\nP2 Points: {pointsB}")
    print("\n---------------------------------------")

    # Shows that a triangle has been claimed
    if i == 1:
        return True
