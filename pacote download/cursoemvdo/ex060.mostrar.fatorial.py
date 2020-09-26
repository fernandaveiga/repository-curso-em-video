#Faça um programa que leia um numero qualquer e mostre o seu fatorial

n=int(input('Digite um fatorial: '))
f=1
for c in range(n,0,-1):
    f=f*c
    print('{}'.format(c), end=' ')
    print('x' if c>1 else '=', end=' ')
print(f)