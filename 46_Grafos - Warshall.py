__author__ = 'Natanael'
"""
    Trabalhando com Grafos - Algoritmo de Warshall

"""

class Vertice:
    def __init__(self, rotulo):
        self.rotulo = rotulo
        self.visitado = False

    def igualA(self,r):
        return r == self.rotulo

    def foiVisitado(self):
        return self.visitado

    def regVisitado(self):
        self.visitado = True

    def Limpa(self):
        self.visitado = False

class Grafo:
    #Metodo Construtor
    def __init__(self):
        self.numVerticesMaximo = 20
        self.numVertices = 0
        self.listaVertices = []
        self.matrizAdjacencias = []
        #Incluida a matriz ordenada
        self.matrizOrdenada = []
        for i in range(self.numVerticesMaximo):
            linhaMatriz=[]
            for j in range(self.numVerticesMaximo):
                linhaMatriz.append(0)
            self.matrizAdjacencias.append(linhaMatriz)

    #Metodo Adicionar_Vertice
    def Adicionar_Vertice(self,rotulo):
        self.numVertices += 1
        self.listaVertices.append(Vertice(rotulo))

    #Metodo Adicionar_Arco
    def Adicionar_Arco(self, inicio, fim):
        self.matrizAdjacencias[inicio][fim] = 1
        #Agora vamos apenas adicionar uma direção
        #self.matrizAdjacencias[fim][inicio] = 1

    #Metodo Mostra_Vertice
    def Mostra_Vertice(self, vertice):
        print(self.listaVertices[vertice].rotulo,end=' -> ')

    #Metodo Imprime Matriz
    def Imprime_Matriz(self):
        print('    ', end=''),
        for i in range(self.numVertices):
            print(self.listaVertices[i].rotulo,end=' ')
        for i in range(self.numVertices):
             print('\n',self.listaVertices[i].rotulo,' ',end='')
             for j in range(self.numVertices):
                 print(self.matrizAdjacencias[i][j],'',end='')
        print("\n")



      #Metodo Localiza_Rotulo
    def Localiza_Rotulo(self,rotulo_r):
        for i in range(self.numVertices):
            #print(rotulo_r)
            #print(self.listaVertices[i].rotulo)
            if(rotulo_r == self.listaVertices[i].rotulo):
                return i
        else:
            return -1

    #Método Adjacente_Nao_Visitado
    def Adjacente_Nao_Visitado(self,v):
        for i in range(self.numVertices):
            #Verifica se existem vértices adjacentes
            if self.matrizAdjacencias[v][i] == 1 and self.listaVertices[i].foiVisitado() == False:
                return i
        else:
            return -1


    def warshall(self):
        for i in range(self.numVertices):
            for j in range(self.numVertices):
                if self.matrizAdjacencias[i][j] == 1:
                    for z in range(self.numVertices):
                        if self.matrizAdjacencias[z][i] == 1:
                            self.matrizAdjacencias[z][j] = 1
        print('Fecho transitivo finalizado')
        self.Imprime_Matriz()





if __name__ == "__main__":
    grf = Grafo()

    while True:
        print("Escolha sua opcao")
        print("(m) Matriz, (v) Vertice (a) Arco (w)Warshall (s) Sair")
        escolha = str(input("Digite sua opcao: ")).lower()
        if escolha == 'm':
            grf.Imprime_Matriz()
        elif escolha == 'v':
            val = str(input("Digite o rotulo do arco a inserir: "))
            grf.Adicionar_Vertice(val)
        elif escolha == 'a':
            r_inicio = str(input("Digite o rotulo do vertice de inicio do arco: "))
            inicio = grf.Localiza_Rotulo(r_inicio)
            if inicio == -1:
                print("Vertice nao cadastrado. Cadastre o vertice primeiro.")
                input()
                continue
            r_fim = str(input("Digite o rotulo do vertice de fim do arco: "))
            fim = grf.Localiza_Rotulo(r_fim)
            if fim == -1:
                print("Vertice nao cadastrado, Cadastre o vertice primeiro")
                input()
                continue
            grf.Adicionar_Arco(inicio, fim)

        elif escolha =='w':
            grf.warshall()

        elif escolha == "s":
            break

        else:
            print("Entrada invalida - Pressione Enter")
            input()


