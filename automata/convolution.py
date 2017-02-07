import random
import math

class ConvolutionAutomata1DKernel():
    def __init__(self):
        self.width = 500
        self.kernelWidth = 7
        self.kernel = [random.random() - 0.4 for i in range(self.kernelWidth)]
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

class ConvolutionAutomata2DKernel():
    def __init__(self):
        self.width = 500
        self.kernelSize = 7
        def randomRow():
            return [random.random() - 0.4 for i in range(self.kernelSize)]
        self.kernel = [randomRow() for i in range(self.kernelSize)]
        self.kernel = [1.0 * k / sum(self.kernel) for k in self.kernel]
        self.cells = [random.random() for i in range(self.width)]

    def getCells(self):
        return self.cells

    def step(self):
        newCells = [0 for i in range(self.width)]

        for indexToCalculate in range(self.width):
            total = 0.0

            for kernelIndex, cellOffset in enumerate(range(-1 * self.kernelSize / 2 + 1, self.kernelSize / 2 + 1)):
                total += self.kernel[kernelIndex] * self.cells[(indexToCalculate + cellOffset) % self.width]

            newCells[indexToCalculate] = total

        self.cells = newCells