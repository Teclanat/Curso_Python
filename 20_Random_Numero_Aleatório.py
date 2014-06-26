__author__ = 'Natanael'
#Biblioteca Random
import random
random.seed()

#Variáveis Utilizadas no Projeto
valor = random.randint(1,99)
chute = 0
tentativas = 0

while chute != valor:
    chute = int(input('Digite seu palpite: '))
    tentativas = tentativas + 1

    #Testando o chute
    if chute == valor:
        print('Parabéns! Você acertou em ',tentativas, ' tentativas.')

    elif chute < valor:
        print('Errou para menos na tentativa ',tentativas, ': ')
    else:
        print('Errou para mais na tentativa ',tentativas,': ')

