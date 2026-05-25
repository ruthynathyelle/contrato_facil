CLAUSULAS = {

    "confidencialidade": """

    CLÁUSULA DE CONFIDENCIALIDADE

    As partes comprometem-se a não divulgar
    informações sensíveis...
    """,

    "lgpd": """

    CLÁUSULA LGPD

    As partes comprometem-se a cumprir
    a Lei Geral de Proteção de Dados...
    """,

    "foro": """

    CLÁUSULA DE FORO

    Fica eleito o foro da comarca...
    """
}

MAPEAMENTO_CONTRATOS = {

    "prestacao_servico": [
        "confidencialidade",
        "lgpd",
        "foro"
    ],

    "software": [
        "confidencialidade",
        "lgpd",
        "propriedade_intelectual",
        "licenca_uso",
        "foro"
    ]
}