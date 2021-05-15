# Ex 1: 
def soma(x,y,z):
    soma = x + y + z
    print (f'O resultado da sua soma é : {soma}')

x = int(input(' Escreva o primeiro número: '))
y = int(input(' Escreva o segundo número: '))
z = int(input(' Escreva o terceiro número: '))
soma(x, y, z)

# Ex 2:
def num():
    if num1 > 0:
        print('P')
    elif num1 < 0: 
        print('N')
    else:
        print('0')
num1 = int(input('Digite um número: '))
print('Este número é: ', end ='') 
num()

# Ex 3:
def somaImposto(taxaImposto, custo ):
    imposto = custo * int(taxaImposto) / 100
    custoFinal = custo + imposto
    return custoFinal
taxaImposto = input('Digite a taxa do imposto: ').replace('%', '')
custo = float(input('Digite o valor do produto: R$ '))
print(f'O valor total com imposto é de R${somaImposto(taxaImposto, custo):.2f}.')

# Ex 4:
def calcular_pagamento(qtd_hr, valor_hr):
  hora = float(qtd_hr)
  taxa = float(valor_hr)
  if hora <= 40:
      salario = hora * taxa 
  else:
      h_excd = hora - 40
      salario = 40 * taxa * (h_excd*(1.5 * taxa))
      return salario

str_horas = input('Digite as horas trabalhadas: ')
str_taxa = input('Digite a taxa: ')
salario_total = calcular_pagamento(str_horas, str_taxa)
print('O valor de seu rendimento é de: R$', salario_total)

# Ex 5:
def imc():
    peso = 75
    altura = 1.68
    imc = peso / (altura**2)
    print('O IMC é = {0:.2f}'.format(imc))

peso = float(input('Digite o peso do indivíduo: '))
altura = float(input('Digite a altura do indivíduo: ').replace(',','.'))
imc(peso, altura)

#Ex 6:
def classificacao(valor):
    if valor >=9:
        print('NOTA:A')
    elif valor >=8:
        print('NOTA:B')
    elif valor >=7:
        print('NOTA:C')
    elif valor >=6:
        print('NOTA:D')
    else:
        print('NOTA:F')
valor = float(input('Digite o valor:'))
classificacao(valor)

# Ex 7:
def menor(n1,n2):
    if a < b:
        print('{} é o menor!'.format(a))
    elif b < a:
        print('{} é o menor!'.format(b))
    else:
        print('SÃO IGUAIS!')
a = int(input('Digite o primeiro número:'))
b = int(input('Digite o segundo número:'))
menor(a, b)