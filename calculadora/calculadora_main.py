from funcoes import calculos, validador

total = 0
flag_primeiro_numero = True

while True:
    
    print(f'Total = {total}')
    operador = input('Digite a operação: ')
    
    if operador == '=':
        print(f'Total = {total}')
        break
    
    elif operador in "+-*/":
        # Essa flag é usada para pedir o primeiro número apenas 1 vez a cada inicio de operação.
        if flag_primeiro_numero:
            primeiro_numero = input(f'Digite um número: ')
            # Possibilidade cast recebe o input do usuário e se caso o retorno for True, podemos converter o valor para int.
            possibilidade_cast = validador.verifica_numero(primeiro_numero)
            if possibilidade_cast:
                total = int(primeiro_numero)
                flag_primeiro_numero = False
            # Caso contrário, ele apenas volta a flag do primeiro número para True e reinicia o calculo.
            else:
                flag_primeiro_numero = True
                continue
        
        # Funciona da mesma forma do primeiro número com a diferença que esse sempre vai ser chamado caso estiver tudo certo com o primeiro número
        segundo_numero = input(f'{total} {operador} ')
        possibilidade_cast = validador.verifica_numero(segundo_numero)
        if possibilidade_cast:
            cast_segundo_numero = int(segundo_numero)
        else:
            continue
        
        while True:
            if operador == '+':
                total = calculos.soma(total, cast_segundo_numero)
            elif operador == '-':
                total = calculos.subtracao(total, cast_segundo_numero)      
            elif operador == '*':
                total = calculos.multiplicacao(total, cast_segundo_numero) 
            elif operador == '/':
                try:
                    total = calculos.divisao(total, cast_segundo_numero)
                except Exception as erro_divisao_zero:
                    print('Erro por divisão por zero. Reiniciando operação.')
                    total = 0 if total > 0 else total
                    flag_primeiro_numero = True
            break
    else:
        print('Operador inválido!')

    
    