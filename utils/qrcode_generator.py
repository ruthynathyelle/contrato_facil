import qrcode


def gerar_qrcode(
    contrato_id
):

    caminho = f"temp/{contrato_id}.png"

    qr = qrcode.make(
        f"Contrato válido: {contrato_id}"
    )

    qr.save(caminho)

    return caminho