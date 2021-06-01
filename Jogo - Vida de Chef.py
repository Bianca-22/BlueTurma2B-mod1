#Participantes: Anderson, Bianca, Pedro
#Ideia: Essencialmente um jogo de memória que possui um restaurante com caixa, e o chefe (o player).
# Dividido em rodadas, a ordem dos pedidos é apresentada e o jogador tem que acertá-la. Cada acerto um bônus, cada erro, um ônus. Se o caixa zerar, o jogo finaliza.
#Desenvolvimento: Juntamos no famoso zap e discutimos por dois dias qual seria o conceito do jogo, esse foi o maior tormento. 
# De resto, revisamos o código original sempre que precisávamos de inspiração. Todos colaboramos a partir da divisão de tarefas e sugestões particulares.


#bibliotecas usadas no programa
import random
import time

class Rodadas():  #classe "Rodadas" definida, na qual irá regular a contagem de dias e rodadas no jogo 
    def __init__(self):
     self.rodada=1 # a variável rodada recebe 1  por valor-padrão
     self.dia=1 # variável dia também recebe 1 por valor-padrão
     

    def __str__(self):
     return f"Rodada {self.rodada}, Dia {self.dia}."
    def avanca_rodada(self, rodada): # método para avançar a quantidade de dias e rodadas 
       self.rodada += rodada  # self.rodada já foi definido tendo 1, agora será adicionado valor à variável caso a condição abaixo seja satisfeita 
       if(self.rodada > 4): # caso self.rodada seja maior a 4
           self.rodada -=3   # o programa tira 3 rodadas da variável
           self.dia += 1     # e adiciona 1

class Restaurante(): # A classe Restaurante define o caixa do jogo
    def __init__(self):
     self.caixa=400 # Caixa inicial tendo por padrão 400 (reais)
     
        


if(__name__ == "__main__"): # declaração de variáveis instanciadas
    rodadas = Rodadas()
    dinheiro = Restaurante()
    print("---"*12) #instruções e time.sleep para dar seguimento ao jogo
    print(f"\tINSTRUÇÕES DO JOGO: \n--> Seu dia como chefe supremo da gastronomia é dividido em 4 pedidos/rodadas. \n--> Ao iniciá-lo, um pedido será mostrado por 7 segundos no terminal!\n--> Seu papel é acertar a ordem do pedido!\n--> Cada erro será um cliente insatisfeito e um custo em dinheiro, cada acerto, um pagamento.\n--> Lembre-se, seu restaurante começa com R$400 reais em caixa! \n--> O jogo acaba se você zerar o orçamento do restaurante e levá-lo à falencia, colapsando o universo. \nEnjoy! ")
    print("---"*12)
    time.sleep(10)
    print("\n" * 10)
    print("***"*10)
    print("     É a "+str(rodadas)) #informação inicial da rodada e dia com concatenação
    print("***"*10)
    nome= input("Digite seu nome, chefe: ") # Dados pedido para o usuario, melhorando a experiência do jogo
    nome_restaurante= input("Escolha um nome para seu restaurante: ")
    print("~~~"*10) #uso dos dados no terminal
    print(f"Olá, Mestre das comidas {nome}.\nSeja bem-vindo ao seu império gastronômico, o: {nome_restaurante}'s! ") 
    print("~~~"*10)
    while True : #estrutura de repetição para o jogo continuar até que a condição para o break seja satisfeita ou pedida pelo jogador
     print("Painel de opções:")
     print("1- Preparar pedido!")
     print("2- Consultar painel do restaurante.")
     print("3- Sair.")
     opcoes=input("Qual a sua ação? ") #Entrada de dados do usuario para dar seguimento à opção selecionada
     if opcoes == "1": # abaixo, lista de todos os alimentos possíveis no cardápio do restaurante
         receita = ['Hamburguer', 'Salada', 'Batatas', 'Coca-cola','Pepsi','Pizza', 'Macarronada', 'Lasanha', 'Cerveja','Arroz', 
         'Acarajé', 'Açaí', 'Baião de dois', 'Suco de maracuja', "Suco de morango", 'Água mineral', "Feijoada", 'Bolo de rolo', "Pão de queijo" ]
         random.shuffle(receita) #opções para randomizar o pedido que será mostrado, com a biblioteca random 
         lista= random.sample(receita,4) #função .sample limita a quantidade de itens a ser mostrada
         print(f"Ordem do pedido: {lista}") #output do pedido ao usuário
         
         time.sleep(5)  #tempo para memorizar o pedido com a biblioteca time e função .sleep
         for i in range(0,50): #estrutura de repetição "for" usada para tirar o pedido da tela 
             print("\n" * 100)
         
         for i in range(len(lista)): #sequenciação da ordem da lista
             print("Digite a ordem: ")
             resp=str.capitalize(input()) #capitalize "à prova de usuário"
             if resp == lista[i]: #repetição de cada item, e estrutura "if" e "else" para validação da resposa 
                 print("Correto! +R$15!")
                 dinheiro.caixa += 15 #recompensa adicionada ao caixa
             else:
                 print("Errou. Seu cliente decidiu não pagar, você perdeu R$15!")
                 dinheiro.caixa -= 15 #ônus do erro retirado do caixa

         rodadas.avanca_rodada(1) 
         if(dinheiro.caixa<=0): # Se o caixa atingir o nivel de 0 reais a função print com um aviso será executada e o jogo encerrado com break
           print("Você faliu! O jogo será reiniciado em outro universo(Esse colapsou sem sua comida)!")
           break
           

         print(rodadas)   
     elif opcoes == "2": #opção 2 mostra os dados recebidos e o caixa do restaurante
    
       print("/~/"*15)
       print(f"{nome_restaurante}'s Império gastrômico, chefe {nome}. É a {rodadas} Você possui R${dinheiro.caixa} em caixa.")
       print("/~/"*15)     
     elif opcoes == "3": #opção 3 encerra o jogo
      break
     else: # caso nenhuma das opções dada no painel seja satisfeita, a mensagem de erro é acionada e o while repetido
      print("Opção inválida!")






