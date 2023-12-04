n = int(input('Digite um número: '))
print('[ 1 ]Converter para BINÁRIO ')
print('[ 2 ]Converter para OCTAL')
print('[ 3 ]Converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))

if opcao == 1:
  print('{} convertido para BINÁRIO {}'.format(n,(bin(n)[2:])))
elif opcao == 2:
  print('{} convertido para OCTAL {}'.format(n,oct(n)[2:]))
elif opcao == 3:
  print('{} convertido para HEXADECIMAL {}'.format(n,hex(n)[2:]))
  
  # O COLCHETE NO PRINT ESTÁ TRUNCANDO OU SEJA FATIANDO OS 2 PRIMEIROS DIGITOS
  # JÁ QUE OS DOIS PRIMEIROS DIGITOS SÃO DESNECESSÁRIOS PARA A INFORMAÇÃO 0b, 0o etc...
  # [2:] FATIANDO OS DOIS PRIMEIRO DIGITO
  