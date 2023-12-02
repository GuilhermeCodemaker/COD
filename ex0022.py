# Codigo analisando o nome.
n = input('Digite seu nome: ').strip()
print('Seu nome é',n)
print('Seu nome em maiusculo fica',n.upper())
print('Seu nome tem {} letras'.format(len(n)))
print('Seu primeiro nome tem {} letras'.format(n.find(' ')))  # Utilizando o .find e colocando espaço no parenteses faz com que o find conte e procure o primeiro espaço ou seja 
                                                              #  localizando o primeiro nome
