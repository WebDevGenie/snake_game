import pygame
pygame.init()
dis=pygame.display.set_mode((500,500))
pygame.display.update()
pygame.display.set_caption("Eugene's Snake Game")

game_over = False
while not game_over:
  for event in pygame.event.get():
    print(event)
    if event.type==pygame.QUIT:
      game_over=True


pygame.quit()
quit()