__author__ = 'Natanael'
#Simulando um Relógio Digital com Laços de Repetição
import os #Biblioteca do sistemaa operacional
os.system("cls")

i = 0
while i < 24:
    j = 0
    while j < 60:
        k = 0
        while k < 60:
            os.system("cls") #Limpa a tela
            print(i,":",j,":",k)
            k = k + 1
        j = j + 1
    i = i + 1


