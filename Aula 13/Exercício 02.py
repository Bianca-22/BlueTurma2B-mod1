#Ex 02:
jogador = input('Digite o nome do jogador: ')
partidas = int(input('Digite o número de partidas desse jogador: '))
gols = []

for i in range(1, partidas+1):
    gols.append(int(input(f'Quantos gols foram feitos na partida {i}: ')))

totalGols = sum(gols)
print('Nome do jogador: ', jogador)
print('Partidas jogadas: ', partidas)
print('Lista de gols: ', gols)
print('Total de gols: ', totalGols)

dicionario = {'Nome': jogador, 'Partidas': partidas, 'Gol por partida': gols, 'Total de gols': totalGols}
print(dicionario)