from utils.gerador_de_numeros import gerar_nove_numeros
from utils.valida_numeros import removedor_de_simbolos
from utils import iniciador_gera_validar

import os
import time

if __name__ == '__main__':
    while True:
        opcao_menu = input('1 - Gerar CPF\n2 - Validar CPF\n3 - Sair\nDigite aqui: ')
        if opcao_menu == '1':
            nove_digitos_cpf = gerar_nove_numeros()
            cpf = iniciador_gera_validar(nove_digitos_cpf)
            print(cpf)
        elif opcao_menu == '2':
            cpf_entrada = input('Digite o CPF: ')
            cpf_sem_simbolos = removedor_de_simbolos(cpf_entrada)
            nove_digitos_cpf = cpf_sem_simbolos[:9]
            if nove_digitos_cpf.isdigit():
                cpf = iniciador_gera_validar(nove_digitos_cpf)
                if cpf_sem_simbolos == cpf:
                    print(f'CPF válido')
                else:
                    print(f'CPF inválido')                
            else:
                print('Ocorreu um erro, tente novamente.')
        elif opcao_menu == '3':
            break
        else:
            print('Opção inválida, escolha outra opção.')
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    
    
    
    
    
    
    



    

