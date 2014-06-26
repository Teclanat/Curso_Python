__author__ = 'Natanael'
#Implementação de Pesquisa Linear no Python
__author__ = 'Natanael'
#Trabalhando com Vetores - Invertendo termos do vetor sem a função reverse

#Inicializando o vetor
vetor = []
numero_termos = int(input('Digite a quantidade de elementos a ser adicionada: '))
i = 0
#Entrada de Dados - Colocando elementos dentro do vetor
while i < numero_termos:
    temp = int(input('Digite o elemento a ser adicionado: '))
    #Uso de append = adiciona um elemento no vetor
    vetor.append(temp)
    i = i + 1

#Entrada de Dados - Informar o elemento a ser pesquisado
elemento_procurado = int(input('Informe o elemento a ser pesquisado: '))

i=0
posicao = -1
while i <len(vetor):
    if elemento_procurado == vetor[i]:
        posicao = i
    i = i + 1

print('Valor Recebido : ',vetor)
print('Valor Procurado: ',elemento_procurado)

if posicao == -1:
    print('Elemento não encontrado...')
else:
    print('Elemento encontrado na posição ',posicao)

#Fim do programa










