# Ex 1:
def menor(v1,v2):
    if n1 < n2:
        print('{} é o menor!'.format(n1))
    elif n2 < n2:
        print('{} é o menor!'.format(n2))
    else:
        print('São iguais!')
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
menor(n1,n2)

# Ex 2:
def maior_soma(a, b, l):
    if n1 + n2 > limite:
        print('A soma entre {} e {} é maior que o limite!'.format(n1,n2))
    else:
        print('A soma entre {} e {} não é maior que o limite!'.format(n1,n2))
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
limite = int(input('Digite o limite:'))
maior_soma(n1, n2, limite)

#Ex 3:
def min(string):
    return string.lower()
string = str(input('Digite uma frase:'))
print(min(string))

#Ex 4:
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade <16:
        return f'Com {idade} anos VOTO:NEGADO'
    elif idade >=16 and idade <18:
        return f'Com {idade} anos VOTO:OPCIONAL'
    else:
        return f'Com {idade} anos VOTO:OBRIGATORIO'

nasc = int(input('Em que ano você nasceu:'))
print(voto(nasc))

#Ex 5:
def ficha(jog='<desconhecido>',gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

n = str(input('Nome do jogador:'))
g = str(input('Número de gols:'))

if g.isnumeric():
    g=int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)