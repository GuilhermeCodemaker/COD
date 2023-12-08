# TABUADA UTILIZANDO LAÇOS DE REPETIÇÃO

n = int(input('Digite o numero que você quer calcular '))
for c in range(0,11):
    print('A Tabuada do {} x {} é igual a = '.format(n,c),n * c)