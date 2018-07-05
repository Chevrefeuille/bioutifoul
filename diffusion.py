import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Grid:
    """The diffusion grid"""

    def __init__(self, w, h, DA, DB, ker_A, ker_B, f, k, delta_t):
        self.A = np.ones((h, w))
        self.B = np.zeros((h, w))
        # area seeded with B
        R=3
        for i in range(h//2 - R, h//2 + R + 1):
            for j in range(w//2 - R, w//2 + R + 1):
                if (i - h//2)**2 + (j - w//2)**2 <= R**2:
                    self.B[i, j] = 1
        self.w = w
        self.h = h
        self.DA = DA
        self.DB = DB
        self.ker_A = ker_A
        self.ker_B = ker_B
        self.f = f
        self.k = k
        self.delta_t = delta_t

    def update_concentrations(self):
        new_A = self.A
        new_B = self.B
        for i in range(1, self.h-1):
            for j in range(1, self.w-1):
                A = self.A[i, j]
                B = self.B[i, j]
                A_neighbors = self.A[i-1:i+2,j-1:j+2]
                B_neighbors = self.B[i-1:i+2,j-1:j+2]
                lap_A = np.sum(np.multiply(A_neighbors, self.ker_A))
                lap_B = np.sum(np.multiply(B_neighbors, self.ker_B))
                new_A[i, j] += (self.DA * lap_A - A*B*B + self.f*(1 - A))*self.delta_t
                new_B[i, j] += (self.DB * lap_B + A*B*B - (self.k + self.f)*B)*self.delta_t
                new_A[i, j] = max(new_A[i, j], 0)
                new_A[i, j] = min(new_A[i, j], 1)
                new_B[i, j] = max(new_B[i, j], 0)
                new_B[i, j] = min(new_B[i, j], 1)
        self.A = new_A
        self.B = new_B

    
    def plot(self):
        return plt.imshow(self.B - self.A, cmap="Greys")

ker_A = np.array([

    [.05, .2, .05], 
    [ .2, -1,  .2],
    [.05, .2, .05]
    ])
ker_B = np.array([
    [.05, .2, .05], 
    [ .2, -1,  .2],
    [.05, .2, .05]
    ])         

fig = plt.figure()

grid = Grid(100, 100, 1, .5, ker_A, ker_B, .0545, .062, 1)
im = grid.plot()

def update(*args):
    global grid
    grid.update_concentrations()
    im.set_array(grid.B - grid.A)
    return im,

ani = FuncAnimation(fig, update, interval=1, blit=True)
plt.show()



