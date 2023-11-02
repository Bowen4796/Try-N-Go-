import pygame
import copy
import gameLogic

# pygame setup
pygame.init()
running = True

# element sizes
SCREEN_HEIGHT = 950
SCREEN_WIDTH = 1425

BOARD_HEIGHT = (7/8) * SCREEN_HEIGHT
BOARD_WIDTH = BOARD_HEIGHT * 1.1495

TRIANGLE_HEIGHT = BOARD_HEIGHT/6
TRIANGLE_WIDTH = BOARD_WIDTH/6

CLAIM_HEIGHT = 178
CLAIM_WIDTH = 326

pygame.display.set_caption('TRY-N-GO!')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# instantiate images
boardRawImage = pygame.image.load("assets/board.png")
boardImage = pygame.transform.scale(boardRawImage, (BOARD_WIDTH, BOARD_HEIGHT))

marbleImage = pygame.image.load("assets/marble.png")


claimButtonRawImage = pygame.image.load("assets/claimButton.png")
claimButtonImage = pygame.transform.scale(
    claimButtonRawImage, (CLAIM_WIDTH, CLAIM_HEIGHT))

selectButtonRawImage = pygame.image.load("assets/selectButton.png")
selectButtonImage = pygame.transform.scale(
    selectButtonRawImage, (CLAIM_WIDTH, CLAIM_HEIGHT))

# store image properties
screen_rect = screen.get_rect()

board = boardImage.get_rect()
marble = marbleImage.get_rect()

claimButton = claimButtonImage.get_rect()

selectButton = selectButtonImage.get_rect()


# centering board
center_x = screen_rect.centerx
center_y = screen_rect.centery
board.centerx = center_x
board.centery = center_y

# Setting claim/selectButton in top right corner
claimButton.x = SCREEN_WIDTH - CLAIM_WIDTH
claimButton.y = 0

selectButton.x = SCREEN_WIDTH - CLAIM_WIDTH
selectButton.y = 0 + CLAIM_HEIGHT

# variable for making empty spots
transparent_color = "white"
tileWidthInterval = board.width/6
tileHeightInterval = board.height/6

vertices = [(board.bottomleft), (board.left + tileWidthInterval, board.bottom),
            (board.left + tileWidthInterval/2, board.bottom - tileHeightInterval)]

tileDict = {}
state = "white"


def fixCoords(r, c=False):
    if r == 5:
        r = 0

    elif r == 4:
        r = 1

    elif r == 3:
        r = 2

    elif r == 2:
        r = 3

    elif r == 1:
        r = 4

    elif r == 0:
        r = 5

    if c:
        if r == 0:
            r = 5

        elif r == 1:
            r = 4

        elif r == 2:
            r = 3

        elif r == 3:
            r = 2

        elif r == 4:
            r = 1

        elif r == 5:
            r = 0
    return r


class tiles():
    def __init__(self, object, position, vertices, state):
        self.object = object
        self.position = position
        self.state = state
        self.vertices = vertices
        pos = list(position)
        pos[1] -= 1
        position = tuple(pos)

        if tileDict.get(position) == None:
            state = "white"
        else:
            state = tileDict[position]['state']

        if state == 'white':
            numRep = 0
        elif state == "red":
            numRep = 1
        elif state == "blue":
            numRep = 2

        listy = list(position)

        fixCoords(listy[0])

        pygame.draw.polygon(screen, state, vertices)
        tileDict[position] = {'vertices': copy.deepcopy(
            vertices), 'position': position, 'state': state, 'numRep': numRep}


