
import math
import os

print('------------------------------------------------------\n')

num = int(input('Digite um número: '))
ant = num - 1
suc = num + 1

print('\nO antecessor do número', num,'é: ', ant)
print('O sucessor do número', num,'é: ', suc, '\n')

print('------------------------------------------------------\n')

num2 = int(input('Digite um número: '))
double = num2 * 2
pow = num2 ** 3
square = math.sqrt(num2)

print('\nO dobro do número', num2,'é: ', double)
print('O valor do número', num2,'ao cubo é:', pow)
print('A raiz quadrada do número', num2,'é: ', square, '\n')

print('------------------------------------------------------\n')

num3 = int(input('Digite um número: '))
print('\nA tabuada do número', num3,'é: \n')

for cont in range(1, 11):
    print(num3, 'x {} = {}'.format(cont, num3*cont))

print('------------------------------------------------------\n')

os.system("pause")