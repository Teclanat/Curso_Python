__author__ = 'Natanael'
#Trabalhando com Vetores

#Inicializando o vetor
vetor = []

n = int(input('Digite a quantidade de elementos a ser adicionada: '))
i = 0

while i < n:
    temp = input('Digite o elemento a ser adicionado: ')
    #Uso de append = adiciona um elemento no vetor
    vetor.append(temp)
    i = i + 1
print('Vetor = ',vetor)


