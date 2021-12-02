from methods import *
from ui import *


if __name__ == '__main__':
    x_range, y_range = get_params_and_solve_equation()
    show(x_range, y_range, label='smth-method')
    
    # shift + alt + A закомментить/раскомментить
    """    # params  для тестирования ручками без ввода с консоли 
    func = lambda x, y: -10 * y 
    num_steps = 3000
    a = 0
    b = 5
    y0 = 1
    mean_variance = True

    x_range, y_range = Euler_solution(func, a, b, y0, num_steps)
    show(x_range, y_range, 'Euler', 'red')
    
    x_range, y_range = Euler_Koshi_solution(func, a, b, y0, num_steps)
    show(x_range, y_range, 'Euler-Koshi')
        
    x_range, y_range = Runge_Kutta_solution(func, a, b, y0, num_steps, mean_variance)
    show(x_range, y_range, 'Runge-Kutta', 'black') """