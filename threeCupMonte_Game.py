#Simulando 'Three cup Monte"
    #Para isso, iremos ver como shuffle uma lista de forma aleatória. Veja:
    # example = [1,2,3,4,5,6,7]
    #from random import shuffle
    # shuffle(example)
    # print(example)

#Agora, faremos o jogo
mylist = [' ', 'O', ' '] #Aqui, o O simboliza a bolinha dentro do copo

from random import shuffle

#Primeiro, faremos uma função que irá embaralhar a lista e retornar seu resultado
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

mixedup_list = shuffle_list(mylist)

#Construindo uma função para que o usuário possa tentar acertar aonde está a bolinha
def player_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1 or 2")

    return int(guess)

myindex = player_guess()

#Criando uma função para conferir se o que o usuário passou está correto
def check_guess (mylist, guess):
    if mylist[guess] == 'O':
        print(f'Correct! \n{mylist}')
    else:
        print(f"Wrong guess! \n{mylist}")

check_guess(mixedup_list, myindex)