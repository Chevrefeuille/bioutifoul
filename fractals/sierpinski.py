import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random

def init():
    ax.set_xlim(-1, 6)
    ax.set_ylim(-1, 6)
    return ln,

def update(frame, corners):
    last_x = xdata[-1]
    last_y = ydata[-1]
    rndm_corner = random.choice(corners)
    new_x = (last_x + rndm_corner[0]) / 2
    new_y = (last_y + rndm_corner[1]) / 2
    xdata.append(new_x)
    ydata.append(new_y)
    ln.set_data(xdata, ydata)
    return ln,



corners = [(0, 0), (5, 0), (2.5, 5)]

fig, ax = plt.subplots()
xdata, ydata = [3], [3]
ln, = plt.plot([], [], 'b.', markersize=1, animated=True)

ani = FuncAnimation(fig, update, frames=range(1000), fargs=(corners, ),
                    init_func=init, blit=True, interval=1)
plt.show()
