import os
from pynput import keyboard

vez = 0
cima = 0
esquerdo = 0
ponteiro = 'o'
jogadas = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

def limpar():
    os.system('clear')

def tabuleiro(lista):

    global vez

    print("####  JOGO DA VELHA  ####")

    print("(x) é a vez do Jogador 1")
    print("(+) é a vez do Jogador 2")

    print("============")

    print(" {0} | {1} | {2} ".format(lista[0][0], lista[0][1], lista[0][2]))
    print("---|---|---")
    print(" {0} | {1} | {2} ".format(lista[1][0], lista[1][1], lista[1][2]))
    print("---|---|---")
    print(" {0} | {1} | {2} ".format(lista[2][0], lista[2][1], lista[2][2]))

    print("===========")
    print("\nAgora é a\nvez do Jogador {0}".format(vez+1) )
    print("===========")

def jogar():

    limpar()

    def evento(key):

        global vez, cima, esquerdo, jogadores, jogadas

        limpar()

        if key == keyboard.Key.left:
            if esquerdo > 0:

                if jogadas[cima][esquerdo] == ponteiro:
                    jogadas[cima][esquerdo] = ' '

                esquerdo -= 1

                if jogadas[cima][esquerdo] == ' ':
                    jogadas[cima][esquerdo] = ponteiro

        elif key == keyboard.Key.right:
            if esquerdo <= 1:

                if jogadas[cima][esquerdo] == ponteiro:
                    jogadas[cima][esquerdo] = ' '

                esquerdo += 1

                if jogadas[cima][esquerdo] == ' ':
                    jogadas[cima][esquerdo] = ponteiro
        
        elif key == keyboard.Key.down:
            if cima <= 1:

                if jogadas[cima][esquerdo] == ponteiro:
                    jogadas[cima][esquerdo] = ' '

                cima += 1

                if jogadas[cima][esquerdo] == ' ':
                    jogadas[cima][esquerdo] = ponteiro
        
        elif key == keyboard.Key.up:
            if cima > 0:

                if jogadas[cima][esquerdo] == ponteiro:
                    jogadas[cima][esquerdo] = ' '

                cima -= 1

                if jogadas[cima][esquerdo] == ' ':
                    jogadas[cima][esquerdo] = ponteiro

        elif key == keyboard.Key.enter:
            if jogadas[cima][esquerdo] == ponteiro:

                if vez == 0:
                    jogadas[cima][esquerdo] = 'x'
                    vez = 1

                elif vez == 1:
                    jogadas[cima][esquerdo] = '+'
                    vez = 0
        
        for lista in jogadas:

            if lista == ['x', 'x', 'x']:
                print('O Jogador {0} ganhou'.format(vez+1))
                return False

            elif lista == ['+', '+', '+']:
                print('O Jogador {0} ganhou'.format(vez+1))
                return False

        tabuleiro(jogadas)

        if jogadas[0][0] == 'x' and jogadas[1][1] == 'x' and jogadas[2][2] == 'x':
            print('O Jogador {0} ganhou'.format(vez+1))
            return False
        
        elif jogadas[0][0] == '+' and jogadas[1][1] == '+' and jogadas[2][2] == '+':
            print('O Jogador {0} ganhou'.format(vez+1))
            return False

        elif jogadas[2][2] == '+' and jogadas[1][1] == '+' and jogadas[0][0] == '+':
            print('O Jogador {0} ganhou'.format(vez+1))
            return False

        elif jogadas[2][2] == 'x' and jogadas[1][1] == 'x' and jogadas[0][0] == 'x':
            print('O Jogador {0} ganhou'.format(vez+1))
            return False

        elif jogadas[0][2] == 'x' and jogadas[1][1] == 'x' and jogadas[2][0] == 'x':
            print('O Jogador {0} ganhou'.format(vez+1))
            return False

        elif jogadas[0][2] == '+' and jogadas[1][1] == '+' and jogadas[2][0] == '+':
            print('O Jogador {0} ganhou'.format(vez+1))
            return False

    tabuleiro(jogadas)

    with keyboard.Listener(on_press=evento) as listener:
        try:
            listener.join()
        except Exception as e:
            print(e.args[0])


jogar()
