__author__ = 'Natanael'
#Programa para gerar uma série PA (Progressão Aritmética)
i = 0 #numero a ser impresso
r = 1 #razao da série

q = int(input('Qual o valor máximo? '))
while i<q:
    print(i)
    i = i + r
    r = r + 1


