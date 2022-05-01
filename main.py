import time
import random
import pygame


class Sort:
    #  Initializes the class fills background, generates list, set background-color, etc...
    def __init__(self):
        pygame.init()
        self.ding_sound = pygame.mixer.Sound("ding_sound_effect.mp3")
        self.lineColor = (18, 124, 128)
        self.running = False
        self.backgroundColor = (63, 64, 51)
        self.arr = [1] * 130 # Max number of items in array can be width/2
        self.width, self.height = 800, 500
        self.timer_interval = False
        self.time = 0.5
        self.generateRandomArr()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(self.backgroundColor)
        self.game()


    #  Fill the array arr with random integers from 10 to 350
    def generateRandomArr(self):
        for i in range(len(self.arr)):
            self.arr[i] = random.randint(10, self.height)
        print(self.arr)

    #  Keeps the game running and handles input
    def game(self):
        self.running = True
        while self.running:
            self.drawArr()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.running = False
                    if event.key == pygame.K_SPACE:
                        self.sortAndShow('selection')
                    if event.key == pygame.K_b:
                        self.sortAndShow('bubble')
                    if event.key == pygame.K_i:
                        self.sortAndShow('insertion')
                    if event.key == pygame.K_r:
                        self.generateRandomArr()
                    if event.key == pygame.K_s:
                        self.arr.sort()
                    if event.key == pygame.K_t:
                        if self.timer_interval:
                            self.timer_interval = False
                        else:
                            self.timer_interval = True

    #  Draws the initial array
    def drawArr(self):
        self.screen.fill(self.backgroundColor)
        width_of_lines = float(self.width / len(self.arr))
        for index, value in enumerate(self.arr):
            if index == 0:
                pygame.draw.line(self.screen, self.lineColor, (((index+0.5) * width_of_lines), 0), (((index+0.5) * width_of_lines), value), width=round((self.width / len(self.arr))/2))
            else:
                pygame.draw.line(self.screen, self.lineColor, (((index+0.5) * width_of_lines), 0), (((index+0.5) * width_of_lines), value), width=round((self.width / len(self.arr))/2))

    #  Highlights the lines which need to be swapped before they are swapped
    def highlightLinesBefore(self, x, y):
        self.screen.fill(self.backgroundColor)
        width_of_lines = float(self.width / len(self.arr))
        for index, value in enumerate(self.arr):

            if x == index or y == index:
                pygame.draw.line(self.screen, (255, 0, 0), (((index+0.5) * width_of_lines), 0), (((index+0.5) * width_of_lines), value), width=round((self.width / len(self.arr))/2))
            else:
                pygame.draw.line(self.screen, self.lineColor, (((index+0.5) * width_of_lines), 0), (((index+0.5) * width_of_lines), value), width=round((self.width / len(self.arr))/2))

    #  Highlights the lines which need to be swapped after they are swapped
    def highlightLinesAfter(self, x, y):
        self.screen.fill(self.backgroundColor)
        width_of_lines = float(self.width / len(self.arr))
        for index, value in enumerate(self.arr):
            if x == index or y == index:
                pygame.draw.line(self.screen, (50, 168, 82), (((index+0.5) * width_of_lines), 0), (((index+0.5) * width_of_lines), value), width=round((self.width / len(self.arr))/2))
            else:
                pygame.draw.line(self.screen, self.lineColor, (((index+0.5) * width_of_lines), 0), (((index+0.5) * width_of_lines), value), width=round((self.width / len(self.arr))/2))

    #  Highlights the lines which won't be swapped/are currently being checked
    def highlightLinesLowerThan(self, x, y):
        self.screen.fill(self.backgroundColor)
        width_of_lines = float(self.width / len(self.arr))
        for index, value in enumerate(self.arr):
            if x == index or y == index:
                pygame.draw.line(self.screen, (229, 240, 22), (((index+0.5) * width_of_lines), 0), (((index+0.5) * width_of_lines), value), width=round((self.width / len(self.arr))/2))
            else:
                pygame.draw.line(self.screen, self.lineColor, (((index+0.5) * width_of_lines), 0), (((index+0.5) * width_of_lines), value), width=round((self.width / len(self.arr))/2))

    #  Sorts the lines and play a ding sound effect when sorting is finished
    def sortAndShow(self, sort_method):
        if sort_method == 'selection':
            for i in range(len(self.arr) - 1):
                for x in range(i + 1, len(self.arr)):
                    if self.arr[i] > self.arr[x]:
                        self.highlightLinesBefore(i, x)
                        pygame.display.update()
                        if self.timer_interval:
                            time.sleep(self.time)
                        self.arr[i], self.arr[x] = self.arr[x], self.arr[i]
                        self.highlightLinesAfter(i, x)
                        pygame.display.update()
                        if self.timer_interval:
                            time.sleep(self.time)
                    else:
                        self.highlightLinesLowerThan(i, x)
                        pygame.display.update()
                        if self.timer_interval:
                            time.sleep(self.time)
            pygame.mixer.Sound.play(self.ding_sound)
        elif sort_method == 'bubble':
            for outer_loop in range(len(self.arr)):
                for i in range(len(self.arr)-outer_loop-1):
                    if self.arr[i] > self.arr[i+1]:
                        self.highlightLinesBefore(i, i+1)
                        pygame.display.update()
                        if self.timer_interval:
                            time.sleep(self.time)
                        self.arr[i], self.arr[i+1] = self.arr[i+1], self.arr[i]
                        self.highlightLinesAfter(i, i+1)
                        pygame.display.update()
                        if self.timer_interval:
                            time.sleep(self.time)
                    else:
                        self.highlightLinesLowerThan(i, i+1)
                        pygame.display.update()
                        if self.timer_interval:
                            time.sleep(self.time)
            pygame.mixer.Sound.play(self.ding_sound)
        elif sort_method == 'insertion':
            for i in range(1, len(self.arr)):
                value_to_sort = self.arr[i]
                while self.arr[i-1] > value_to_sort and i > 0:
                    self.highlightLinesBefore(i-1, i)
                    pygame.display.update()
                    if self.timer_interval:
                        time.sleep(self.time)
                    self.arr[i], self.arr[i - 1] = self.arr[i - 1], self.arr[i]
                    self.highlightLinesAfter(i-1, i)
                    pygame.display.update()
                    if self.timer_interval:
                        time.sleep(self.time)
                    i-=1
                if i > 0:
                    self.highlightLinesLowerThan(i-1, i)
                    pygame.display.update()
                    if self.timer_interval:
                        time.sleep(self.time)
            pygame.mixer.Sound.play(self.ding_sound)


s = Sort()
