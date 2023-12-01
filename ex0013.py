sb = float(input('Qual seu salário base? R$'))
a = sb*15/100
p = sb + a 
print('O salário base desse trabalhador é de R${}'.format(sb))
print('Com o acrecimo de 15% que é o equivalente a R${}\nO salário atual será R${}'.format(a,p))