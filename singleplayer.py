import pygame
import sys
import random

class Snake():
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH/2), (HEIGHT/2))]
        self.colour = BLACK
        self.score = 0
        self.direction = random.choice([up, down, left, right])

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x,y = self.direction
        new = (((cur[0]+(x*gridsize))%WIDTH), (cur[1]+(y*gridsize))%HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((WIDTH/2), (HEIGHT/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw(self,surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
            pygame.draw.rect(surface, self.colour, r)
            pygame.draw.rect(surface, BLACK, r, 1)

    def handleMovement(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.turn(up)
                elif event.key == pygame.K_s:
                    self.turn(down)
                elif event.key == pygame.K_a:
                    self.turn(left)
                elif event.key == pygame.K_d:
                    self.turn(right)

class Food():
    def __init__(self):
        self.position = (0,0)
        self.colour = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_width-1)*gridsize, random.randint(0, grid_height-1)*gridsize)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.colour, r)
        pygame.draw.rect(surface, self.colour, r, 1)

def drawBoard(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x+y)%2 == 0:
                ss = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface,LIGHT_BLUE, ss)
            else:
                fs = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface, LIGHT_PURPLE, fs)

WIDTH = 600
HEIGHT = 480

RED = (224, 18, 18)
BLUE = (10, 13, 240)
GREEN = (10, 240, 98)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_BLUE = (87, 175, 230)
LIGHT_PURPLE = (144, 135, 245)

gridsize = 20
grid_width = WIDTH/gridsize
grid_height = HEIGHT/gridsize

up = (0,-1)
down = (0,1)
left = (-1,0)
right = (1,0)


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawBoard(surface)

    snake = Snake()
    food = Food()

    myfont = pygame.font.SysFont("agencyfb",25)

    while (True):
        clock.tick(10)
        snake.handleMovement()
        drawBoard(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))
        text = myfont.render("Player 1: {0}".format(snake.score), 1, (0,0,0))
        screen.blit(text, (5,10))
        pygame.display.update()