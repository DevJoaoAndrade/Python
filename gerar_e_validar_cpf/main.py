from utils.gerador_de_numeros import gerar_nove_numeros
from utils.gerador_digito_verificador import gerar_digito_verificador


if __name__ == '__main__':
    while True:
        opcao_menu = input('1 - Gerar CPF\n2 - Validar CPF\n3 - Sair\nDigite aqui: ')
        if opcao_menu == '1':
                
            nove_digitos_cpf = gerar_nove_numeros()
    
            primeiro_verificador = gerar_digito_verificador(nove_digitos_cpf, 10)
            dez_digitos_cpf = nove_digitos_cpf + primeiro_verificador
    
            segundo_verificador = gerar_digito_verificador(dez_digitos_cpf, 11)
            cpf = dez_digitos_cpf + segundo_verificador
            print(cpf)
        elif opcao_menu == '2':
            cpf_para_validar = input('Validar CPF\nDigite o CPF:')
        elif opcao_menu == '3':
            break
        else:
            print('Opção inválida, escolha outra opção.')
    
    
    
    
    
    
    



    

