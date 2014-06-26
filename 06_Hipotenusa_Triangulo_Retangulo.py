__author__ = 'Natanael'

import math
#Programa para calcular a hipotenusa de um triangulo-retangulo qualquer
print("Cálculo de Hipotenusa de Triangulo Retângulo")
a = int(input("Informe o valor do lado A: "))
b = int(input("Informe o valor do lado B: "))

#Calculo da hipotenusa
h = math.sqrt(a * a + b * b)

#Exibição do Resultado
print("Hipotenusa = ",h )

