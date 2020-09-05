# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os
# espaços.

f=str(input('Digite uma frase: ')).strip().upper()
palavras=f.split()
juntou = ''.join(palavras)
inverso = ''

for letra in range(len(juntou) -1, -1, -1):
    inverso= inverso + juntou[letra]
print('A frase digitada foi {} e invertida é {}'.format(juntou,inverso))

if inverso==juntou:
    print('A frase digitada é palindromo!')
else:
    print('A frase digitada não é palindromo!')

#OU
#frase=str(input('Digite uma frase: ')).strip().upper()
#separar=frase.split()
#juntou= ''.join(separar)
#inverso=juntou[::-1]
#print('A frase digitada foi {} e o inverso é {}'.format(juntou,inverso))

#if juntou==inverso:
#    print('A frase digitada é palindromo')
#else:
#    print('A frase digitada não é palindromo')
