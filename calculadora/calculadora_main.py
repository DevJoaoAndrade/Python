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
            total = int(input(f'Digite um número: '))
            flag_total = False
        
        while True:
            segundo_numero = int(input(f'{total} {operador} '))
            
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
                try:
                    total = calculos.divisao(total, segundo_numero)
                    break
                except Exception as erro_divisao_zero:
                    print('Erro por divisão por zero. Reiniciando operação.')
                    total = 0 if total > 0 else total
                    flag_total = True
                    break
    else:
        print('Operador inválido!')

    
    