__author__ = 'Natanael'
#Implementação de Pesquisa Linear no Python
__author__ = 'Natanael'
#Trabalhando com Vetores - Invertendo termos do vetor sem a função reverse

#Inicializando o vetor
vetor = []
pares = []
impares = []
numero_termos = int(input('Digite a quantidade de elementos a ser adicionada: '))
i = 0
#Entrada de Dados - Colocando elementos dentro do vetor
while i < numero_termos:
    temp = int(input('Digite o elemento a ser adicionado: '))
    #Uso de append = adiciona um elemento no vetor
    vetor.append(temp)
    i = i + 1
i=0
posicao = -1
while i <len(vetor):
    if vetor[i] % 2 == 0:
        pares.append(vetor[i])
    else:
        impares.append(vetor[i])
    i = i + 1

print('Valor Recebido : ',vetor)
print('Valores Pares  : ',pares)
print('Valores Impares: ',impares)











