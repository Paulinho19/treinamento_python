# Informa o fatorial de qualquer número inteiro
number = int(input('Digite o número: '))
result = 1
print('O fatorial de {} é:'.format(number))
print('{}!'.format(number), end =' ')

while number > 0:
    print(number, end=' ')
    if number > 1:
        print('x', end=' ')
    else:
        print('=', end=' ')
    # armazena o resultado final     
    result*=number
    
    number-=1
print(result)
