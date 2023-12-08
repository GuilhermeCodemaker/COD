# O EXERCICIO É PARA QUE FIZESSE UM PROGRAMA QUE CALCULASSE A SOMA
# DE TODOS OS NUMEROS IMPARES QUE FOSSEM MULTIPLOS DE 3 
 
soma = 0 
# ISSO ATRIBUI A VARIAVEL O QUE ELA É ENTRE OS NUMEROS
for c in range(1,501,2):
    if c % 3 == 0:
# ^ DESSA FORMA EU FAÇO A CONDIÇÃO RECONHECER QUAL É MULTIPLO DE 3 
        soma = soma + c
# ^ DESSA FORMA A VARIAVEL VAI SOMAR ENTRE 0 E 500 
print('A soma de todos os valores solicitados que são multiplos de 3 é:\n  {}'.format(soma))