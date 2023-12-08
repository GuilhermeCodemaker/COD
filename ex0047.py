# ESTE PROGRAMA LÊ SOMENTE NUMEROS PARES E SOMA ELES 

soma = 0
cont = 0 
for c in range (1,7):
    n = int(input('Digite {} um numero: '.format(c)))
    if n % 2 == 0:
        soma = n + soma
        cont = cont + 1
print('Você informou {} numeros e a soma deles é de {}'.format(cont,soma))