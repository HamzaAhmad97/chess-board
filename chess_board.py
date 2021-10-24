import matplotlib.pyplot as plt
import numpy as np

class ChessBoard:
    def __init__(self):
        self.grid = np.zeros((8,8,3))
        self.blue = [0,0]
        self.red = [0,0]
        self.create_grid()
    def add_red(self, row, col):
        self.grid[row, col] = (1,0,0)
        self.red = [row, col]
    def add_blue(self, row, col):
        self.grid[row, col] = (0,0,1.0)
        self.blue = [row, col]
    def render(self):
        plt.imshow(self.grid)
    def is_under_attack(self):
        hor = self.blue[1] - self.red[1]
        vert = self.blue[0] - self.red[0]
        try:
            slope = abs(vert / hor)
        except ZeroDivisionError:
            return True
        
        return (slope == 1 ) or not vert
    def create_grid(self):
        length = range(len(self.grid))
        for i in length:
            for j in length:
                self.grid[i,j] = [1,1,1] if (not i%2 and not j%2) or (i%2 and j%2) else [0,0,0]