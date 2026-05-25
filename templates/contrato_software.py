from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def montar_contrato_software(dados):

    styles = getSampleStyleSheet()

    story = []

    titulo = Paragraph(
        "<b>CONTRATO DE DESENVOLVIMENTO DE SOFTWARE</b>",
        styles['Heading1']
    )

    story.append(titulo)
    story.append(Spacer(1, 20))

    intro = f"""
    O desenvolvedor

    <b>{dados['nome_contratado']}</b>

    desenvolverá o sistema solicitado por

    <b>{dados['nome_contratante']}</b>.
    """

    story.append(
        Paragraph(intro, styles['BodyText'])
    )

    propriedade = """
    Todo o código-fonte, documentação e arquivos
    produzidos poderão ser cedidos conforme
    acordo entre as partes.
    """

    story.append(
        Paragraph(propriedade, styles['BodyText'])
    )

    return story