import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
import argparse

def init():
    ax.set_aspect('equal')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    return ln,

def update(frame, R, r, rho, dt):
    l, k = rho / r, r / R
    t = frame * dt
    xdata.append(R * ((1 - k) * math.cos(t) + l * k * math.cos(t * (1 - k) / k)))
    ydata.append(R * ((1 - k) * math.sin(t) - l * k * math.sin(t * (1 - k) / k)))
    ln.set_data(xdata, ydata)
    return ln,

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-R", "--outer_circle_size", help="size of the outer circle", type=float, default=5)
    parser.add_argument("-r", "--inner_circle_size", help="size of the inner circle", type=float, default=1.5)
    parser.add_argument("-rho", "--eccentricity", help="eccentricity", type=float, default=2)
    args = parser.parse_args()

    fig, ax = plt.subplots()
    xdata, ydata = [], []

    ln, = plt.plot([], [], 'b.', markersize=1, animated=True)

    ani = FuncAnimation(fig, update, fargs=(args.outer_circle_size, args.inner_circle_size, args.eccentricity, 0.1),
                    init_func=init, blit=True, interval=100)
    plt.show()