__author__ = 'Natanael'
#Calcular uma Equação de 2º Grau

import math

#Entrada de Dados
a = int(input('Informe o valor para o termo a: '))
b = int(input('Informe o valor para o termo b: '))
c = int(input('Informe o valor para o termo c: '))

#Calculo do Delta
delta = b * b - 4 * a * c

#Caso o Delta seja menor que 0
if(delta<0):
    print('A equação não possui raízes reais')
#Caso o Delta seja igual a 0
elif(delta==0):
    raiz = (-1 * b + math.sqrt(delta))/(2*a)
    print('A equação possui somente uma raiz que vale: ',raiz)
#Caso o Delta seja maior que 0
elif(delta>0):
    raiz1 = (-1*b + math.sqrt(delta)/(2*a))
    raiz2 = (-1*b - math.sqrt(delta)/(2*a))
    print('As duas raízes da equação são: ',raiz1, " e ",raiz2)


