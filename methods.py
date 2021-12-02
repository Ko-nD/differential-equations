import numpy as np 


def Euler_solution(func, a, b, y0, num_steps, mean_variance=False):
    '''
    using Euler method for solving differential equation on the interval [a, b]
    params: 
    func - lambda function 
    a - const - start of the interval 
    b - const - end of the interval 
    y0 - const - initial condition of Koshi task
    num_steps - const - number of steps
    mean_variance (optional) - bool - flag for showing meen variance between exact func and solution 

    return: x_range, y_range - nd.array - arrays of values of a solved differential equation
    '''
    x_range = np.linspace(a, b, num_steps)
    y_range = np.zeros(num_steps)
    y_range[0] = y0
    h = x_range[1] - x_range[0]
    
    for i in range(num_steps-1):
        y_range[i + 1] = y_range[i] + h * func(x_range[i], y_range[i])

    if mean_variance:
        calc_mean_variance(func, x_range, y_range)

    return x_range, y_range


def Euler_Koshi_solution(func, a, b, y0, num_steps, mean_variance=False):
    '''
    using Euler-Koshi method for solving differential equation on the interval [a, b]
    params: 
    func - lambda function 
    a - const - start of the interval 
    b - const - end pf the interval 
    y0 - const - initial condition of Koshi task
    num_steps - const - number of steps
    mean_variance (optional) - bool - flag for showing meen variance between exact func and solution 

    return: nd.array - an array of values of a solved differential equation
    '''
    x_range = np.linspace(a, b, num_steps)
    y_range = np.zeros(num_steps)
    y_range[0] = y0
    h = x_range[1] - x_range[0]
    
    for i in range(num_steps-1):
        func_x_y = func(x_range[i], y_range[i])
        y_i = y_range[i]
        y_range[i + 1] = y_i + \
                h * (func_x_y + func(x_range[i + 1], y_i +  h * func_x_y)) / 2

    if mean_variance:
        calc_mean_variance(func, x_range, y_range)

    return x_range, y_range


def Runge_Kutta_solution(func, a, b, y0, num_steps, mean_variance=False):
    '''
    using Runge-Kutta method for solving differential equation on the interval [a, b]
    params: 
    func - lambda function 
    a - const - start of the interval 
    b - const - end pf the interval 
    y0 - const - initial condition of Koshi task
    num_steps - const - number of steps
    mean_variance (optional) - bool - flag for showing meen variance between exact func and solution 

    return: nd.array - an array of values of a solved differential equation
    '''
    x_range = np.linspace(a, b, num_steps)
    y_range = np.zeros(num_steps)
    y_range[0] = y0
    h = x_range[1] - x_range[0]
    
    for i in range(num_steps-1):
        func_x_y = func(x_range[i], y_range[i])
        x_i = x_range[i]
        y_i = y_range[i]
        k1 = h * func_x_y
        k2 = h * func(x_i + h/2, y_i + k1/2)
        k3 = h * func(x_i + h/2, y_i + k2/2)
        k4 = h * func(x_i + h, y_i + k3)
        y_range[i + 1] = y_i + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    
    if mean_variance:
        calc_mean_variance(func, x_range, y_range)
        
    return x_range, y_range


def calc_mean_variance(func, x_range, y_range):
    '''
    calculate and print mean variance between func and y_range
    params:
    func - lambda function
    x_range - nd.array of x values
    y_range - nd.array of y values
    '''
    # производная методом конечных разностей
    diff = (y_range[1::] - y_range[0:-1:]) / (x_range[1] - x_range[0])
    # вывод средней разности 
    print('Среднее отклонение: ', round(np.sum(abs(diff - func(x_range, y_range)[1::])), 2))