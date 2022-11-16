import pygame
pygame.init()
dis=pygame.display.set_mode((500,500))
pygame.display.update()
pygame.display.set_caption("Eugene's Snake Game")

blue=(0,0,255)
red=(255,0,0)

game_over = False
while not game_over:
  for event in pygame.event.get():
    print(event)
    if event.type==pygame.QUIT:
      game_over=True

  pygame.draw.rect(dis,blue,[250,250,10,10])
  pygame.display.update()


pygame.quit()
quit()