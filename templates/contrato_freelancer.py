from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def montar_contrato_freelancer(dados):

    styles = getSampleStyleSheet()

    story = []

    titulo = Paragraph(
        "<b>CONTRATO DE FREELANCER</b>",
        styles['Heading1']
    )

    story.append(titulo)
    story.append(Spacer(1, 20))

    texto = f"""
    O freelancer <b>{dados['nome_contratado']}</b>
    prestará serviços para

    <b>{dados['nome_contratante']}</b>.
    """

    story.append(
        Paragraph(texto, styles['BodyText'])
    )

    clausula = f"""
    O projeto contratado consiste em:

    <br/><br/>

    <b>{dados['objeto_servico']}</b>
    """

    story.append(
        Paragraph(clausula, styles['BodyText'])
    )

    return story