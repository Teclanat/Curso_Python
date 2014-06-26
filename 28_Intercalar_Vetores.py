__author__ = 'Natanael'
#Trabalhando com Vetores - Intercalar
vetor1 = []
vetor2 = []
vetor3 = []

#Entrada de Dados - Colocando elementos dentro do vetor1
numero_termos_1 = int(input('Digite a quantidade de elementos do vetor 1: '))
i = 0
while i < numero_termos_1:
    temp = int(input('Digite o elemento a ser adicionado: '))
    #Uso de append = adiciona um elemento no vetor
    vetor1.append(temp)
    i = i + 1

#Entrada de Dados - Colocando elementos dentro do vetor2
numero_termos_2 = int(input('Digite a quantidade de elementos do vetor 2: '))
i = 0
while i < numero_termos_2:
    temp = int(input('Digite o elemento a ser adicionado: '))
    #Uso de append = adiciona um elemento no vetor
    vetor2.append(temp)
    i = i + 1

#Processamento - Intercalando os valores dos vetores recebidos

i = 0 #Posicao do vetor 3
j = 0 #Posicao do vetor 1
k = 0 #Posicao do vetor 2
vetor3 = []

#While da Intercalacao
while i< len(vetor1)+len(vetor2):
    if j<len(vetor1):
        vetor3.append(vetor1[j])
        i = i + 1
        j = j + 1

    if k<len(vetor2):
        vetor3.append(vetor2[k])
        i = i + 1
        k = k + 1

#Saída dos Resultados
print('Vetor 1 Recebido     :',vetor1)
print('Vetor 2 Recebido     :',vetor2)
print('Vetor 3 Intercalado  :',vetor3)

#Fim do Programa



















