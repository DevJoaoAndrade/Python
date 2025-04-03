def removedor_de_simbolos(cpf_entrada):
    cpf_sem_simbolos = ''
    
    for numero in cpf_entrada:
        if numero in '.-':
            cpf_sem_simbolos += ''
            continue
        cpf_sem_simbolos += numero
    
    return cpf_sem_simbolos