def makeRow(row, pair, neededLoops):
    global vertices
    global column
    # triangle 1
    if row == 0 and pair == 0:
        vertices = [(board.bottomleft), (board.left + tileWidthInterval, board.bottom),
                    (board.left + tileWidthInterval/2, board.bottom - tileHeightInterval)]

        column = 1
        tiles(pygame.draw.polygon(screen, state, vertices),
              (row, column), vertices, "white")
        pygame.draw.lines(screen, "black", True, vertices, 2)

    # starting on new row
    elif row >= 1 and pair == 0:
        # For rows 1 and 4
        if (row % 3) == 1:
            listy1 = list(vertices[0])
            listy2 = list(vertices[1])
            listy3 = list(vertices[2])

            listy1[0] -= (neededLoops - .5) * tileWidthInterval
            listy1[1] -= tileHeightInterval

            listy2[0] -= (neededLoops - .5) * tileWidthInterval
            listy2[1] -= tileHeightInterval

            listy3[0] -= (neededLoops - .5) * tileWidthInterval
            listy3[1] -= tileHeightInterval

            vertices[0] = tuple(listy1)
            vertices[1] = tuple(listy2)
            vertices[2] = tuple(listy3)

            column = 1
            tiles(pygame.draw.polygon(screen, transparent_color,
                  vertices), (row, column), vertices, "white")
            pygame.draw.lines(screen, "black", True, vertices, 2)

        # For rows 2 and 5
        elif (row % 3) == 2:
            listy1 = list(vertices[0])
            listy2 = list(vertices[1])
            listy3 = list(vertices[2])

            listy1[0] -= tileWidthInterval * 3
            listy1[1] -= tileHeightInterval * 2

            listy2[0] -= tileWidthInterval * 4.5
            listy2[1] -= tileHeightInterval

            listy3[0] -= tileWidthInterval * 3

            vertices[0] = tuple(listy1)
            vertices[1] = tuple(listy2)
            vertices[2] = tuple(listy3)

            column = 1
            tiles(pygame.draw.polygon(screen, transparent_color,
                  vertices), (row, column), vertices, "white")
            pygame.draw.lines(screen, "black", True, vertices, 2)

        # For row 3
        else:
            listy1 = list(vertices[0])
            listy2 = list(vertices[1])
            listy3 = list(vertices[2])

            listy1[0] -= tileWidthInterval * 3

            listy2[0] -= tileWidthInterval * 1.5
            listy2[1] -= tileHeightInterval

            listy3[0] -= tileWidthInterval * 3
            listy3[1] -= tileHeightInterval * 2

            vertices[0] = tuple(listy1)
            vertices[1] = tuple(listy2)
            vertices[2] = tuple(listy3)

            column = 1
            tiles(pygame.draw.polygon(screen, transparent_color,
                  vertices), (row, column), vertices, "white")
            pygame.draw.lines(screen, "black", True, vertices, 2)

        column = 1
    else:
        column += 1
        tiles(pygame.draw.polygon(screen, transparent_color,
              vertices), (row, column), vertices, "white")
        pygame.draw.lines(screen, "black", True, vertices, 2)

    # triangle 2
    # For rows 0 or 3
    if row == 0 or row == 3:
        column += 1
        if pair == 0 or pair == 3:
            point = 0
            listy = list(vertices[0])
        elif pair == 1 or pair == 4:
            point = 1
            listy = list(vertices[1])
        else:
            point = 2
            listy = list(vertices[2])
        listy[0] += tileWidthInterval*1.5
        listy[1] -= tileHeightInterval
        vertices[point] = tuple(listy)

        tiles(pygame.draw.polygon(screen, transparent_color,
              vertices), (row, column), vertices, "white")
        pygame.draw.lines(screen, "black", True, vertices, 2)

        # setting triangle 3
        if pair == 0 or pair == 3:
            point = 2
            listy = list(vertices[2])
        elif pair == 1 or pair == 4:
            point = 0
            listy = list(vertices[0])
        else:
            point = 1
            listy = list(vertices[1])
        listy[0] += tileWidthInterval*1.5
        listy[1] += tileHeightInterval
        vertices[point] = tuple(listy)

    # For rows 1 or 4
    if row == 1 or row == 4:
        column += 1
        if pair == 0 or pair == 3:
            point = 2
            listy = list(vertices[2])
        elif pair == 1 or pair == 4:
            point = 0
            listy = list(vertices[0])
        else:
            point = 1
            listy = list(vertices[1])
        listy[0] += tileWidthInterval*1.5
        listy[1] -= tileHeightInterval
        vertices[point] = tuple(listy)

        tiles(pygame.draw.polygon(screen, transparent_color,
              vertices), (row, column), vertices, "white")
        pygame.draw.lines(screen, "black", True, vertices, 2)

        # setting triangle 3
        if pair == 0 or pair == 3:
            point = 1
            listy = list(vertices[1])
        elif pair == 1 or pair == 4:
            point = 2
            listy = list(vertices[2])
        else:
            point = 0
            listy = list(vertices[0])
        listy[0] += tileWidthInterval*1.5
        listy[1] += tileHeightInterval
        vertices[point] = tuple(listy)

    # For row 2
    if row == 2:
        column += 1
        if pair == 0 or pair == 3:
            point = 1
            listy = list(vertices[1])
        elif pair == 1 or pair == 4:
            point = 2
            listy = list(vertices[2])
        else:
            point = 0
            listy = list(vertices[0])
        listy[0] += tileWidthInterval*1.5
        listy[1] -= tileHeightInterval
        vertices[point] = tuple(listy)

        tiles(pygame.draw.polygon(screen, transparent_color,
              vertices), (row, column), vertices, "white")
        pygame.draw.lines(screen, "black", True, vertices, 2)

        # setting triangle 3
        if pair == 0 or pair == 3:
            point = 0
            listy = list(vertices[0])
        elif pair == 1 or pair == 4:
            point = 1
            listy = list(vertices[1])
        else:
            point = 2
            listy = list(vertices[2])
        listy[0] += tileWidthInterval*1.5
        listy[1] += tileHeightInterval
        vertices[point] = tuple(listy)


