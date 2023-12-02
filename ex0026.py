frase = input('Digite uma frase: ').strip().upper()
s=frase.count('A') +1 
d=frase.find('A')+1
e= frase.rfind('A')+1
# O +1 está sendo usado porque o programa começa a contar do 0
# na variavel 'e' foi usado rfind ou seja o find começa a procurar do lado direito para o esquerdo
print('A letra "a" aparece {} na frase e a primeira posição dela é {} e a ultima {}'.format(s,d,e))