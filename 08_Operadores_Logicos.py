__author__ = 'Natanael'
#Definindo para utf8
#coding:utf8

a = int(input('Informe o valor de a: '))
b = int(input('Informe o valor de b: '))
c = int(input('Informe o valor de c: '))

#Estrutura Condicional usando operadores Lógicos
if(a>b) and (a>c):
    print('O maior valor é A = ', a)

if(a>b) and (a<c):
    print('O maior valor é C = ', c)

if(a<b) and (b>c):
    print('O maior valor é B = ', b)

if(a<b) and (b<c):
    print('O maior valor é C = ', c)
