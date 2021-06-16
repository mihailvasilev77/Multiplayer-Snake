import pygame
import sys
import random
import singleplayer

class mains():
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH/2), (HEIGHT/2))]
        self.colour = BLACK
        self.score = 0
        self.colcheck = False

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
        self.colcheck = True

    def draw(self,surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
            pygame.draw.rect(surface, self.colour, r)
            pygame.draw.rect(surface, self.colour, r, 1)
            
class Snake(mains):
    def __init__(self):
        super().__init__()
        self.colour = BLUE
        self.direction = random.choice([up, left])
 
class Snake1(mains):
    def __init__(self):
        super().__init__()
        self.colour = GREEN 
        self.direction = random.choice([down, right])

class Food():
    def __init__(self):
        self.position = (0,0)
        self.colour = RED
        self.randomize_position()

    def randomize_position(self):
        chance = random.uniform(0,1)
        if chance >= 0.8:
            self.colour = YELLOW
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

def handleMovement(up,down,right,left):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:
            snake.turn(up)
        if keys_pressed[pygame.K_d]:
            snake.turn(right)
        if keys_pressed[pygame.K_s]:
            snake.turn(down)
        if keys_pressed[pygame.K_a]:
            snake.turn(left)
        if keys_pressed[pygame.K_UP]:
            snake1.turn(up)
        if keys_pressed[pygame.K_RIGHT]:
            snake1.turn(right)
        if keys_pressed[pygame.K_DOWN]:
            snake1.turn(down)
        if keys_pressed[pygame.K_LEFT]:
            snake1.turn(left)

def snakeCol(snake,snake1):
    if snake.get_head_position() in snake1.positions:
        snake.reset()
        
    if snake1.get_head_position() in snake.positions:
        snake1.reset()

def eatCheck(snake,food):
    if snake.get_head_position() == food.position:
        if food.colour == YELLOW:
            snake.length += 2
            snake.score += 2
            food.colour = RED
        else:
            snake.length += 1
            snake.score += 1
        food.randomize_position()

def gameloop(choice):
    while (True):
        clock.tick(velocity)
        seconds=(pygame.time.get_ticks()-start_ticks)/1000

        handleMovement(up,down,right,left)
        drawBoard(surface)
        snake.move()
        snake1.move()

        snakeCol(snake,snake1)
        snakeCol(snake1,snake)
        
        eatCheck(snake,food)
        eatCheck(snake1,food)

        snake.draw(surface)
        snake1.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))

        p1 = font.render("Player 1: {0}".format(snake.score), 1, (0,0,0))
        p2 = font.render("Player 2: {0}".format(snake1.score), 1, (0,0,0))
        screen.blit(p1, (4,5))
        screen.blit(p2,(485,5))

        if choice == True:
            if snake.colcheck == True:
                text = font.render("Player 2 won cograts",True,BLACK, GREEN)
                screen.fill(BLACK)
                screen.blit(text, centertext)
            if snake1.colcheck == True:
                text = font.render("Player 1 won cograts",True,BLACK, BLUE)
                screen.fill(BLACK)
                screen.blit(text, centertext)
        else:
            secs = font.render("{:.2f}".format(seconds),True,BLACK)
            screen.blit(secs,(WIDTH//2-30,5))
            if seconds>120:
                if snake.score > snake1.score:
                    text = font.render("Player 1 won cograts",True,BLUE, BLACK)
                elif snake1.score > snake.score:
                    text = font.render("Player 2 won cograts",True,GREEN, BLACK)
                else:
                    text = font.render("Draw. Nobody won. :(",True,LIGHT_BLUE, LIGHT_PURPLE)
                screen.fill(BLACK)
                screen.blit(text, centertext)
        
        pygame.display.update()

def main():
    ans = input("Please select the desirable singleplayer or multiplayer:")
    if ans == "singleplayer":
        singleplayer.main()
    else:
        answer = input("Please select the desirable gamemode (time rush/vanilla):")
        choice = False
        if answer == "vanilla":
            choice = True
        gameloop(choice)

WIDTH = 600
HEIGHT = 480

RED = (224, 18, 18)
BLUE = (10, 13, 240)
GREEN = (10, 240, 98)
YELLOW = (255,255,0)
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
velocity = 12

snake = Snake()
snake1 = Snake1()
food = Food()

pygame.init()
clock = pygame.time.Clock()
start_ticks=pygame.time.get_ticks()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

pygame.display.set_caption("MultiSnakeBros")
image = pygame.image.load("snake.jpg")
pygame.display.set_icon(image)

font = pygame.font.SysFont("agencyfb",32)
text = font.render("Player X won cograts",True,WHITE, BLACK)
centertext = text.get_rect()
centertext.center = (WIDTH//2, HEIGHT//2)

surface = pygame.Surface(screen.get_size())
surface = surface.convert()
drawBoard(surface)