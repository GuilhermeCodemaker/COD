# ESTE PROGRAMA UTILIZA CONDIÇÕES ANINHADAS PARA FAZER UM JOGO DE JOKENPO (PEDRA, PAPEL E TESOURA)

from random import randint
from time import sleep

print('Este é um jogo clássico PEDRA, PAPEL, TESOURA')
print('''Suas opções são:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')
escolhido = int(input('Faça Sua escolha: '))
print('JO'), sleep(1)
print('KEN'), sleep(1)
print('PO'), sleep(1)
computador = randint(0,2)

if computador == 0:
    if computador == 0 and escolhido == 0:
        print('Você escolheu PEDRA e o computador pedra você EMPATOU!')
    elif computador == 0 and escolhido == 1:
        print('Você escolheu PAPEL e o computador pedra você GANHOU!')
    elif computador == 0 and escolhido == 2:
        print('Você escolheu TESOURA e o computador pedra você PERDEU!')
    else:
        print('JOGADA INVALIDA')
if computador == 1:
    if computador == 1 and escolhido == 0:
        print('Você escolheu PEDRA e o computador PAPEL você PERDEU!')
    elif computador == 1 and escolhido == 1:
        print('Você escolheu PAPEL e o computador PAPEL você EMPATOU!')
    elif computador == 1 and escolhido == 2:
        print('Você escolheu TESOURA e o computador PAPEL você GANHOU')
    else:
        print('JOGADA INVALIDA')
if computador == 2:
    if computador == 2 and escolhido == 0:
        print('Você escolheu PEDRA e o computador TESOURA você GANHOU!')
    elif computador == 2 and escolhido == 1:
        print('Você escolheu PAPEL e o computador TESOURA você PERDEU!')
    elif computador == 2 and escolhido == 2:
        print('Você escolheu TESOURA e o computador TESOURA você EMPATOU!')
    else:
        print('JOGADA INVALIDA')