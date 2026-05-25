from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def montar_contrato_consultoria(dados):

    styles = getSampleStyleSheet()

    story = []

    titulo = Paragraph(
        "<b>CONTRATO DE CONSULTORIA</b>",
        styles['Heading1']
    )

    story.append(titulo)
    story.append(Spacer(1, 20))

    texto = f"""
    O consultor

    <b>{dados['nome_contratado']}</b>

    fornecerá serviços de consultoria para

    <b>{dados['nome_contratante']}</b>.
    """

    story.append(
        Paragraph(texto, styles['BodyText'])
    )

    return story