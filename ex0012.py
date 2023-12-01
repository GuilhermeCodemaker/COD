p = float(input('Qual o preço do produto? R$'))
s = (p*5)/100
f = p - s
print('Este produto custa R${:.2f}\nCom o desconto de 5% que é de R${:.2f}\nO produto custará R${:.2f}'.format(p,s,f))