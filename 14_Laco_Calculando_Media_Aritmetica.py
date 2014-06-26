__author__ = 'Natanael'
#Calcular a média artimética de um intervalo de números qualquer

#Variaveis
contador = 0
acumulador = 0

#Receber a quantidade de números
qtde = int(input('Informe a quantidade de números que será calculada: '))

#Início do Laço While
while contador < qtde:
    numero = int(input('Digite um valor inteiro para o nr: '))
    contador = contador + 1
    acumulador = acumulador + numero;

#Calculo da Média Aritmética
media = acumulador / qtde

#Exibição do Resultado
print('A média aritmética simples do conjunto informado é: ', media)

