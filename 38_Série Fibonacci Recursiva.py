__author__ = 'Natanael'

#Implementação da Série Fibonacci Recursiva

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n -2)

#Fim da função

x = int(input('Digite o tamanho da série: '))
print('Série gerada: ')

for i in range(1, x+1):
    print(fib(i),' ',end='')
