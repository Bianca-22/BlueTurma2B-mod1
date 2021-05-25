#Ex 04:
nomes = []

for i in range(1000):
    a = input('Digite um nome para acrescentar á lista ou 0 para sair: ')
    if a == '0':
        break
    else:
        nomes.append(a)
nome = input('Digite um nome para ser buscado na lista: ').lower()
if nome in nomes:
    print(f'O nome {nome} está na lista!')
else: 
    print(f'O nome {nome}  NÃO está na lista!')