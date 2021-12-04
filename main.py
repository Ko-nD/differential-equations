from methods import *
from ui import *


if __name__ == '__main__':
    x_range, y_range = solve_equation()
    show(x_range, y_range, label='smth-method')