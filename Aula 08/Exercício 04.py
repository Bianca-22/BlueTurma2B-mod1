#Ex 4:
frase = input("Digite uma frase: ")
vogais = []
cont = 0

for frase1 in frase:
    if frase1 in 'aeiou':
        vogais.append(frase1)
        cont += 1
print(f'Vogais:{vogais}')
print(f'Quantidade:{cont}')