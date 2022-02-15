import random
import pygame
pygame.init()
RES=WIDTH,HEIGHT=1500,900
tile=50
sc=pygame.display.set_mode(RES)
clock=pygame.time.Clock()
while True:
    [pygame.draw.line(sc,(255,255,255),(x,0),(x,HEIGHT)) for x in range(0,WIDTH, tile)]
    [pygame.draw.line(sc,(255,255,255),(0,y),(WIDTH,y)) for y in range(0,HEIGHT, tile)]
    pygame.display.flip()
    clock.tick(60)