class pessoa():
    def __init__(self, nome,sobrenome,idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    def dados(self):
        print(self.nome)
        print(f'Sobrenome:{self.sobrenome} e a idade é {self.idade}')

serzinho = pessoa('Bianca','Monteiro',19)