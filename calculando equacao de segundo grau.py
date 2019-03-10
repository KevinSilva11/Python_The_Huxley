#Calculando equacao de segundo grau

a = float(input('Insira valor de a: '))
b = float(input('Insira valor de b: '))
c = float(input('Insira valor de C: '))

delta = b**2 -4*a*c

raizdelta = delta**0.5

print('Delta: ', delta)

if delta < 0:
    print('CONTA NÃO TEM SOLUÇÃO POR NÂO TER RAIZ REAL')

x1 = (-b+raizdelta)/2*a
x2 = (-b-raizdelta)/2*a


print('Raiz de delta: ', raizdelta)
print('Esse é o valor de x1: ',x1)
print('Esse é o valor de x2: ',x2)


#Mantem o programa aberto ate 5s
from time import sleep

print('O programa sera fechado em...')

l = [0, 1, 2, 3, 4, 5]
l.reverse()
for i in l:
        sleep(2)
        print (i)
print('Até logo')

