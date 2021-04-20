import pygame

WIDTH, HEIGHT = 900, 500
BLACK = (0, 0, 0)

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("MultiSnakeBros")
image = pygame.image.load("snake.jpg")
pygame.display.set_icon(image)



def draw_window():
    WIN.fill(BLACK)
    pygame.display.update()

def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        draw_window()
    main()

if __name__ == "__main__":
    main()