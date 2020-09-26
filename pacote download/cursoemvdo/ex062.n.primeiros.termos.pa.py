# Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra
# quando ele disser que quer mostrar 0 termos

ts=10
c=0
t=int(input('Qual o primeiro termo da PA? '))
r=int(input('Qual a razão da PA? '))
tt=1
while c<11:
    pa=t+c*r
    c=c+1
    print(pa, end=' -> ')
while tt!=0:
    if tt!=0:
        tt=int(input('Quantos termos deseja ver a mais? '))
        ts=ts+tt
        for b in range(pa+r,(pa+r)+tt*r,r):
            print(b, end=' -> ')
        pa=pa+tt*r
print('Acabou, finalizada com {} termos'.format(ts))


