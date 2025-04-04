from utils.gerador_de_numeros import gerar_digito_verificador

# Essa função foi criada para iniciar a geração do cpf a partir dos nove_digitos_cpf de input no main.
def iniciador_gerar_validar(nove_digitos_cpf):
    primeiro_verificador = gerar_digito_verificador(nove_digitos_cpf, 10)
    dez_digitos_cpf = nove_digitos_cpf + primeiro_verificador
    
    segundo_verificador = gerar_digito_verificador(dez_digitos_cpf, 11)
    cpf = dez_digitos_cpf + segundo_verificador
    return cpf