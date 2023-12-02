d = float(input('Qual a distância da viagem? '))
m = 0.50 * d
mm = 0.45 * d
if d <= float('200'):
    print('O preço da viagem será R${:.2f}'.format(m))
else:
    print('O preço da viagem será R${:.2f}'.format(mm))

# Dá para simplificar mais isso ai
# if d <= 200
      #print('Sua passagem vai custar {} reais'.format(d*0.5))
# multiplicando dentro do format ao invés de criar uma variavel 