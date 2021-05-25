#Ex 05:
produto = 1
valores = []

while True:
    valor_produto = float(input('Preço do produto: R$ '))
    valores.append(valor_produto)
    produto += 1
    if valor_produto == 0:
        break
    continue
print('Total: R$ ', sum(valores))
dinheiro = float(input('Dinheiro: R$ '))
troco = dinheiro - sum(valores)
print(f'Troco: R$ {troco}')