senha = 'superghoul'
usuario = input('Digite a senha: ')
while usuario != senha:
    print('Senha incorreta, tente novamente.')
    usuario = input('Digite a senha novamente: ')
print('Bem-vindo, vamos jogar um jogo de advinhação!')
from random import randint
aleatorio = randint(0, 20)
acertou = False
tentativas = 0
while not acertou:
    num = int(input('Diga um número entre 0 e 20: '))
    tentativas += 1 
    if num == aleatorio:
        acertou = True
    else:
        if num < aleatorio:
            print('O número pensado é maior, tente outra vez.')
        elif num > aleatorio:
            print('O número pensado é menor, tente outra vez.')
print(f'Você conseguiu advinhar depois de {tentativas} tentativas. Parabéns!!')