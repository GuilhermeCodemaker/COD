# ESTE PROGRAMA SIMULA UMA MAQUINA DE CARTÃO APLICANDO JUROS E DESCONTOS CONFORME A OPÇÃO ESCOLHIDA

print(10*'-=-','LOJAS PY',10*'-=-')
Preco_compra = float(input('Qual o preço da compra? ')) 
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

Opcao = int(input('Qual sua opção? '))

if Opcao == 1:
    print('A vista R${:.2f}'.format(Preco_compra - (Preco_compra*0.10)))
elif Opcao == 2:
    print('A opção foi à vista no cartão R${:.2f}'.format(Preco_compra - (Preco_compra*0.05)))
elif Opcao == 3:
    print('Duas vezes no cartão então fica duas vezes de R${:.2f}'.format(Preco_compra/2))
elif Opcao == 4:
     parcelas = int(input('Quantas paracelas serão? '))
     print('A opção foi parcelar no cartão então fica {}x de R${:.2f} COM JUROS'.format(parcelas , (Preco_compra + (Preco_compra*20/100))/parcelas))
     print('Sua compra de R${:.2f} vai custar R${:.2f} no final por conta de juros.'.format(Preco_compra , Preco_compra + (Preco_compra * 0.20 ) ))