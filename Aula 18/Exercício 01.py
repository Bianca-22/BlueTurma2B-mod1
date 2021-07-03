class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel): #Classe com 3 atributos
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel =quantidadeCombustivel 

    def abastecerPorValor(self, valor): # Método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
        temp = valor / self.valorLitro #Arazenar total de litros
        self.alterarQuantidadeCombustivel(self.quantidadeCombustivel - temp)
        return temp

    def abastecerPorLitro(self, quantidade): # Método onde é informado a quantidade em litros de combustivel e mostra o valor a ser pago pelo cliente 
        temp = quantidade * self.valorLitro #Armazena o valor total a ser pago
        self.alterarQuantidadeCombustivel(self.quantidadeCombustivel - quantidade)
        return temp

    def alterarValor(self, valor): # Método Altera o valor do litro do combustivel
        self.valorLitro = valor

    def alterarCombustivel(self, combustivel): # Método Altera o tipo do combustivel
        self.tipoCombustivel = combustivel

    def alterarQuantidadeCombustivel(self, quantidade): #Método Altera a quantidade de combustivel restante na bomba
        self.quantidadeCombustivel = quantidade


gasolina = bombaCombustivel('Gasolina Aditivada', 6.15, 500)
print(vars(gasolina))
gasolina.alterarValor(6.11)
print(vars(gasolina))
gasolina.alterarCombustivel('Gasolina Supra')
print(vars(gasolina))
gasolina.alterarQuantidadeCombustivel(1000)
print(vars(gasolina))

#Abatecer 50 litros
litros = 50
print(f'O valor a ser pago para abastecer {litros} L é R$ {gasolina.abastecerPorLitro(litros):.2f}')
print(vars(gasolina))

#Abastecer 50 reais
valor = 50
print(f'O total de litros abastacidos com R$ {valor} é de {gasolina.abastecerPorValor(valor):.2f} L')
print(vars(gasolina))