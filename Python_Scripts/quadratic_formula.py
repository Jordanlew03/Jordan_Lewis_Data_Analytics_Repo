import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
print('\n', end = '')

print('Equation:', a, end = '')
print('x^2', end = '')
print(' +', b, end = '')
print('x +', c, '= 0')

print('Discriminant:', math.pow(b,2) - 4 * a * c)
print('Solution #1:', (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2*a))
print('Solution #2:', (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2*a))