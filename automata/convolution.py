import random
import math
from simplexnoise import *


def sigmoid(x, a, alpha = None):
    if alpha is None:
        alpha = 1.0/10
    x, a = 1.0*x, 1.0*a
    return 1 / (1 + math.exp((-4 / alpha) * (x - a)))

def sigm(m, a, b):
    m, a, b = 1.0*m, 1.0*a, 1.0*b
    return a * (1 - sigmoid(m, 0.5)) + b * sigmoid(m, 0.5)

def sign(n, a, b):
    n, a, b = 1.0*n, 1.0*a, 1.0*b
    return sigmoid(n, a) * (1 - sigmoid(n, b))

def clamp(x):
    if x < 0:
        return 0
    if x > 1:
        return 1
    return x

class ConvolutionAutomata1DKernel():
    def __init__(self, cells = None, kernel = None):

        if not cells:
            self.cells = [random.random() for i in range(self.width)]
        else:
            self.cells = cells

        self.width = len(self.cells)

        if not kernel:
            self.kernel = [random.random() - 0.4 for i in range(500)]
            self.kernel = [1.0 * k / sum(self.kernel) for k in self.kernel]
        else:
            self.kernel = kernel

        self.kernelWidth = len(self.kernel)

    def getCells(self):
        return self.cells

    def step(self):
        newCells = [0 for i in range(self.width)]

        for indexToCalculate in range(self.width):
            total = 0.0

            for kernelIndex, cellOffset in enumerate(range(-1 * self.kernelWidth / 2 + 1, self.kernelWidth / 2 + 1)):
                total += self.kernel[kernelIndex] * self.cells[(indexToCalculate + cellOffset) % self.width]

            newCells[indexToCalculate] = total

        self.cells = newCells

        self.cells = [1 if cell > 1 else cell for cell in self.cells]
        self.cells = [0 if cell < 0 else cell for cell in self.cells]

class ConvolutionAutomata2DTransition():
    def transition(self, n, m):
        return sign(n, sigm(m, self.b1, self.b2), sigm(m, self.d1, self.d2))

    def __init__(self, cells = None, kernel = None):
        self.b1 = 0.25
        self.b2 = self.d1 = self.d2 = 3.0/8
        self.b1, self.b2, self.d1, self.d2 = random.random(), random.random(), random.random(), random.random()
        if cells is None:
            self.width = 500
            self.cells = [random.random() for i in range(self.width)]
        else:
            self.cells = cells
            self.width = len(self.cells)

        if kernel is None:
            self.kernel = [1,1,1]
        else:
            self.kernel = kernel

        self.kernelWidth = len(self.kernel)
        self.kernel = [1.0 * k / sum(self.kernel) for k in self.kernel]

        #self.transitionTable = [[sigmoid(0.5, (octave_noise_3d(1, 0.5, 1, sumValue / 100000.0, currentValue / 100000.0, random.random()*1000)+1)/(2.0), 1.0/2) for sumValue in range(100)] for currentValue in range(100)]
        #self.transitionTable = [[(octave_noise_3d(1, 0.5, 1, sumValue / 100.0, currentValue / 100.0, random.random()*1000)+1)/(2.0) for sumValue in range(100)] for currentValue in range(100)]

        randomIndex = random.random()*1000
        self.transitionTable = [[0 for x in range(100)] for y in range(100)]
        for x in range(len(self.transitionTable)):
            for y in range(len(self.transitionTable[x])):
                self.transitionTable[x][y] = (octave_noise_3d(4, 0.5, 1, x/100.0, y/100.0, randomIndex) + 1) / 2
                self.transitionTable[x][y] = sigmoid(0.5, self.transitionTable[x][y], 1/5.0)
                #print x, y, self.transitionTable[x][y]

        #self.transitionTable = [[self.transition(x/100.0, y/100.0) for x in range(100)] for y in range(100)]
        #self.transitionTable = [[clamp(value * 2) for value in row] for row in self.transitionTable]

    def getCells(self):
        return self.cells

    def getTransitionTable(self):
        return self.transitionTable

    def step(self):
        newCells = [0 for i in range(self.width)]

        for indexToCalculate in range(self.width):
            total = 0.0

            for kernelIndex, cellOffset in enumerate(range(-1 * self.kernelWidth / 2 + 1, self.kernelWidth / 2 + 1)):
                total += self.kernel[kernelIndex] * self.cells[(indexToCalculate + cellOffset) % self.width]

            newCells[indexToCalculate] = self.transitionTable[int(99*clamp(self.cells[indexToCalculate]))][int(clamp(total) * 99)]

        self.cells = newCells