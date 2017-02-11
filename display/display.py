import pygame
from pygame.locals import *
from automata.convolution import ConvolutionAutomata1DKernel, ConvolutionAutomata2DTransition
from automata.simplexnoise import *
import random

pygame.init()
screen = pygame.display.set_mode((1000, 600))

running = 1

ca = ConvolutionAutomata1DKernel(
    cells = [octave_noise_2d(5, 0.5, 1, 0, i) for i in range(500)],
    kernel = [0,1,0])

ca = ConvolutionAutomata2DTransition(cells = [octave_noise_2d(5, 0.5, 1, 0, i) for i in range(500)], kernel = [1,1,1])

screen.fill((0,0,0))

rownum = 0

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0
        if event.type == MOUSEBUTTONDOWN:
            ca = ConvolutionAutomata2DTransition(cells = [octave_noise_2d(5, 0.5, 1, random.random()*1000, i) for i in range(500)], kernel = [1,1,1])
            rownum = 0
            screen.fill((0,0,0))

    for tX in range(len(ca.getTransitionTable())):
        for tY in range(len(ca.getTransitionTable()[0])):
            value = ca.getTransitionTable()[tX][tY]
            screen.set_at((tX + 600, tY), ((value*255)%255, (value*255)%255, (value*255)%255))

    for index, value in enumerate(ca.getCells()):
        screen.set_at((index, rownum), ((value*255)%255, (value*255)%255, (value*255)%255))
    if sum(ca.getCells()) < 1:
        ca = ConvolutionAutomata2DTransition(cells = [octave_noise_2d(5, 0.5, 1, random.random()*1000, i) for i in range(500)], kernel = [1,1,1])
        rownum = 0
        screen.fill((0,0,0))

    rownum += 1
    rownum = rownum if rownum <=400 else 0
    ca.step()

    pygame.display.flip()

pygame.quit()
