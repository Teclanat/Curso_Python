__author__ = 'Natanael'
"""
    Trabalhando com Grafos - Busca em Largura

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

    #Método dfs - Busca em Profundidade
    def dfs(self,inicio,fim):
        pilha = [] #podemos simular uma pilha (append, pop)
        self.listaVertices[inicio].regVisitado()
        pilha.append(inicio) #usado como push
        while len(pilha) != 0:
            elementoAnalisar = pilha[len(pilha)-1]
            #Visitando os vértices
            if elementoAnalisar == fim:
                print("Rota encontrada. O caminho é => ",end=''),
                for i in pilha: print(self.listaVertices[i].rotulo,' ', end='')
                print('\n')
                break

            v = self.Adjacente_Nao_Visitado(elementoAnalisar)
            if v == -1:
                pilha.pop()
            else:
                self.listaVertices[v].regVisitado()
                pilha.append(v)
        else:
            print('Caminho não encontrado. Busca sem sucesso')
        for i in self.listaVertices:
            i.Limpa()

    #Busca em Largura
    def bfs(self,inicio,fim):
        for i in self.listaVertices:
            i.Limpa()
        fila = []
        if inicio == fim:
            print("Início igual ao fim. Nada a fazer")
            input()
            return
        self.listaVertices[inicio].regVisitado()
        self.Mostra_Vertice(inicio)
        fila.append(inicio) #usado como push
        while len(fila) != 0:
            elementoAtual = fila.pop(0) # remove o primeiro elemento da fila
            v = self.Adjacente_Nao_Visitado(elementoAtual)
            while v != -1:
                if v == fim:
                    self.Mostra_Vertice(v)
                    print("Caminho encontrado: ")
                    return
                self.listaVertices[v].regVisitado()
                self.Mostra_Vertice(v)
                fila.append(v)
                v = self.Adjacente_Nao_Visitado(elementoAtual)
        else:
            print("Caminho não encontrado. Busca sem sucesso!")


if __name__ == "__main__":
    grf = Grafo()

    while True:
        print("Escolha sua opcao")
        print("(M) mostra, (V) Inserir Vertice (A) Inserir Arco (B)Busca DFS (L)Busca BFS (S) Sair")
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

        elif escolha =='b':
            r_inicio = str(input('Digite o rótulo do vértice de início do arco: '))
            inicio = grf.Localiza_Rotulo(r_inicio)
            if inicio== -1:
                print('Vértice não cadastrado. Cadastre o vértice primeiro. (Enter para prosseguir)')
                input()
                continue
            r_fim = str(input('Digite o rótulo do vértice de fim do arco: '))
            fim = grf.Localiza_Rotulo(r_fim)
            if fim == -1:
                print('Vértice não cafastrado. Cadastre o vértice primeiro. (Enter para prosseguir)')
                input()
                continue
            grf.dfs(inicio,fim)

        elif escolha == "l":
            r_inicio = input('Informe o rótulo de início da busca: ')
            r_fim =    input('Informe o rótulo do fim da busca   :')
            inicio = grf.Localiza_Rotulo(r_inicio)
            fim = grf.Localiza_Rotulo(r_fim)
            grf.bfs(inicio,fim)

        elif escolha == "s":
            break
        else:
            print("Entrada invalida - Pressione Enter")
            input()


