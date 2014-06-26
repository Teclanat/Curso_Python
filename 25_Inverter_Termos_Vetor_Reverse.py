__author__ = 'Natanael'
#Trabalhando com Vetores - Invertendo termos do vetor sem a função reverse

#Inicializando o vetor
vetor = []

numero_termos = int(input('Digite a quantidade de elementos a ser adicionada: '))
i = 0

#Entrada de Dados
while i < numero_termos:
    temp = int(input('Digite o elemento a ser adicionado: '))
    #Uso de append = adiciona um elemento no vetor
    vetor.append(temp)
    i = i + 1

#Saída de Dados - Impressão dos Resultados
print('Vetor Informado       :',vetor)
vetor.reverse()

#Imprimindo o vetor na ordem inversa
print('Vetor na Ordem Inversa:',vetor)

#Fim do Programa






