import pygame
import boardfuns

#Init Pygame 
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

#Constace
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE / 2 - 5)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


board = None
board = boardfuns.create_board(ROW_COUNT,COLUMN_COUNT)
print(board)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill("pink")

    boardfuns.draw_board(board, screen)



    pygame.display.flip()

    clock.tick(60)
    

pygame.quit()