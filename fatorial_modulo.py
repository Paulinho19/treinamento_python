# Informa o fatorial de qualquer número inteiro
from math import factorial

number = int(input('Digite o número: '))
result = number

print('O fatorial de {} é:'.format(number))
print('{}!'.format(number), end =' ')

while number > 0:
    print(number, end=' ')
    print('x' if number > 1 else ('='), end=' ')
    number-=1
print(factorial(result))
