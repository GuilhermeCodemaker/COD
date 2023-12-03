from random import choice
from time import sleep
print('\033[35m -=-'* 30)
print('\033[mTente adivinhar o numero que o computador vai pensar!')
n = int(input('Escolha um número de 1 a 5: '))
s = choice([1,2,3,4,5])
sleep(2)
if n == s:
    print('\033[34mvocê ACERTOU PARABÉNS!!!!! \033[m')
else:
    print('\033[31mvocê ERROU o numero escolhido foi {} \033[m'.format(s))

print('\033[35m -=-' *30)

