def validar_campos(dados):

    campos_obrigatorios = [

        "nome_contratado",
        "cpf_contratado",
        "telefone_contratado",
        "email_contratado",
        "endereco_contratado",

        "nome_contratante",
        "cpf_contratante",
        "telefone_contratante",
        "email_contratante",
        "endereco_contratante",

        "objeto_servico",
        "valor_servico",
        "data_inicio",
        "data_fim"
    ]

    for campo in campos_obrigatorios:

        valor = dados.get(campo)

        # STRING VAZIA
        if isinstance(valor, str):

            if not valor.strip():

                return False, campo

        # NONE
        elif valor is None:

            return False, campo

    return True, None