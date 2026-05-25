from datetime import datetime

from reportlab.platypus import Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from services.clause_engine import obter_clausulas
from utils.signature import (
    gerar_id_contrato,
    gerar_assinatura
)
from utils.qrcode_generator import (
    gerar_qrcode
)

contrato_id = gerar_id_contrato()


def montar_contrato_servico(dados):
    contrato_id = gerar_id_contrato()

    assinatura = gerar_assinatura(
        dados['usuario_nome']
    )

    qr_path = gerar_qrcode(
        contrato_id
    )

    styles = getSampleStyleSheet()

    style_title = ParagraphStyle(
        'Titulo',
        parent=styles['Heading1'],
        alignment=TA_CENTER,
        spaceAfter=20
    )

    style_body = ParagraphStyle(
        'Corpo',
        parent=styles['Normal'],
        alignment=TA_JUSTIFY,
        leading=16,
        spaceAfter=12
    )

    style_clause = ParagraphStyle(
        'Clausula',
        parent=styles['Normal'],
        alignment=TA_JUSTIFY,
        leading=16,
        leftIndent=20,
        spaceAfter=10
    )

    style_assinatura = ParagraphStyle(
        'Assinatura',
        parent=styles['Normal'],
        alignment=TA_CENTER,
        leading=20,
        spaceBefore=30
    )

    story = []

    # TÍTULO
    story.append(
        Paragraph(
            "<b>CONTRATO DE PRESTAÇÃO DE SERVIÇOS</b>",
            style_title
        )
    )

    story.append(Spacer(1, 20))

    # PARTES
    preambulo = f"""

    <b>CONTRATANTE:</b>
    
    {dados['nome_contratante']},
    
    inscrito(a) no CPF/CNPJ sob o nº
    {dados['cpf_contratante']},
    
    telefone:
    {dados['telefone_contratante']},
    
    email:
    {dados['email_contratante']},
    
    endereço:
    {dados['endereco_contratante']}.
    
    <br/><br/>
    
    <b>CONTRATADO:</b>
    
    {dados['nome_contratado']},
    
    inscrito(a) no CPF/CNPJ sob o nº
    {dados['cpf_contratado']},
    
    telefone:
    {dados['telefone_contratado']},
    
    email:
    {dados['email_contratado']},
    
    endereço:
    {dados['endereco_contratado']}.
    
    <br/><br/>
    
    As partes acima identificadas celebram
    o presente Contrato de Prestação de Serviços.
    """

    story.append(
        Paragraph(preambulo, style_body)
    )

    # CLÁUSULA OBJETO
    story.append(
        Paragraph(
            "<b>CLÁUSULA PRIMEIRA – DO OBJETO</b>",
            style_body
        )
    )

    objeto = f"""
    O presente contrato possui como objeto:

    <br/><br/>

    <b>{dados['objeto_servico']}</b>
    """

    story.append(
        Paragraph(objeto, style_clause)
    )

    # VALOR
    story.append(
        Paragraph(
            "<b>CLÁUSULA SEGUNDA – DO VALOR</b>",
            style_body
        )
    )

    valor = f"""
    O valor acordado é de
    <b>R$ {dados['valor_servico']}</b>.
    """

    story.append(
        Paragraph(valor, style_clause)
    )

    # PRAZO
    story.append(
        Paragraph(
            "<b>CLÁUSULA TERCEIRA – DO PRAZO</b>",
            style_body
        )
    )

    prazo = f"""
    O serviço iniciará em
    <b>{dados['data_inicio']}</b>

    e terminará em

    <b>{dados['data_fim']}</b>.
    """

    story.append(
        Paragraph(prazo, style_clause)
    )

    # MULTA
    story.append(
        Paragraph(
            "<b>CLÁUSULA QUARTA – DA MULTA</b>",
            style_body
        )
    )

    multa = """
    O inadimplemento contratual acarretará multa
    de 10% sobre o valor do contrato.
    """

    story.append(
        Paragraph(multa, style_clause)
    )

    # ENCERRAMENTO
    data_atual = datetime.now().strftime("%d/%m/%Y")

    encerramento = f"""
    Firmado eletronicamente em {data_atual}.
    """

    story.append(
        Paragraph(encerramento, style_body)
    )

    story.append(Spacer(1, 40))

    story.append(
        Spacer(1, 30)
    )

    story.append(
        Paragraph(
            f"<b>ID DO CONTRATO:</b> {contrato_id}",
            style_body
        )
    )

    story.append(
        Paragraph(
            assinatura,
            style_body
        )
    )

    story.append(
    Spacer(1, 20)
    )



    story.append(
        Paragraph(
            "<b>Validação Digital</b>",
            style_body
        )
    )

    qr_image = Image(
        qr_path,
        width=120,
        height=120
    )

    story.append(qr_image)

    
    # ASSINATURAS
    story.append(
        Spacer(1, 60)
    )

    assinatura_1 = """
    _________________________________

    <b>CONTRATANTE</b>

    {0}
    """.format(dados['nome_contratante'])

    assinatura_2 = """
    _________________________________

    <b>CONTRATADO</b>

    {0}
    """.format(dados['nome_contratado'])

    tabela_assinaturas = Table(
        [[
            Paragraph(
                assinatura_1,
                style_assinatura
            ),

            Paragraph(
                assinatura_2,
                style_assinatura
            )
        ]],
        colWidths=[260, 260]
    )

    tabela_assinaturas.setStyle(
        TableStyle([

            ('ALIGN', (0,0), (-1,-1), 'CENTER'),

            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),

            ('BOTTOMPADDING', (0,0), (-1,-1), 30),

            ('TOPPADDING', (0,0), (-1,-1), 20),

        ])
    )

    story.append(
        tabela_assinaturas
    )
    # CLÁUSULAS INTELIGENTES
    clausulas = obter_clausulas(
        "prestacao_servico",
        dados
    )

    for clausula in clausulas:

        story.append(
            Paragraph(
                clausula,
                style_clause
            )
        )
    

    return story