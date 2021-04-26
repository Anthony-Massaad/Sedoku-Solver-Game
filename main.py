import pygame
import sedoku_board
import copy
pygame.init()
gameWidth = 541
gameHeight = 541

display = pygame.display.set_mode((gameWidth, gameHeight))
pygame.display.set_caption("Sedoku")
clock = pygame.time.Clock()
mainBoard = sedoku_board.Board(display)


def draw():
    display.fill((255,255,255))
    mainBoard.draw(display)
    pygame.display.update()


run = True
found = False
while run: 
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and mainBoard.canPlay:
            mouseX, mouseY = pygame.mouse.get_pos()
            countPos = [0, 0]
            for i in range(9):
                for j in range(9):
                    if countPos[0] <= mouseX <= countPos[0] + 60 and countPos[1] <= mouseY <= countPos[1] + 60 and (i, j) not in mainBoard.initialValuePos:
                        mainBoard.rowsAndCols[0] = i
                        mainBoard.rowsAndCols[1] = j
                        mainBoard.selected = True
                        found = True
                        break
                    if found:
                        found = False
                        break
                    countPos[0] += 60
                countPos[1] += 60
                countPos[0] = 0
            countPos[0] = 0
            countPos[1] = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mainBoard.selected = False
                mainBoard.isSolved = False
                mainBoard.initialDisplay = True
                mainBoard.canPlay = True
                mainBoard.tiles = []
                mainBoard.threeByThreeTiles = []
                mainBoard.tilesPos = [0, 0]
                mainBoard.createRecs()
                mainBoard.rowsAndCols = [0, 0]
                mainBoard.initialValuePos = []
                mainBoard.board = [[0 for i in range(9)] for j in range(9)]
                mainBoard.generate(mainBoard.board)
                mainBoard.solvedBoard = copy.deepcopy(mainBoard.board)
                mainBoard.solve(mainBoard.solvedBoard)

    mainBoard.gameControls()
    draw()

pygame.quit()