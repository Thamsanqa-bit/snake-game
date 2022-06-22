from json.encoder import ESCAPE
import pygame
import time
from pygame.locals import *
import random

size = 40

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.y = size*3
        self.x = size*3

    def draw(self):
        self.parent_screen.blit(self.image,(self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0, 24)*size
        self.y = random.randint(0, 19)*size

class Snake:
    def __init__ (self,parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.x = [size]*length
        self.y = [size]*length
        self.block = pygame.image.load("resources/snake.webp").convert()
        self.block = pygame.transform.scale(self.block, (30, 30))
        self.direction = 'down'

    def draw(self):
        self.parent_screen.fill((255, 255, 255))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i], self.y[i]))
        pygame.display.flip()

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'


    def walk(self):
        for i in range(self.length-1,0,-1):
            self.y[i] = self.y[i - 1]
            self.x[i] = self.x[i - 1]

        if self.direction == 'up':
            self.y[0] -= size
        if self.direction == 'down':
            self.y[0] += size
        if self.direction == 'left':
            self.x[0] -= size
        if self.direction == 'right':
            self.x[0] += size

        self.draw()


class Game:
    def __init__ (self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.surface.fill((255, 255, 255))
        self.snake = Snake(self.surface, 5)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self, x1,y1,x2,y2):
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True

        return False

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # snake coliding wuth the apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.apple.move()

        #snake coliding with itself
        # for i in range(3, self.snake.length):
        #     if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
        #         print("Game Over")
        #         exit(0)

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True,(0,0,0))
        self.surface.blit(score,(800,10))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    pass
                    if event.key == ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                elif event.type == QUIT:
                    running = False
            self.play()
            time.sleep(0.3)


if __name__ == "__main__":
    game = Game()
    game.run()

