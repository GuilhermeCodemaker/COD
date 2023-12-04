from datetime import date
ano = int(input('Qaul o ano de seu nascimento? '))
idade = ano - date.today().year
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print(' -Atleta MIRIM- ')
elif idade <= 14:
    print(' -Atleta INFANTIL- ')
elif idade <= 19:
    print(' -Atleta JUNIOR- ')
elif idade <= 25:
    print(' -Atleta SÊNIOR- ')
else:
    print(' -Atleta MASTER- ')