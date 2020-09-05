# Crie um programa que tenha uma função chamda voto() que vai receber como parametro o ano de
# nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado,
# opcional ou obrigatório nas eleições

def voto(nasc):
    from datetime import datetime
    idade = datetime.now().year - nasc
    if idade>=18 and idade<65:
        frase = f'Com a idade {idade}: VOTO OBRIGATÓRIO'
    elif idade<18 and idade>=16 or idade>=65:
        frase = f'Com a idade {idade}: VOTO OPCIONAL'
    else:
        frase = f'Com a idade {idade}: VOTO NEGADO'
    return frase

nasc = int(input('Digite o ano de nascimento: '))
a = voto(nasc)
print(a)



'''
def voto(nasc):
    from datetime import datetime
    idade = datetime.now().year - nasc
    if idade >= 18 and idade < 65:
        print(f'Com {idade}: Voto obrigatório!')
    elif idade < 18 and idade >= 16 or idade >= 65:
        print(f'Com idade {idade}: Voto opcional!')
    else:
        print(f'Com {idade}: Voto negado!')


nasci = int(input('Ano de nascimento: '))
voto(nasci)'''
