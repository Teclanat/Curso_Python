__author__ = 'Natanael'
#Trabalhando com Vetores

#Inicializando o vetor
vetor = []

n = int(input('Digite a quantidade de elementos a ser adicionada: '))
i = 0

#Entrada de Dados
while i < n:
    temp = int(input('Digite o elemento a ser adicionado: '))
    #Uso de append = adiciona um elemento no vetor
    vetor.append(temp)
    i = i + 1

#Processamento
#Declarando as variáveis maior e menor
maior = vetor[0]
menor = vetor[0]

#Reiniciando o i
i = 0

#Selecionando o maior e menor elemento
while i<len(vetor):
    if vetor[i]<menor:
        menor = vetor[i]
    if vetor[i]>maior:
        maior = vetor[i]
    i = i + 1

#Saída de Dados - Impressão dos Resultados
print('Vetor Informado :',vetor)
print('Menor Valor     :',menor)
print('Maior Valor     :',maior)



