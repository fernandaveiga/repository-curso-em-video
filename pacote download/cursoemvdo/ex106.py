# Faça um mini sistema que utilize o interactive help do python. O usuário vai digitar o comando e
# o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará
# obs: use cores
comando = ''
from time import sleep
while True:
    if comando.lower() != 'fim':
        print('-'*24)
        comando = str(input('\33[1;33m  Função da biblioteca: \33[0;0m')).lower()
        print('-'*24)
        sleep(0.3)
        print('-'*33)
        print(f"\33[1;34m  Acessando o manual do comando '{comando}'\33[0;0m")
        print('-'*33)
        sleep(0.3)
        help(comando)
        sleep(0.3)
    if comando.lower() == 'fim':
        print('Até logo!')
        break
