import math
Angulo = float(input('Valor do ângulo: '))
seno = math.sin(math.radians(Angulo))
# É NECESSARIO UTILIZAR math.radians porque o angulo está em graus
# E para o calculo dar certo precisa da conversão para radiano
print('O seno do ângulo {}° é de: {:.2f}'.format(Angulo,seno))
cosseno = math.cos(math.radians(Angulo))
print('O cosseno do ângulo {}° é de {:.2f}'.format(Angulo,cosseno))
tangente = math.tan(math.radians(Angulo))
print('A tangente do ângulo {}° é de {:.2f}'.format(Angulo,tangente))
