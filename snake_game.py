import pygame
import random
pygame.init()


dis=pygame.display.set_mode((500,500))
pygame.display.update()
pygame.display.set_caption("Eugene's Snake Game")

# Set Colors
blue=(0,0,255)
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)

# Snake starting point
x1 = 250
y1 = 250

x1_change=0
y1_change=0

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

# Message function
def message(msg,color):
  mesg = font_style.render(msg, True, color)
  dis.blit(mesg, [200, 200])

game_over = False


# Spawn food randomly
food_x = round(random.randrange(0, 500 - 10) / 10.0) * 10.0
food_y = round(random.randrange(0, 500 - 10) / 10.0) * 10.0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0

    # Create border restrictions for snake
    if x1 >= 500 or x1 < 0 or y1 >= 500 or y1 < 0:
      game_over=True

    x1 += x1_change
    y1 += y1_change
    dis.fill(black)

    # Create Food
    pygame.draw.rect(dis, red, [food_x, food_y, 10, 10])

    # Create Snake
    pygame.draw.rect(dis,white,[x1,y1,10,10])
    pygame.display.update()

    # When snake eats food
    if x1 == food_x and y1 == food_y:
        print("Nom Nom Nom")
    

    clock.tick(30)

message("Game Over", red)
pygame.display.update()


pygame.quit()
quit()