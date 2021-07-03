class Ingresso:
    def __init__(self,valor):
        self.__valor = valor

    def imprimirValor(self):
        return self.__valor

class IngressoVIP(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.adicional = adicional
        return self.valor + self.adicional

ingresso = Ingresso(50)
ingressoVIP = IngressoVIP(100)
print(f'O valor do ingresso é de R${ingresso}\nO valor do ingresso VIP é de R${ingressoVIP}')