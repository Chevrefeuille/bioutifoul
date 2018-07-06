import matplotlib.pyplot as plt
from tools import utils as ut
from math import *


def construct_square(segment):
    "Construct a square with segment as its base"
    xA, yA = segment[0][0], segment[0][1]
    xB, yB = segment[1][0], segment[1][1]
    xC = cos(pi / 2) * (xB - xA) - sin(pi / 2) * (yB - yA) + xA
    yC = sin(pi / 2) * (xB - xA) + cos(pi / 2) * (yB - yA) + yA
    xD = cos(-pi / 2) * (xA - xB) - sin(-pi / 2) * (yA - yB) + xB
    yD = sin(-pi / 2) * (xA - xB) + cos(-pi / 2) * (yA - yB) + yB
    return [(xC, yC), (xD, yD), (xB, yB), (xA, yA)]

def compute_new_squares(square, angle):
    "Compute the two new square of the fractal process"
    xB, yB = square[1][0], square[1][1]
    xA = (square[0][0] + square[1][0]) / 2
    yA = (square[0][1] + square[1][1]) / 2
    rad_angle = pi * angle / 180
    xC = cos(rad_angle) * (xB - xA) - sin(rad_angle) * (yB - yA) + xA
    yC = sin(rad_angle) * (xB - xA) + cos(rad_angle) * (yB - yA) + yA
    square_left = construct_square([square[0], (xC, yC)])
    square_right = construct_square([(xC, yC), square[1]])
    return [square_left, square_right]

def compute_fractal(square, angle, iterations, step):
    squares_list = [square]
    if step < iterations:
        square_left, square_right = compute_new_squares(square, angle)
        squares_list += compute_fractal(square_left, angle, iterations, step + 1)
        squares_list += compute_fractal(square_right, angle, iterations, step + 1)
    return squares_list


init_square = [
    (0, 4),
    (4, 4),
    (4, 0),
    (0, 0)
]

fractal = compute_fractal(init_square, 75, 6, 0)

ut.draw_shapes(fractal)
