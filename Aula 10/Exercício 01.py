senha = 'superghoul'
usuario = input('Digite a senha: ')
while usuario != senha:
    print('A senha está incorreta!')
    usuario = input('Digite a senha novamente: ')
    continue
print('A senha está correta! Bem vindo(a)!')