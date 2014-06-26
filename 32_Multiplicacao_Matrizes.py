
def Multiplicar_Matrizes(A, B):
    """
    Função que retorna a matriz M, resultante da multiplicação das
    matrizes A e B.

    M só existirá se o número de colunas da matriz A for igual ao número
    de linhas da matriz B.
    """
    A_linhas = len(A) #Número de linhas que A possui
    A_colunas = len(A[0]) # Número de colunas que A possui
    B_linhas = len(B) # Número de linhas que B possui
    B_colunas = len(B[0]) # Número de colunas que B possui

    if A_colunas == B_linhas:
        comum = A_colunas # Número igual de colunas de A e linhas de B
        M = [[sum(A[m][n] * B[n][p] for n in range(comum)) \
            for p in range(B_colunas)] for m in range(A_linhas)]
        return M
    else:
        return -1 # Valor de erro


# Exemplo:
# A(2x3)
A = [[1, 0, 2],
     [-1, 3, 1],
     [1, 4, 2]]

# B(3x1)
B = [[3],
     [2],
     [1]]

# A(2x3) * B(3x1) = C(2x1)
C = Multiplicar_Matrizes(A, B)

# Exibindo a matriz C(2x1)

for linha in C:
    print
    for coluna in linha:
        print (coluna),