import random

class Lancar:
    def __init__(self):
        self.dado = ''
        self.moeda = ''

    def lanca_dado(self):
        self.dado = random.randint(1,6)
        print(self.dado)

    def lanca_moeda(self):
        self.moeda = random.randint(1,2)
        if self.moeda == 1:
            print('Deu cara!')
        else:
            print('Deu coroa!')