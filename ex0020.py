from random import shuffle
a1 = input('Digte um nome: ')
a2 = input('Digite um nome: ')
a3 = input('Digite um nome: ')

lista = [a1, a2, a3]
shuffle(lista)
print('A ordem de aprensentação será {}.'.format(lista))