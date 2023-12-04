s1 = int(input('Segmento 1: '))
s2 = int(input('Segmento 2: '))
s3 = int(input('Segmento 3: '))

if s1 < s2 + s3 or s2 < s3 + s1 or s3 < s1 + s2:
    print('Estes segmentos podem formar um triângulo!')
    if s1 == s2 == s3:
         print('Este triângulo é EQUILÁTERO!')
    elif s1 != s2 != s3 != s1:
        print('Este triângulo é ESCALENO')
    else:
        print('Este triangulo é ISÓSCELES')
else:
    print('Estes segmentos não podem formar um triângulo!')
print('-=-'*30)