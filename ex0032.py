print('-=-'*30)
l1 = float(input('Segmento1: '))
l2 = float(input('Segumento2: '))
l3 = float(input('Segumento3: '))

if l1 < l2 + l3 or l2 < l3 + l1 or l3 < l1 + l2:
    print('Estes segmentos podem formar um triangulo!')
else:
    print('Estes segmentos não podem formar um triangulo!')
print('-=-'*30)