from automata.simplexnoise import *
import random
import pygame
from pygame.locals import *
from automata.convolution import *


pygame.init()
screen = pygame.display.set_mode((640, 480))

running = 1

screen.fill((0,0,0))

rownum = 0

b1 = 0.25
b2 = d1 = d2 = 0.375

def transition(n, m):
        return sign(n, sigm(m, b1, b2), sigm(m, d1, d2))

table = [[0 for x in range(400)] for y in range(400)]
for x in range(len(table)):
    for y in range(len(table[x])):
        table[x][y] = octave_noise_3d(1, 0.5, 1, x/400.0, y/400.0, 1)
        print x, y, table[x][y]

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0
        if event.type == MOUSEBUTTONDOWN:
            b1, b2, d1, d2 = random.random(), random.random(), random.random(), random.random()
            rownum = 0
            screen.fill((0,0,0))


    print rownum
    for x in range(400):
        for y in range(400):
            # value = octave_noise_3d(5, 0.5, 1, x/400.0, y/400.0, rownum) + 1
            # value /= 2

            value = table[x][y]

            #value = sign(x/400.0, 0.25, 0.75)
            screen.set_at((x,y), ((value*255)%255, (value*255)%255, (value*255)%255))

    rownum += 1

    pygame.display.flip()

pygame.quit()
