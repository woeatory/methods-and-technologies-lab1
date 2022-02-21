import math
import sys


def interactive_mode():
    try:
        a = float(input('a = '))
        b = float(input('b = '))
        c = float(input('c = '))
    except:
        print('Error. Expected a valid real number, got something else instead')
        input()
    equation = QuadraticEquation(a, b, c)
    equation.solve_equation()


def non_interactive_mode():
    file = sys.argv[1]
    try:
        f = open(file, 'r')
        line = f.readline()
        a, b, c = float(line[0]), float(line[2]), float(line[4])
        if a == 0:
            raise Exception('0 can\'t be zero')
    except:
        print('Wrong file format')
        input()
    equation = QuadraticEquation(a, b, c)
    equation.solve_equation()


class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def solve_equation(self):
        print(f'Equation is: ({self.a})x^2 + ({self.b})x + ({self.c}) = 0')

        D = self.b ** 2 - 4 * self.a * self.c
        if D < 0:
            print('There are 0 roots')
            return
        else:
            x1 = ((-self.b + math.sqrt(D)) / (2 * self.a))
            x2 = ((-self.b - math.sqrt(D)) / (2 * self.a))
            if x1 == x2:
                print('There is 1 root\n'
                      f'x1 = {x1}')
            else:
                print('There ara 2 roots\n'
                      f'x1 = {x1}\n'
                      f'x2 = {x2}')


if len(sys.argv) > 1:
    non_interactive_mode()
    input()
else:
    interactive_mode()
    input()

