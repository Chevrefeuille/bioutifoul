import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random

def init():
    ax.set_xlim(-2.1820 , 2.6558)
    ax.set_ylim(0, 9.9983)
    return ln,


def apply_transformation(x, y, param):
    "Apply the affine tranformation with parameters param to the point (x, y)"
    mat = param[0:4].reshape((2, 2))
    vec = param[4:6].reshape((2, 1))
    X = np.array([x, y]).reshape((2, 1))
    new_x, new_y = (np.dot(mat, X) + vec).flatten()
    return new_x, new_y

def update(frame, transfo_param):
    last_x = xdata[-1]
    last_y = ydata[-1]
    r = random.uniform(0, 1)
    h, w = np.shape(transfo_param)
    curr_p = 0 
    for i in range(h):
        curr_p += transfo_param[i, 6]
        if r <  curr_p:
            new_x, new_y = apply_transformation(last_x, last_y, transfo_param[i])
            break
    xdata.append(new_x)
    ydata.append(new_y)
    ln.set_data(xdata, ydata)
    return ln,


transfo_param = np.array([
    [0, 0, 0, 0.16, 0, 0, 0.01],
    [0.85, 0.04, -0.04, 0.85, 0,  1.60, 0.85],
    [0.20, -0.26, 0.23, 0.22, 0, 1.60, 0.07],
    [-0.15, 0.28, 0.26, 0.24, 0, 0.44, 0.07]
])


fig, ax = plt.subplots()
xdata, ydata = [0], [0]
ln, = plt.plot([], [], 'g.', markersize=1, animated=True)

ani = FuncAnimation(fig, update, fargs=(transfo_param, ),
                    init_func=init, blit=True, interval=1)
plt.show()