def makeTiles():
    # pygame.draw.polygon(screen, transparent_color, vertices)
    global column
    neededLoops = 6

    # loop through every tile
    for row in range(6):
        for pair in range(neededLoops):

            if row == 5 and pair == neededLoops-1:
                # If last tile

                listy1 = list(vertices[0])
                listy2 = list(vertices[1])

                listy1[1] -= tileHeightInterval * 2

                listy2[0] -= tileWidthInterval * 1.5
                listy2[1] -= tileHeightInterval

                vertices[0] = tuple(listy1)
                vertices[1] = tuple(listy2)

                column = 1
                tiles(pygame.draw.polygon(screen, transparent_color,
                      vertices), (row, column), vertices, "white")
                pygame.draw.lines(screen, "black", True, vertices, 2)

            elif pair == neededLoops-1:
                # If last tile on the current row
                column += 1
                tiles(pygame.draw.polygon(screen, transparent_color,
                      vertices), (row, column), vertices, "white")
                pygame.draw.lines(screen, "black", True, vertices, 2)

            else:
                # Make a triangle for the current spot
                makeRow(row, pair, neededLoops)
        neededLoops -= 1


def claim(targetTriangle):
    global claimNotClicked
    global tilePressed
    claimNotClicked = False

    # Store selected triangles into a board
    claimedTriangles = gameLogic.claimedTriangles
    for tile in selectedTiles:
        claimedTriangles[fixCoords(tile['position'][0])
                         ][tile['position'][1]] = tile['numRep']

    # Check if the triangle is llegal
    if gameLogic.checkforTriangles(claimedTriangles, targetTriangle, True):
        print("triangle claimed")
        for tile in selectedTiles:
            tile['state'] = 'white'
            tile['numRep'] = 0
            gameLogic.board[fixCoords(
                tile['position'][0])][tile['position'][1]] = 0

        gameLogic.playGame(True)
        tileDict[fixCoords(gameLogic.r), gameLogic.c]['state'] = 'blue'
        tileDict[fixCoords(gameLogic.r), gameLogic.c]['numRep'] = 2
        tilePressed = False
        print(gameLogic.board)
        for row in range(len(gameLogic.board)):
            for column in range(len(gameLogic.board[row])):
                print(row, column)
                tileDict[fixCoords(
                    row), column]['numRep'] = gameLogic.board[row][column]
                if gameLogic.board[row][column] == 0:
                    tileDict[fixCoords(row), column]['state'] = 'white'

                if gameLogic.board[row][column] == 1:
                    tileDict[fixCoords(row), column]['state'] = 'red'

                if gameLogic.board[row][column] == 2:
                    tileDict[fixCoords(row), column]['state'] = 'blue'
    else:
        print("illegal triangle")
        tilePressed = True
        for tile in selectedTiles:
            pygame.draw.lines(screen, "black", True, tile['vertices'], 2)
        pygame.draw.lines(screen, "red", True, [
                          topLeft, topRight, bottomRight, bottomLeft], 15)
        pygame.display.flip()


