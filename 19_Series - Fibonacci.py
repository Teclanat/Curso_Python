__author__ = 'Natanael'
#Gerando a Série de Fibonacci
atual = 0       #Valor Atual
anterior = 0    #Valor Anterior
proximo = 1     #Próximo Valor

#Entrada de Dados
q = int(input('Qual o valor máximo? '))

#Laço
while proximo < q:
    print(proximo)
    #Método Convencional

    #anterior = atual
    #atual = proximo
    #proximo = anterior + atual

    #Atribuição Múltipla (Recurso do Python)
    anterior,proximo = proximo, anterior + proximo



