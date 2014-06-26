__author__ = 'Natanael'
#Uso de Break, continue, else
# break = quebra o laço mais interno de um for ou while
# continue = continua o próximo passo do laço mais interno
# else = laços podem ter um else executado quando se encerra por exaustão da lista, no caso do for
# ou quando a condição se torna falsa (no caso do while) mas nunca quando o laço é encerrado por break


#Exibe todos os números primos até o valor limite n
q = int(input('Digite um número limite: '))
for n in range(2,q): #Se não colocar o valor do passo ele fica com passo 1
    for x in range(2,n):
        if n % x == 0:
            print(n,' igual a ',x,' * ',n/x)
            break
    else:
        #Chegou até aqui por não executar o break
        print(n,' é um número primo')



