#Ex 3:
resp = []
resp.append(input('Telefonou para a vítima? (Sim ou Não) '))
resp.append(input('Esteve no local do crime? (Sim ou Não) '))
resp.append(input('Mora perto da vítima? (Sim ou Não) '))
resp.append(input('Devia para a vítima? (Sim ou Não) '))
resp.append(input('Já trabalhou com a vítima? (Sim ou Não) '))
resp_sim = resp.count('Sim'.lower())
if resp_sim == 2:
    print('Suspeito(a)')
elif resp_sim == 3 and resp_sim == 4:
    print('Cúmplice')
elif resp_sim == 5:
    print('Assassino(a)')
else:
   print('Inocente')