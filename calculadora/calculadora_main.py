from funcoes import calculos, validador

total = 0
flag_total = True

while True:
    
    print(f'Total = {total}')
    operador = input('Digite a operação: ')
    
    if operador == '=':
        print(f'Total = {total}')
        break
    elif operador in "+-*/":
        
        if flag_total:
            total = int(input('Digite um valor: '))
            flag_total = False
        
        while True:
            segundo_numero = int(input('Digite outro numero: '))
            
            if operador == '+':
                total = calculos.soma(total, segundo_numero)
                break
            elif operador == '-':
                total = calculos.subtracao(total, segundo_numero)
                break
            elif operador == '*':
                total = calculos.multiplicacao(total, segundo_numero)
                break
            elif operador == '/':
                pass
            else:
                print('Operador inválido!')

    
    