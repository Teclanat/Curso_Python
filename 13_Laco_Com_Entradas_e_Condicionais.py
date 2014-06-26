__author__ = 'Natanael'
#Exemplo: Recebendo uma quantidade de números qualquer para efetuar uma soma.

#Definindo o valor inicial das variáveis
contador = 0;
acumulador = 0;

#Recebendo a quantidade de números que será contada
quantidade = int(input('Informe a quantidade de números que será somada: '))

#Uso do While
while contador < quantidade:
    numero = int(input('Digite o valor numérico: '))
    contador = contador + 1
    acumulador = acumulador + numero

print('A soma dos números fornecidos é ', acumulador)


