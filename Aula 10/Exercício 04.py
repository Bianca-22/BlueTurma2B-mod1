palavra_secreta = 'borboleta'
lista = ['_','_','_','_','_','_','_','_','_']
acertou = False
enforcou = False
errou = 0
print(lista)
while not acertou and not enforcou:
    letra = input('Digite uma letra: ')
    if letra in lista:
        posicao = 0
        for abc in palavra_secreta:
            if letra == abc:
                lista[posicao] = abc
                posicao += 1
    else:
        errou += 1
    enforcou = errou == 6
    acertou = '_' not in lista
    print(lista)
if acertou:
    print('Você ganhou!')
else:
    print('Você perdeu!')
print('Fim de jogo!')