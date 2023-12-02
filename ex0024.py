frase = input('Digite a cidade que você nasceu: ').strip()
frase.lower()
print('Santo' in frase.title())

#Este exercicio também pode ser resolvido por
#frase = input('Em que cidade você nasceu? ').strip()
#print(frase[:5].upper()) == 'SANTO')
#dessa forma ^ jogaria a palavra pra upper caso tenha escrito errado
# e iria conferir com o == se a palavra escrita no começo da frase foi SANTO
 