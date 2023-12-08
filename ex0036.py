# ESTE PROGRAMA UTILIZA CONDIÇÕES ANINHADAS PARA FAZER O CADASTRO DE ALISTAMENTO MILITAR OBRIGATORIO.

h = input('Qual seu sexo m ou f (masculino ou feminino)? ')
if  h == 'f':
    print('Não há obrigatoriedade de mulheres se alistarem!')
    print('Se deseja continuar com o alistamento digite seu ano de nascimento')
ano = int(input(('Ano de nascimento: ')))
idade = 2023 - ano 
p = 18 - idade
print ('Você tem {} anos'.format(idade))
if idade == 18:
    print('Está no ano de seu alistamento!')
elif idade < 18:
    print('Falta {} anos para você ter que se alistar'.format(p))
else:
    print('Você já deveria ter se alistado há {} anos'.format(p*-1))
    print('Seu alistamento foi em {}'.format(ano+18))