# check if a point is within a emptyTriangle button
def point_in_triangle(point, triangle):
    vertex_0 = triangle[0]
    vertex_1 = triangle[1]
    vertex_2 = triangle[2]

    # Calculate vectors
    v0 = (vertex_2[0] - vertex_0[0], vertex_2[1] - vertex_0[1])
    v1 = (vertex_1[0] - vertex_0[0], vertex_1[1] - vertex_0[1])
    v2 = (point[0] - vertex_0[0], point[1] - vertex_0[1])

    # Compute dot products
    dot00 = v0[0] * v0[0] + v0[1] * v0[1]
    dot01 = v0[0] * v1[0] + v0[1] * v1[1]
    dot02 = v0[0] * v2[0] + v0[1] * v2[1]
    dot11 = v1[0] * v1[0] + v1[1] * v1[1]
    dot12 = v1[0] * v2[0] + v1[1] * v2[1]

    # Compute barycentric coordinates
    inv_denominator = 1.0 / (dot00 * dot11 - dot01 * dot01)
    u = (dot11 * dot02 - dot01 * dot12) * inv_denominator
    v = (dot00 * dot12 - dot01 * dot02) * inv_denominator

    # Check if point is inside triangle
    return u >= 0 and v >= 0 and u + v <= 1


# Variable to determine if a gameTile has been clicked
tilePressed = False
gameOngoing = True

# Text variables
# You can choose the font and size you prefer
font = pygame.font.Font(None, 56)
score = f'Player Score: {gameLogic.pointsA}, Computer Score: {gameLogic.pointsB}'
turnText = f'{23 - gameLogic.turnCounter} turn remaning'


