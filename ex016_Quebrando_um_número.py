# exercicio 16 - Quebrando um número  
'''
Crie um programa que leia um número Real qualquer pelo teclado emostre na tela a sua fração inteira
'''
'''
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
'''
# Importando biblioteca 
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))
