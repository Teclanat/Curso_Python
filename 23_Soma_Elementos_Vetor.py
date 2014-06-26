__author__ = 'Natanael'
#Trabalhando com Vetores

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

#Processamento
#Declarando as variáveis maior e menor
soma = 0


#Reiniciando o i
i = 0

#Selecionando o maior e menor elemento
while i<len(vetor):
    #Somando elementos do vetor
    soma = soma + vetor[i]
    i = i + 1

#Calculo da Média Aritmética dos Elementos
media = soma / numero_termos

#Saída de Dados - Impressão dos Resultados
print('Vetor Informado  :',vetor)
print('Soma dos Termos  :',soma)
print('Média Aritmética :',media)





