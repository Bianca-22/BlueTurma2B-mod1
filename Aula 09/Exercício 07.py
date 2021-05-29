#Ex 07: Desafio
from random import randint
num = randint(1,100)
chance = 10

while True:
    chute = int(input('Adivinhe o número entre 1 e 100: '))
    chance -= 1
    if chute == num:
        print('Você acertou!')
        break
    elif chance < 1:
        print('Suas chances acabaram, você perdeu!')
        break
    else:
        if chute < num:
            print(f'O número {chute} é menor')
        else:
            print(f'O número {chute} é maior')
    print(f'Restam {chance} chances')