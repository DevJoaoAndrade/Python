# Essa função serve apenas para verificar se o número digitado pelo usuário é um número, com isso ele retorna True
# caso contrario, retorna false.
def verifica_numero(numero):
    if numero.isdigit():
        return True
    else:
        return False
