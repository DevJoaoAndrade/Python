from  random import randint

def gerar_nove_digitos():
    nove_digitos = ''
    for _ in range(9):
        nove_digitos += str(randint(0, 9))
    return nove_digitos