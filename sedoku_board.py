import pygame
import copy
from sedoku_solver import printBoard, solvePuzzle, generate

class Board:
    def __init__(self, display):
        self.board = [[0 for i in range(9)] for j in range(9)]
        self.generate(self.board)
        self.initialDisplay = True
        self.canPlay = True
        self.solvedBoard = copy.deepcopy(self.board)
        self.solve(self.solvedBoard)
        self.initialValuePos = []
        self.isSolved = False
        self.color = [(0, 0, 0), (255, 0, 0), (0, 0, 255), (255, 0, 0)]
        self.surface = pygame.display.set_mode((541, 541))
        self.tiles = []
        self.threeByThreeTiles = []
        self.tilesPos = [0, 0]
        self.createRecs()
        self.selected = False
        self.font = pygame.font.SysFont('Arial', 35)
        self.rowsAndCols = [0, 0]

    def draw(self, display):
        for i, item in enumerate(self.tiles):
            for j, recs in enumerate(item):
                if self.isSolved is False:
                    if self.selected is False:
                        pygame.draw.rect(recs[0], recs[1], recs[2], recs[3])
                    else:
                        if i == self.rowsAndCols[0] and j == self.rowsAndCols[1]:
                            self.surface.fill((211, 211, 211), pygame.draw.rect(recs[0], recs[1], recs[2], recs[3]))
                        else:
                            pygame.draw.rect(recs[0], recs[1], recs[2], recs[3])
                    if self.board[i][j] != 0 and self.initialDisplay:
                        text = self.font.render(str(self.board[i][j]), True, self.color[0])
                        self.surface.blit(text, (recs[2][0] + 40 // 2, recs[2][1] + 20 // 2))
                        self.initialValuePos.append((i, j))
                    elif self.board[i][j] != 0 and self.initialDisplay is False and (i, j) not in self.initialValuePos:
                        text = self.font.render(str(self.board[i][j]), True, self.color[2])
                        self.surface.blit(text, (recs[2][0] + 40 // 2, recs[2][1] + 20 // 2))
                    elif self.board[i][j] != 0 and self.initialDisplay is False and (i, j) in self.initialValuePos:
                        text = self.font.render(str(self.board[i][j]), True, self.color[0])
                        self.surface.blit(text, (recs[2][0] + 40 // 2, recs[2][1] + 20 // 2))
                else:
                    pygame.draw.rect(recs[0], recs[1], recs[2], recs[3])
                    if self.board[i][j] != self.solvedBoard[i][j]:
                        text = self.font.render(str(self.solvedBoard[i][j]), True, self.color[3])
                        self.surface.blit(text, (recs[2][0] + 40 // 2, recs[2][1] + 20 // 2))
                    elif self.board[i][j] == self.solvedBoard[i][j] and (i, j) not in self.initialValuePos:
                        text = self.font.render(str(self.board[i][j]), True, self.color[2])
                        self.surface.blit(text, (recs[2][0] + 40 // 2, recs[2][1] + 20 // 2))
                    elif self.board[i][j] == self.solvedBoard[i][j] and (i, j) in self.initialValuePos:
                        text = self.font.render(str(self.board[i][j]), True, self.color[0])
                        self.surface.blit(text, (recs[2][0] + 40 // 2, recs[2][1] + 20 // 2))
                
        self.initialDisplay = False

        for item in self.threeByThreeTiles:
            for recs in item:
                pygame.draw.rect(recs[0], recs[1], recs[2], recs[3])

    def gameControls(self):
        keys = pygame.key.get_pressed()
        if self.selected and self.canPlay:
            if keys[pygame.K_1] or keys[pygame.K_KP1]:
                self.setNum(1)
            elif keys[pygame.K_2] or keys[pygame.K_KP2]:
                self.setNum(2)
            elif keys[pygame.K_3] or keys[pygame.K_KP3]:
                self.setNum(3)
            elif keys[pygame.K_4] or keys[pygame.K_KP4]:
                self.setNum(4)
            elif keys[pygame.K_5] or keys[pygame.K_KP5]:
                self.setNum(5)
            elif keys[pygame.K_6] or keys[pygame.K_KP6]:
                self.setNum(6)
            elif keys[pygame.K_7] or keys[pygame.K_KP7]:
                self.setNum(7)
            elif keys[pygame.K_8] or keys[pygame.K_KP8]:
                self.setNum(8)
            elif keys[pygame.K_9] or keys[pygame.K_KP9]:
                self.setNum(9)
            elif keys[pygame.K_BACKSPACE] or keys[pygame.K_0] or keys[pygame.K_KP0]:
                self.setNum(0)
        if keys[pygame.K_SPACE]:
            self.isSolved = True
            self.canPlay = False

    def generate(self, board):
        generate(board)

    def solve(self,board):
        solvePuzzle(board)

    def printBoard(self,board):
        printBoard(board)

    def setNum(self, val):
        self.board[self.rowsAndCols[0]][self.rowsAndCols[1]] = val

    def createRecs(self):
        for i in range(9):
            temp = []
            for j in range(9):
                temp.append((self.surface, self.color[0], (self.tilesPos[0], self.tilesPos[1], 60, 60), 2))
                self.tilesPos[0] += 60
            self.tilesPos[1] += 60
            self.tilesPos[0] -= 60 * 9
            self.tiles.append(temp)
        self.tilesPos[0] = 0
        self.tilesPos[1] = 0
        for i in range(3):
            temp = []
            for j in range(3):
                temp.append((self.surface, self.color[1], (self.tilesPos[0], self.tilesPos[1], 180, 180), 2))
                self.tilesPos[0] += 180
            self.tilesPos[1] += 180
            self.tilesPos[0] = 0
            self.threeByThreeTiles.append(temp)
