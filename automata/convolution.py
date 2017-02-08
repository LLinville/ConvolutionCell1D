import random
import math

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

class ConvolutionAutomata2DKernel():
    def __init__(self):
        self.width = 500
        self.kernelWidth = 7
        self.kernelHeight = 100
        def randomRow():
            return [random.random() for i in range(self.kernelWidth)]
        self.kernel = [randomRow() for i in range(self.kernelWidth)]
        self.kernel = [1.0 * k / sum(self.kernel) for k in self.kernel]
        self.cells = [random.random() for i in range(self.width)]

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