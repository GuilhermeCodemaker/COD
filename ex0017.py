from math import sqrt
co = float(input('Diga o comprimento do cateto oposto: '))
ca = float(input('Diga o comprimento do cateto adjacente: '))
hp = sqrt(co**2+ca**2)
print('A soma do quadrado do cateto op {}cm e do cateto adj {}cm '.format(co,ca))
print('Resulta na hipotenusa que é {:.2f}cm'.format(hp))

# EXISTE TAMBÉM O METODO HYPOT QUE ESTÁ NA BIBLIOTECA DO MATH
# EXEMPLO math.hypot(co, ca) que já iria resolver a esquação dos catetos
# ENTÃO hp = math.hypot(ca, co)