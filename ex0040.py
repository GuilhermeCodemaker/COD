#ESTE PROGRAMA FAZ CALCULO DE IMC INDICE DE MASSA CORPORAL

a = float(input('Qual sua altura? '))
p = float(input('Qual seu peso? '))
IMC = p / (a ** 2)

if IMC <= 18.5:
    print('Você está abaixo do Peso ideal!')
elif IMC < 25 and IMC > 18.5:
    print('Você está no peso ideal!')
elif IMC < 30 and IMC > 25:
    print('Você está Sobrepeso ou seja gordo!')  
elif IMC < 40 and IMC > 30:
    print('VOCÊ ESTÁ OBESO!')
elif  IMC > 40:
    print('OBESIDADE MORBIDA!!!!')
print('Seu IMC é de {:.1f}'.format(IMC))
