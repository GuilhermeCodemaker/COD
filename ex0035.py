#Condições aninhadas para a conferir qual numero é maior que qual

c = int(input('Primeiro número: '))
v = int(input('Segundo número: '))

if c > v:
    print('O primeiro número é maior que o segundo')
elif c < v:
    print('O segundo número é maior que o primeiro')
elif c == v:
    print('Os dois valores são iguais')