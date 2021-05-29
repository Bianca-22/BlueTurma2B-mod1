#Ex 06:
materia = int(input('Quantas matérias você tem? '))
lista = []
for i in range(1,materia+1):
    nota = float(input('Qual a nota na matéria: '))
    lista.append(nota)
    print(lista)
    print('A média geral do aluno é de ', sum(lista)/4)