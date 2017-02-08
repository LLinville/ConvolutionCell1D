import pygame
from pygame.locals import *
from automata.convolution import ConvolutionAutomata1DKernel
from automata.simplexnoise import *
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))

running = 1

ca = ConvolutionAutomata1DKernel(
    cells = [octave_noise_2d(5, 0.5, 1, 0, i) for i in range(500)],
    kernel = [0,1,0])

screen.fill((0,0,0))

rownum = 0

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0
        if event.type == MOUSEBUTTONDOWN:
            randomIndex = random.random()
            ca = ca = ConvolutionAutomata1DKernel(
                cells = [(octave_noise_2d(5, 0.5, 1, randomIndex, i/100.0) + 1) / 2 for i in range(500)],
                kernel = [-0.2,1.2,-0.2])
            rownum = 0
            screen.fill((0,0,0))

    for index, value in enumerate(ca.getCells()):
        screen.set_at((index, rownum), ((value*255)%255, (value*255)%255, (value*255)%255))
    print sum(ca.getCells())

    rownum += 1
    ca.step()

    pygame.display.flip()

pygame.quit()
