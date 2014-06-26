__author__ = 'Natanael'

#Função Recursiva = aquela que chama ela mesma

#Função para calculo de fatorial usando recursividade

def fat(n):
        if n<0:
            return 'Erro: nao existe fatorial de negativos'
        elif n==0:
            return 1
        else:
            return n * fat(n-1)

#Fim da função

#Utilização da Função

x = int(input('Informe um valor para calcular o fatorial: '))
fatorial = fat(x)

print('O fatorial é ', fatorial)

