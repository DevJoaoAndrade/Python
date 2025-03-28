from funcoes import calculos, validador

total = 0
opcao_funcionamento_while = False

print('Calculadora (Pressione "x" para iniciar ou "=" para encerrar seu calculo!)')
opcao_menu_inicial = input('Digite aqui:')

if opcao_menu_inicial == 'x':
    opcao_funcionamento_while = True
elif opcao_menu_inicial == '=':
    print(f'Total = {total}')
else:
    pass

while opcao_funcionamento_while:
    operador = input('Digite a operação: ')
    if operador == '=':
        print(total)
        break
    elif operador in "+-*/":
        while True:
            numero1 = int(input('Digite um numero: '))
            numero2 = int(input('Digite outro numero: '))
            
            if operador == '+':
                total += calculos.soma(numero1, numero2)
                break
            elif operador == '-':
                pass
            elif operador == '*':
                pass
            elif operador == '/':
                pass
                
            else:
                print('Operador inválido!')

    
    