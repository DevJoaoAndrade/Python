import os
from time import sleep
from random import randint

placar = {'jogador': 0, 'computador': 0, 'empate':0}

while True:
    print('Bem vindo(a) ao jogo pedra papel e tesoura!')
    menu_inicial = input('1-Iniciar jogo\n2-Encerrar\nDigite aqui: ')
    if menu_inicial == '1':
        quantidade_rodadas = input('Digite a quantidade de rodadas: ')
        quantidade_rodadas = int(quantidade_rodadas) if quantidade_rodadas.isdigit() else 0
        
        if quantidade_rodadas > 0:
            for rodada in range(quantidade_rodadas):
                escolha_jogador = input('0-Pedra, 1-Papel, 2-Tesoura\nDigite aqui: ')
                escolha_jogador = int(escolha_jogador) if escolha_jogador.isdigit() else 3
                escolha_computador = randint(0, 2)
                
                if escolha_jogador == escolha_computador:
                    placar['empate'] +=1
                    print(f'{rodada} empate')                    
                
                if escolha_jogador == 0:
                    if escolha_computador == 1:
                        placar['computador'] += 1
                    elif escolha_computador == 2:
                        placar['jogador'] += 1 
                
                elif escolha_jogador == 1:
                    if escolha_computador == 2:
                        placar['computador'] += 1
                    elif escolha_computador == 0:
                        placar['jogador'] += 1 
                    
                
                elif escolha_jogador == 2:
                    if escolha_computador == 0:
                        placar['computador'] += 1
                    elif escolha_computador == 1:
                        placar['jogador'] += 1 
                
                else:
                    print('Opção inválida, tente novamente...')
                    quantidade_rodadas += 1
            print(placar, sep='--')
            sleep(10)
            os.system('cls' if os.name == 'nt' else 'clear')
    elif menu_inicial == '2':
        break
    else:
        print('Opção inválida, tente novamente...')