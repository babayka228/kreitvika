import pygame, sys
from constans import *
sc=pygame.display.set_mode(RES)
pygame.font.init()

FPS=120
clock=pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type==pygame.MOUSEMOTION:
            sc.fill((0,0,0))
            print(event.pos)
            font = pygame.font.Font(None, 24)
            img = font.render(str(event.pos), True, (0,0,255))
            sc.blit(img, (20, 20))
            pygame.display.flip()
            clock.tick(FPS)
            pygame.draw.rect(sc, WHITE, (event.pos[0]-25,event.pos[0]+25,event.pos[1]-25,event.pos[1]+25))
    pygame.display.flip()
    clock.tick(FPS)