# Crie um programa que leia o nome de cidade de nascimento de uma pessoa e diga se o inicio do nome
# da cidade é 'santo'

cidade = str(input('Digite o nome da cidade que você nasceu: ')).strip()
print('O primeiro nome da cidade que voce nasceu é SANTO?',cidade[0:5].upper() =='SANTO')