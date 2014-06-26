__author__ = 'Natanael'

#Definição de Funções no Python

#Definindo uma função para calcular o fatorial de um número qualquer

def fat(n):
    if n < 0:
        return "Erro: não existe fatorial para número negativo"
    elif n == 0:
        return 1
    else:
        fat = n
        for i in range(1,n):
            fat = fat * i
            return fat
#Fim da Função fat

#Executando a função fat(n)
n = int(input('Informe o número para calcular o fatorial: '))
fat = fat(n)

#Retornando o valor de fat
print('O valor de fatorial de ', n, ' é : ', fat)


