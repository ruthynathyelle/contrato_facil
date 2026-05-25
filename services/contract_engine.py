from templates.contrato_servico import montar_contrato_servico
from templates.contrato_freelancer import montar_contrato_freelancer
from templates.contrato_software import montar_contrato_software
from templates.contrato_consultoria import montar_contrato_consultoria

def gerar_contrato(tipo_contrato, dados):

    templates = {

        "prestacao_servico": montar_contrato_servico,

        "freelancer": montar_contrato_freelancer,

        "software": montar_contrato_software,

        "consultoria": montar_contrato_consultoria
    }

    if tipo_contrato not in templates:
        raise ValueError("Tipo de contrato inválido.")

    return templates[tipo_contrato](dados)