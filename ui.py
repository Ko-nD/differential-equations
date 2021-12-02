import matplotlib.pyplot as plt 
from methods import *


def get_params_and_solve_equation():
    '''
    gets params and returns solution
    return: x_range, y_range - nd.array - arrays of values of a solved differential equation
    '''
    func = eval('lambda ' + input('Введите зависимые переменные через запятую:\n') + ': ' + input('Введите функцию:\n'))
    a = float(input('Введите начало интервала:\n'))
    b = float(input('Введите конец интервала:\n'))
    y0 = float(input('Введите значение y0 (условие Коши):\n'))
    num_steps = int(input('Введите желаемое кол-во шагов:\n'))
    method = int(input('Выберите желаемый метод решения:\n1 - метод Эйлера\n2 - метод Эйлера-Коши\n3 - метод Рунге-Кутты\n'))
    mean_variance = int(input('Вывести среднее отклонение?\n1 - да\n2 - нет\n'))
    if method == 1:
        return Euler_solution(func, a, b, y0, num_steps, mean_variance)
    if method == 2:
        return Euler_Koshi_solution(func, a, b, y0, num_steps, mean_variance)
    if method == 3: 
        return Runge_Kutta_solution(func, a, b, y0, num_steps, mean_variance)
    else: 
        print('Выбранный метод не поддерживается, всего доброго!')


def show(x_range, y_range, label='unknown', color='blue'):
    '''
    draws a graph of the dependence of y on x
    params:
    x - nd.array of x values
    y  - nd array if y values 
    label - optional - name of graph
    color - optional - color of graph 
    '''
    plt.plot(x_range, y_range, ".--", label=label, color=color)
    plt.legend(loc="best")
    plt.show()