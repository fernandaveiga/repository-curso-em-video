# Faça um programa que tenha uma função chamada escreva(), que receba um texto
# qualquer como parametro e mostre uma mensagem com tamanho adaptável.

def escreva(frase):
    a = len(frase) + 4
    print('-' * a)
    print(f'  {frase}')
    print('-' * a)


escreva('NÃO TO NEM AQUI')
escreva('NUNCA NEM VI')
escreva('NUM SEI SÓ SEI QUE FOI ASSIM')
escreva('AH NÃO')