import time
import random

import pygame


class Sort:
    def __init__(self):
        self.lineColor = (18, 124, 128)
        self.running = False
        self.backgroundColor = (63, 64, 51)
        self.arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Keep values less than 380, because of buttons
        self.keepSorting = True
        self.generateRandomArr()
        self.width, self.height = 800, 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(self.backgroundColor)
        self.game()

    def generateRandomArr(self):
        for i in range(len(self.arr)):
            self.arr[i] = random.randint(1, 350)

    def game(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.sortAndShow()
                    if event.key == pygame.K_r:
                        self.generateRandomArr()

            self.drawArr()
            pygame.display.update()

    def drawArr(self):
        self.screen.fill(self.backgroundColor)
        widthOfLines = int(self.width / len(self.arr))
        for index, value in enumerate(self.arr):
            indx = index + 0.5
            pygame.draw.line(self.screen, self.lineColor, ((indx * widthOfLines), 0), ((indx * widthOfLines), value),
                             width=widthOfLines - 20)

    def highlightLinesBefore(self, x, y):
        self.screen.fill(self.backgroundColor)
        widthOfLines = int(self.width / len(self.arr))
        for index, value in enumerate(self.arr):
            indx = index + 0.5
            if x == value or y == value:
                pygame.draw.line(self.screen, (229, 240, 22), ((indx * widthOfLines), 0),
                                 ((indx * widthOfLines), value),
                                 width=widthOfLines - 20)
            else:
                pygame.draw.line(self.screen, self.lineColor, ((indx * widthOfLines), 0),
                                 ((indx * widthOfLines), value),
                                 width=widthOfLines - 20)

    def highlightLinesAfter(self, x, y):
        self.screen.fill(self.backgroundColor)
        widthOfLines = int(self.width / len(self.arr))
        for index, value in enumerate(self.arr):
            indx = index + 0.5
            if x == value or y == value:
                pygame.draw.line(self.screen, (100, 255, 255), ((indx * widthOfLines), 0),
                                 ((indx * widthOfLines), value),
                                 width=widthOfLines - 20)
            else:
                pygame.draw.line(self.screen, self.lineColor, ((indx * widthOfLines), 0),
                                 ((indx * widthOfLines), value),
                                 width=widthOfLines - 20)

    def sortAndShow(self):
        for i in range(len(self.arr) - 1):
            for x in range(i + 1, len(self.arr)):
                if self.arr[i] > self.arr[x]:
                    self.highlightLinesBefore(self.arr[i], self.arr[x])
                    pygame.display.update()
                    time.sleep(0.5)
                    self.arr[i], self.arr[x] = self.arr[x], self.arr[i]
                    self.highlightLinesAfter(self.arr[i], self.arr[x])
                    pygame.display.update()
                    time.sleep(0.5)


s = Sort()
