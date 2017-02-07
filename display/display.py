import pygame
from pygame.locals import *
from automata.convolution import ConvolutionAutomata2DKernel

pygame.init()
screen = pygame.display.set_mode((640, 480))

running = 1

ca = ConvolutionAutomata()

screen.fill((0,0,0))

rownum = 0

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0
        if event.type == MOUSEBUTTONDOWN:
            ca = ConvolutionAutomata()
            rownum = 0
            screen.fill((0,0,0))

    for index, value in enumerate(ca.getCells()):
        screen.set_at((index, rownum), ((value*255)%255, (value*255)%255, (value*255)%255))
    print sum(ca.getCells())

    rownum += 1
    ca.step()

    pygame.display.flip()

pygame.quit()
