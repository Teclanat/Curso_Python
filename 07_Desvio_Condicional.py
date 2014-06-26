__author__ = 'Natanael'
#Definindo para utf8
#coding:utf8

a = int(input('Informe o valor de a: '))
b = int(input('Informe o valor de b: '))
c = int(input('Informe o valor de c: '))

#Estrutura Condicional
if (a > b):
    if(a > c):
        print(u'O maior valor é A = ',a)
    else:
        print(u'O maior valor é C = ',c)
else:
    if(b > c):
        print(u'O maior valor é B = ',b)
    else:
        print('O maior valor é C = ',c)
