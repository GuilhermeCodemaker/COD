a = float(input('Qual a altura da sua parede? '))
l = float(input('Qual a largura da sua parede? '))
aa = a*l 
print('A dimensão da sua parede é de {}x{} e a sua área é de {}m²'.format(a,l,aa))
t = aa/2
print('Para pintar a parede ira precisar de {}L de tinta'.format(t))