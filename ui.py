import matplotlib.pyplot as plt 
from methods import *


def get_func():
    '''
    gets funcеion from terminal 
    return: lambda function 
    '''
    str_func = 'lambda ' + input('Введите зависимые переменные через запятую:\n') + ': ' + input('Введите функцию:\n')
    changes = {'cos': 'np.cos', 'sin': 'np.sin', 'exp':'np.exp', 'tan':'np.tg', 'cot': 'np.cot', 'log': 'np.log'}
    for change in changes:
        str_func = str_func.replace(change, changes[change])
    
    return eval(str_func)


def get_params():
    '''
    gets parameters from terminal
    return: list of parameters
    '''
    func = get_func()
    a = float(input('Введите начало интервала:\n'))
    b = float(input('Введите конец интервала:\n'))
    y0 = float(input('Введите значение y0 (условие Коши):\n'))
    num_steps = int(input('Введите желаемое кол-во шагов:\n'))
    method = int(input('Выберите желаемый метод решения:\n1 - метод Эйлера\n2 - метод Эйлера-Коши\n3 - метод Рунге-Кутты\n'))
    mean_variance = int(input('Вывести среднее отклонение?\n1 - да\n2 - нет\n'))
    return (func, a, b, y0, num_steps, method, mean_variance)

def solve_equation():
    '''
    solves equation and gets parameters from terminal
    return: np.array, np.array -  solution in the form of a list of arguments(x_range) and values(y_range)
    '''
    params = get_params()
    method = params[5]
    try: 
        if method == 1:
            return Euler_solution(*params)
        if method == 2:
            return Euler_Koshi_solution(*params)
        if method == 3: 
            return Runge_Kutta_solution(*params)
    except:
        print('Посчитать не удалось, но вы не расстраивайтесь :)')


def show(x_range, y_range, label='unknown', color='blue'):
    '''
    draws a graph of the dependence of y on x
    params:
    x - nd.array of x values
    y  - nd array if y values 
    label(optional) - str - name of graph
    color(optional) - str - color of graph 
    '''
    plt.plot(x_range, y_range, ".--", label=label, color=color)
    plt.legend(loc="best")
    plt.show()