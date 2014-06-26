__author__ = 'Natanael Garcia Rodrigues'

#Pesquisa binária = é um algoritmo conhecido para pesquisar um valor em uma lista ordenada.
# ordem de Θ(log2n),

def Pesquisa_Binaria(vetor, x):
   superior = len(vetor)
   inferior = 0
   anterior = -1
   if x < vetor[0]:
       return -1 #Retorna -1 quando não encontrar
   while 1:
       meio = (inferior + superior) // 2
       cursor = vetor[meio]
       if x == cursor:
           return meio
       if meio == anterior:
           return - 2 - meio
       elif x < cursor:
           superior = meio
       else:
           inferior = meio
       cursor = meio


#Exemplo de aplicação da função
vetor = [1,2,3,4,5,6,7,8,9,10]
x = 5
pesquisa = Pesquisa_Binaria(vetor, x)
print(pesquisa)
