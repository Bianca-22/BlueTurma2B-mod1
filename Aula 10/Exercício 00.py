#Ex 0:
num = int(input('Digite um número: '))
num1 = int(input('Digite outro número: '))
soma = num + num1
while soma != 50:
    print('A soma desses números não é 50.')
    num = int(input('Digite um número novamente: '))
    num1 = int(input('Digite outro número novamente: '))
    soma = num + num1
print('A soma desses números é de 50.')