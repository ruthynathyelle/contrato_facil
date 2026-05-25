def obter_clausulas(tipo_contrato, dados):

    clausulas = []

    # CLÁUSULA DE MULTA
    clausulas.append("""
    O inadimplemento acarretará multa de
    10% sobre o valor do contrato.
    """)

    # SOFTWARE
    if tipo_contrato == "software":

        clausulas.append("""
        Todo código-fonte desenvolvido poderá
        ser cedido ao contratante conforme
        acordo firmado entre as partes.
        """)

        clausulas.append("""
        O contratado manterá sigilo sobre
        informações confidenciais do projeto.
        """)

    # CONSULTORIA
    if tipo_contrato == "consultoria":

        clausulas.append("""
        O contratado não garante resultados
        específicos na consultoria prestada.
        """)

    # FREELANCER
    if tipo_contrato == "freelancer":

        clausulas.append("""
        O freelancer possui autonomia técnica
        na execução do serviço contratado.
        """)

    return clausulas