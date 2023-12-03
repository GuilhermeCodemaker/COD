vc = float(input('Qual o valor da casa?R$ '))
sl = float(input('Qual seu salário mensal?R$ '))
qa = float(input('Em quantos anos será paga? '))

m = qa*12
valorpc = (vc/m)
por = sl*30/100
print('O valor da parcela mensal é de R${:.2f}'.format(valorpc))
if por >= valorpc:
    print('O emprestimo foi aprovado!')
else:
    print('O emprestimo foi negado!')