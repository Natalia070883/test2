import pygame
from pygame.draw import *
GREY = (190, 190, 190)
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill(GREY)
x1 = 65; y1 = 15
x2 = 60; y2 = 35
circle(screen, (255, 255, 0), (200, 175), 150)
circle(screen, (0, 0, 0), (200, 175), 150,1)
rect(screen, (0, 0, 0), (120, 250, 150, 25))
circle(screen, (255, 0, 0), (260, 150), 20)
circle(screen, (0, 0, 0), (260, 150), 20,1)
circle(screen, (0, 0, 0), (260, 150), 10)
circle(screen, (255, 0, 0), (140, 150), 30)
circle(screen, (0, 0, 0), (140, 150), 30,1)
circle(screen, (0, 0, 0), (140, 150), 10)
polygon(screen, (0, 0, 0), [(x1+300,y1+60), (x2+300,y2+60),
                               (x2+155,y2+120), (x1+150,y1+120)])
polygon(screen, (0, 0, 0), [(x1,y1), (x2,y2),
                               (x2+120,y2+120), (x1+120,y1+120)])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()