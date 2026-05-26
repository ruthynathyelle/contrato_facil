from datetime import datetime
import uuid



def gerar_id_contrato():

    codigo = str(
        uuid.uuid4()
    )[:8]

    data = datetime.now().strftime(
        "%Y%m%d"
    )

    return f"CTR-{data}-{codigo}"


def gerar_assinatura(
    usuario_nome
):

    data_hora = datetime.now().strftime(
        "%d/%m/%Y %H:%M"
    )

    return f"""
    Documento assinado digitalmente por:

    {usuario_nome}

    Data/Hora:
    {data_hora}
    """