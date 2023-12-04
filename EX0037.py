n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))

cal = (n1+n2)/2

if cal > 7.0:
    print('O aluno foi APROVADO sua média é de {}'.format(cal))
elif cal < 5.0:
    print('O aluno foi REPROVADO {}'.format(cal))
elif cal >= 5 or cal < 7:
    print('O aluno está de RECUPERAÇÃO sua média é de {}'.format(cal))