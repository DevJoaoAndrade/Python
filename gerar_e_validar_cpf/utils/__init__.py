from utils.gerador_de_numeros import gerar_digito_verificador


def iniciador_gera_validar(nove_digitos_cpf):
    primeiro_verificador = gerar_digito_verificador(nove_digitos_cpf, 10)
    dez_digitos_cpf = nove_digitos_cpf + primeiro_verificador
    
    segundo_verificador = gerar_digito_verificador(dez_digitos_cpf, 11)
    cpf = dez_digitos_cpf + segundo_verificador
    return cpf