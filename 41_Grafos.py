__author__ = 'Natanael'
"""
    Trabalhando com Grafos
"""

class Vertice:
    def __init__(self, rotulo):
        self.rotulo = rotulo
        #self.visitado = False

    def visitado(self):
        self.visitado = True

class Grafo:
    #Metodo Construtor
    def __init__(self):
        self.numVerticesMaximo = 20
        self.numVertices = 0
        self.listaVertices = []
        self.matrizAdjacencias = []
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
        self.matrizAdjacencias[fim][inicio] = 1

    #Metodo Mostra_Vertice
    def Mostra_Vertice(self, vertice):
        print(self.matrizAdjacencias[vertice].rotulo)

    #Metodo Imprime Matriz
    def Imprime_Matriz(self):
        print('....', end=''),
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



if __name__=="__main__":
    grf=Grafo()

    while True:
        print("Escolha sua opcao")
        print("(M) mostra, (V) Inserir Vertice (A) Inserir Arco (S) Sair")
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
        elif escolha == "s":
            break
        else:
            print("Entrada invalida - Pressione Enter")
            input()


