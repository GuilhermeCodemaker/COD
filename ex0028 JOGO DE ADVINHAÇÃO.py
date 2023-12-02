from random import choice
from time import sleep
print('=-'*30)
print('Tente adivinhar o numero que o computador vai pensar!')
n = int(input('Escolha um número de 1 a 5: '))
s = choice([1,2,3,4,5])
sleep(3)
if n == s:
    print('você ACERTOU PARABÉNS!!!!!')
else:
    print('você errou o numero escolhido foi {}'.format(s))

print('=-'*30)
