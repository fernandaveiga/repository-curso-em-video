# Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuario
# digitar o valor 999, que é a condição de parada. No final, mostre quantos numeros foram digitados e qual
# foi a soma entre eles

c=0
n=0
soma=0
n = int(input('Digite um número inteiro: '))
while n!=999:
    soma=soma+n
    c=c+1
    n=int(input('Digite um número inteiro: '))
print('''Você digitou 999, que é a condição de parada. 
A soma foi {} e foram digitados {} numeros'''.format(soma, c))

# Este exercicio pode ser resolvido colocando fora do while soma=soma-999 e c=c-1 e não colocando a pergunta
# duas vezes, só uma vez logo após o while