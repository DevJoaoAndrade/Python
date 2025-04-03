# Essa função percorre o cpf digitado pelo usuário e verifica se contém os simbolos .-, caso haja, ele o remove da string e adiciona a uma nova variável.
def removedor_de_simbolos(cpf_entrada):
    cpf_sem_simbolos = ''
    for numero in cpf_entrada:
        if numero in '.-':
            cpf_sem_simbolos += ''
            continue
        cpf_sem_simbolos += numero
    
    return cpf_sem_simbolos