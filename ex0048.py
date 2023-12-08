#PROGRESSÃO ARIMÉTICA

p1 = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
Pa = p1 + (10 - 1) * razao
for p1 in range(p1, Pa + razao ,razao):
    print( p1, end=('  '))