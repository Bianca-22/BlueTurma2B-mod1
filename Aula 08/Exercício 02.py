#Ex 02: Jogo da Forca
print('***********************************')
print('***Bem vindo ao jogo da Forca!!!***')
print('***********************************')

palavra_secreta = 'pirata'
letras_acertadas = ['_','_','_','_','_','_']
acertou = False
enforcou = False
erros = 0

print(letras_acertadas)

while not acertou and not enforcou:
    chute = input('Digite uma letra: ')
    if chute in palavra_secreta:
        posicao = 0
        for letra in palavra_secreta:
            if chute == letra:
                letras_acertadas[posicao] = letra
            posicao += 1
    else:
        erros += 1

    enforcou = erros == 6
    acertou = '_' not in letras_acertadas
    print(letras_acertadas)

if acertou:
    print('Você ganhou!!')
else:
    print('Você perdeu!!')
print('Fim de Jogo')