#Ex 6:
texto = input('Digite uma frase: ')
suaFrase = ''
for vogal in texto.lower():
    if vogal not in 'aeiou':
        suaFrase += vogal

print(suaFrase)