while running:
    # fill the screen with a color to wipe away anything from last frame
    screen.blit(marbleImage, marble)

    # RENDER YOUR GAME HERE
    screen.blit(boardImage, board)
    screen.blit(claimButtonImage, claimButton)
    screen.blit(selectButtonImage, selectButton)

    makeTiles()

    if gameLogic.turnCounter == 23:
        if gameLogic.pointsA > gameLogic.pointsB:
            print("Game Over: Player 1 Wins")
            turnText = "Game Over: Player 1 Wins"

            gameOngoing = False
        if gameLogic.pointsB > gameLogic.pointsA:
            print("Game Over: Computer Wins")
            gameOngoing = False
            turnText = "Game Over: Computer Wins"
        if gameLogic.pointsA == gameLogic.pointsB:
            print("Game Over: Tie")
            gameOngoing = False
            turnText = "Game Over: Tie"

    # Text variables
    score = f'Player Score: {gameLogic.pointsA}, Computer Score: {gameLogic.pointsB}'
    scoreBoardText = font.render(score, True, 'turquoise')
    turnBoardText = font.render(turnText, True, 'turquoise')

    scoreBoard = scoreBoardText.get_rect()
    turnBoard = turnBoardText.get_rect()

    scoreBoard.x = 0
    scoreBoard.y = 0
    turnBoard.x = 0
    turnBoard.y = 0 + CLAIM_HEIGHT

    screen.blit(scoreBoardText, scoreBoard)
    screen.blit(turnBoardText, turnBoard)

    if gameOngoing:
        turnText = f'{23 - gameLogic.turnCounter} turns remaning'

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # If mouse down check if a tile has been clicked
        elif event.type == pygame.MOUSEBUTTONDOWN and gameOngoing:
            mouse_pos = pygame.mouse.get_pos()
            for tile in tileDict.values():
                if point_in_triangle(mouse_pos, tile['vertices']) and tile['state'] == 'white':
                    # Tile clicked, perform your desired action here

                    # Update tileDict values to red and remake the triangle on gui and data
                    tile['state'] = "red"
                    tile['numRep'] = 1
                    pygame.draw.polygon(screen, 'red', tile['vertices'])
                    pygame.draw.lines(screen, "black", True,
                                      tile['vertices'], 2)
                    pygame.display.flip()

                    # Switch logicBoard coords to match gui board
                    logicBoardRow = fixCoords(tile['position'][0])
                    gameLogic.board[logicBoardRow][tile['position']
                                                   [1]] = tile['numRep']

                    tilePressed = True
                    returnNotPressed = True

            # Then, while the tile has just been pressed, wait for return or select
            while tilePressed:
                for event in pygame.event.get():

                    # If mouse down, check if select Button is clicked
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if selectButton.collidepoint(pygame.mouse.get_pos()):
                            print("select engaged")
                            selectedTiles = []
                            claimNotClicked = True
                            topLeft = (selectButton.x, selectButton.y)
                            topRight = (selectButton.x +
                                        selectButton.width, selectButton.y)
                            bottomLeft = (selectButton.x,
                                          selectButton.y + selectButton.height)
                            bottomRight = (
                                selectButton.x + selectButton.width, selectButton.y + selectButton.height)
                            # While claim button not clicked yet
                            while claimNotClicked:
                                pygame.draw.lines(screen, "green", True, [
                                                  topLeft, topRight, bottomRight, bottomLeft], 15)
                                pygame.display.flip()
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:

                                        # Check if claim button has been clicked
                                        if claimButton.collidepoint(pygame.mouse.get_pos()):

                                            if len(selectedTiles) == 4:
                                                targetTriangle = 4
                                                claim(targetTriangle)
                                                selectedTiles = []

                                            elif len(selectedTiles) == 9:
                                                targetTriangle = 9
                                                claim(targetTriangle)
                                                selectedTiles = []

                                            else:
                                                print("illegal triangle")
                                                for tile in selectedTiles:
                                                    pygame.draw.lines(
                                                        screen, "black", True, tile['vertices'], 2)
                                                pygame.draw.lines(screen, "red", True, [
                                                                  topLeft, topRight, bottomRight, bottomLeft], 15)
                                                pygame.display.flip()
                                                selectedTiles = []
                                                claimNotClicked = False

                                    # Check if any tiles have been clicked
                                        elif selectButton.collidepoint(pygame.mouse.get_pos()):
                                            claimNotClicked = False
                                            for tile in selectedTiles:
                                                pygame.draw.lines(
                                                    screen, "black", True, tile['vertices'], 2)
                                            pygame.draw.lines(screen, "red", True, [
                                                              topLeft, topRight, bottomRight, bottomLeft], 15)
                                            pygame.display.flip()
                                        else:
                                            for tile in tileDict.values():
                                                if point_in_triangle(pygame.mouse.get_pos(), tile['vertices']):
                                                    print("mouse down")
                                                    # Add tile to selectedtile list
                                                    selectedTiles.append(tile)
                                                    pygame.draw.lines(
                                                        screen, "green", True, tile['vertices'], 2)
                                                    pygame.display.flip()

                    # Otherwise, check if return key has been clicked
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            # Play game, and use CPU choice to change list
                            print("returned")
                            gameLogic.playGame(True)

                            # Adjust game state database
                            tileDict[fixCoords(gameLogic.r),
                                     gameLogic.c]['state'] = 'blue'
                            tileDict[fixCoords(gameLogic.r),
                                     gameLogic.c]['numRep'] = 2
                            for row in range(len(gameLogic.board)):
                                for column in range(len(gameLogic.board[row])):
                                    print(row, column)
                                    tileDict[fixCoords(
                                        row), column]['numRep'] = gameLogic.board[row][column]
                                    if gameLogic.board[row][column] == 0:
                                        tileDict[fixCoords(
                                            row), column]['state'] = 'white'

                                    if gameLogic.board[row][column] == 1:
                                        tileDict[fixCoords(
                                            row), column]['state'] = 'red'

                                    if gameLogic.board[row][column] == 2:
                                        tileDict[fixCoords(
                                            row), column]['state'] = 'blue'

                            # Draw new blue triangles
                            pygame.draw.polygon(screen, "blue", tileDict[fixCoords(
                                gameLogic.r), gameLogic.c]['vertices'])

                            returnNotPressed = False
                            tilePressed = False

    # flip() the display to put your work on screen
    pygame.display.flip()


pygame.quit()
