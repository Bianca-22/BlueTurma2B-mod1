#Ex 01:
num = int(input('Digite um número: '))
num1 = int(input('Digite outro número: '))

if num + num1:
    print('A soma desses números é de', num+num1)
if num * num1:
    print('A multiplicação desses números é de', num*num1)
if num // num1:
    print('A divisão inteira desses números é de', num//num1)
if num < num1:
    print(num1, 'é maior que', num)
if num > num1:
    print(num, 'é maior que', num1)
soma = num+num1
if soma % 2 == 0:
    print('A soma desses números é par.')
if soma % 2 != 0:
    print('A soma deses números é impar.')
mult = num * num1
if mult <= 40:
    print('A multiplicação entre esses números não é maior que 40')
elif mult > 40:
    print(mult/(num//num1))
