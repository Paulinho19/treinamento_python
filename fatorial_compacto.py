# Informa o fatorial de qualquer número inteiro
number = int(input('Digite o número: '))
result = 1
print('O fatorial de {} é:'.format(number))
print('{}!'.format(number), end =' ')

while number > 0:
    print(number, end=' ')
    print('x' if number > 1 else ('='), end=' ')
    # armazena o resultado final     
    result*=number
    number-=1
print(result)
