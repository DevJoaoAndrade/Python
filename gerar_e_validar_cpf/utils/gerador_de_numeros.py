from  random import randint

# Essa função gera 9 digitos em uma string e retorna para o main
def gerar_nove_numeros():
    nove_digitos = ''
    for _ in range(9):
        nove_digitos += str(randint(0, 9))
    return nove_digitos


def gerar_digito_verificador(nove_numeros, contador):
    soma_numeros = 0
    
    # Este laço vai pegar cada número dos nove_numeros, multiplicar por um valor decrescente do contador e adicionar na
    # variável soma_numeros
    for numero in nove_numeros:
        soma_numeros += int(numero) * contador
        contador -= 1
    
    soma_numeros %= 11
    
    # Neste operador ternário, ele verifica se o resto da divisão entre soma_numeros % 11 == 0 ou 1, caso for, retorna 0
    # para a variável, caso contrário, retorna a subtração entre 11 - soma_numeros
    digito_verificador = 0 if soma_numeros < 2 else 11 - soma_numeros
    
    return str(digito_verificador)