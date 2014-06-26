def permutacoes(lista):
 """ Dada uma lista, retorna uma lista de listas,
 onde cada elemento é uma permutação da lista
 original """
 if len(lista) == 1: # Caso base
    return [lista]
 primeiro = lista[0]
 resto = lista[1:]
 resultado = []
 for perm in permutacoes(resto):
    for i in range(len(perm)+1):
        resultado += \
            [perm[:i]+[primeiro]+perm[i:]]
 return resultado

lista = [1,2,3,4,5,6,7]
a = permutacoes(lista)
print(len(a))

