v = float(input('Velocidade na via: '))
c = (v -80 )*7
if v > 80:
    print('Você ultrapassou o limite de velocidade ao passar {:.2f}km deverá pagar R${:.2f}'.format(v,c))
else:
    print('Siga em frente!')

# A cada Km acima de 80 na via será pago 7.00 reais de multa

