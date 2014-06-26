__author__ = 'Natanael'
#Importar Funções do SO
import os
os.system('cls') #Importando o comando clear no windows

#Verificando se um numero é primo
valor = int(input('Informe um valor para verificar se é primo: '))

#Variaveis
i = 2
nr_divisores = 0
nr_comparacoes = 0

#Iniciando a verificação
while i <= valor/2:
    nr_comparacoes = nr_comparacoes + 1
    if valor % i == 0:
        nr_divisores = nr_divisores + 1
    i = i + 1

if nr_divisores == 0:
    print('O número informado é um número primo.')
    print('Comparações: ',nr_comparacoes)
    print('Divisões: ', nr_divisores)
else:
    print('O número informado não é um número primo.')
    print('Comparações: ',nr_comparacoes)
    print('Divisões: ', nr_divisores)



