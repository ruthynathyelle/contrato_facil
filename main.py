import streamlit as st

from services.pdf_generator import criar_documento
from services.contract_engine import gerar_contrato
from services.validators import validar_campos

from services.database_service import (
    salvar_contrato,
    listar_contratos,
    total_contratos,
    valor_total_contratos,
    buscar_contratos,
    excluir_contrato,
    atualizar_contrato
)

from services.auth_service import (
    criar_usuario,
    autenticar_usuario
)

from database.models import criar_tabelas

# =========================
# INICIALIZAÇÃO
# =========================

criar_tabelas()

if "usuario" not in st.session_state:

    st.session_state["usuario"] = None

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================

st.set_page_config(
    page_title="Gerador Automático de Contratos",
    page_icon="📄",
    layout="centered"
)

st.image(
    "assets/logo.png",
    width=220
)

# =========================
# LOGIN / CADASTRO
# =========================

if not st.session_state["usuario"]:

    st.title("🔐 Login")

    aba1, aba2 = st.tabs([
        "Entrar",
        "Cadastrar"
    ])

    # LOGIN
    with aba1:

        email_login = st.text_input(
            "Email"
        )

        senha_login = st.text_input(
            "Senha",
            type="password"
        )

        if st.button("Entrar"):

            usuario = autenticar_usuario(
                email_login,
                senha_login
            )

            if usuario:

                st.session_state[
                    "usuario"
                ] = usuario

                st.rerun()

            else:

                st.error(
                    "Credenciais inválidas."
                )

    # CADASTRO
    with aba2:

        nome = st.text_input(
            "Nome"
        )

        email = st.text_input(
            "Email",
            key="cad_email"
        )

        senha = st.text_input(
            "Senha",
            type="password",
            key="cad_senha"
        )

        if st.button("Cadastrar"):

            try:

                criar_usuario(
                    nome,
                    email,
                    senha
                )

                st.success(
                    "Usuário criado com sucesso!"
                )

            except Exception as e:

                st.error(
                    f"Erro ao cadastrar: {str(e)}"
                )

    st.stop()

# =========================
# USUÁRIO LOGADO
# =========================

usuario_id = st.session_state[
    "usuario"
][0]

usuario_nome = st.session_state[
    "usuario"
][1]

# =========================
# TOPO
# =========================

col1, col2 = st.columns([4, 1])

with col1:

    st.title(
        "📄 Gerador Automático de Contratos"
    )

with col2:

    if st.button("🚪 Sair"):

        st.session_state["usuario"] = None

        st.rerun()

st.markdown(
    f"Bem-vindo, **{usuario_nome}**"
)

# =========================
# DASHBOARD
# =========================

st.header("📊 Dashboard")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Total de Contratos",
        total_contratos(usuario_id)
    )

with col2:

    valor_total = valor_total_contratos(
        usuario_id
    )

    st.metric(
        "Valor Total",
        f"R$ {valor_total:,.2f}"
    )

# =========================
# FILTROS
# =========================

st.subheader("🔎 Buscar Contratos")

col1, col2 = st.columns(2)

with col1:

    busca_nome = st.text_input(
        "Buscar por contratante"
    )

with col2:

    filtro_tipo = st.selectbox(
        "Filtrar por tipo",
        [
            "",
            "prestacao_servico",
            "freelancer",
            "software",
            "consultoria"
        ]
    )

# =========================
# LISTA DE CONTRATOS
# =========================

st.subheader("📄 Últimos Contratos")

contratos = buscar_contratos(
    usuario_id,
    nome=busca_nome,
    tipo_contrato=filtro_tipo
)

if contratos:

    for contrato in contratos:

        with st.expander(
            f"📄 Contrato #{contrato[0]}"
        ):

            st.write(
                f"Tipo: {contrato[1]}"
            )

            st.write(
                f"Contratante: {contrato[2]}"
            )

            st.write(
                f"Valor: {contrato[3]}"
            )

            st.write(
                f"Data: {contrato[4]}"
            )

            col1, col2 = st.columns(2)

            # EXCLUIR
            with col1:

                if st.button(
                    "🗑️ Excluir",
                    key=f"delete_{contrato[0]}"
                ):

                    excluir_contrato(
                        contrato[0]
                    )

                    st.success(
                        "Contrato excluído!"
                    )

                    st.rerun()

            # EDITAR
            with col2:

                if st.button(
                    "✏️ Editar",
                    key=f"edit_{contrato[0]}"
                ):

                    st.session_state[
                        "editar_id"
                    ] = contrato[0]

else:

    st.info(
        "Nenhum contrato encontrado."
    )

# =========================
# EDIÇÃO
# =========================

if "editar_id" in st.session_state:

    st.divider()

    st.subheader("✏️ Editar Contrato")

    id_edicao = st.session_state[
        "editar_id"
    ]

    with st.form("editar_form"):

        novo_nome = st.text_input(
            "Novo Contratante"
        )

        novo_valor = st.text_input(
            "Novo Valor"
        )

        atualizar = st.form_submit_button(
            "Salvar Alterações"
        )

        if atualizar:

            dados_update = {

                "usuario_nome": usuario_nome,

                "tipo_contrato": "prestacao_servico",

                "nome_contratante": novo_nome,

                "nome_contratado": "",

                "objeto_servico": "",

                "valor_servico": novo_valor,

                "data_inicio": "",

                "data_fim": ""
            }

            atualizar_contrato(
                id_edicao,
                dados_update
            )

            st.success(
                "Contrato atualizado!"
            )

            del st.session_state[
                "editar_id"
            ]

            st.rerun()

st.divider()

# =========================
# FORMULÁRIO
# =========================

with st.form("formulario_contrato"):

    st.header("Novo Contrato")

    tipo_contrato = st.selectbox(
        "Selecione o modelo de contrato",
        [
            ("Prestação de Serviço", "prestacao_servico"),
            ("Freelancer", "freelancer"),
            ("Software", "software"),
            ("Consultoria", "consultoria")
        ],
        format_func=lambda x: x[0]
    )

    st.subheader("Dados do Contratado")

    nome_contratado = st.text_input(
        "Nome do Contratado"
    )

    cpf_contratado = st.text_input(
        "CPF/CNPJ do Contratado"
    )

    telefone_contratado = st.text_input(
        "Telefone do Contratado"
    )

    email_contratado = st.text_input(
        "Email do Contratado"
    )

    endereco_contratado = st.text_input(
        "Endereço do Contratado"
    )
    st.subheader("Dados do Contratante")

    nome_contratante = st.text_input(
        "Nome do Contratante"
    )

    cpf_contratante = st.text_input(
        "CPF/CNPJ do Contratante"
    )

    telefone_contratante = st.text_input(
        "Telefone do Contratante"
    )

    email_contratante = st.text_input(
        "Email do Contratante"
    )

    endereco_contratante = st.text_input(
        "Endereço do Contratante"
    )

    st.subheader("Serviço")

    objeto_servico = st.text_area(
        "Objeto do Serviço"
    )

    valor_servico = st.number_input(
        "Valor do Serviço (R$)",
        min_value=0.0,
        step=100.0,
        format="%.2f"
    )

    st.subheader("Prazos")

    col1, col2 = st.columns(2)

    with col1:

        data_inicio = st.date_input(
            "Data de Início"
        ).strftime("%d/%m/%Y")

    with col2:

        data_fim = st.date_input(
            "Data Final"
        ).strftime("%d/%m/%Y")

    submit = st.form_submit_button(
        "📄 Gerar Contrato"
    )

# =========================
# PROCESSAMENTO
# =========================

if submit:

    dados = {
        "nome_contratado": nome_contratado,

        "nome_contratante": nome_contratante,

        "cpf_contratado": cpf_contratado,
        
        "telefone_contratado": telefone_contratado,
        
        "email_contratado": email_contratado,
        
        "endereco_contratado": endereco_contratado,

        "cpf_contratante": cpf_contratante,
        
        "telefone_contratante": telefone_contratante,
        
        "email_contratante": email_contratante,
        
        "endereco_contratante": endereco_contratante,
        
        "usuario_nome": usuario_nome,

        "tipo_contrato": tipo_contrato[1],

        "objeto_servico": objeto_servico,

        "valor_servico": valor_servico,

        "data_inicio": data_inicio,

        "data_fim": data_fim
    }

    valido = validar_campos(dados)

    if not valido:

        st.error(
            f"❌ Campo obrigatório não preenchido: {campo}"
        )

    else:

        try:

            # SALVAR
            salvar_contrato(
                usuario_id,
                dados
            )

            # PDF
            doc, pdf_buffer = criar_documento()

            story = gerar_contrato(
                tipo_contrato[1],
                dados
            )

            doc.build(story)

            pdf_buffer.seek(0)

            st.success(
                "✅ Contrato gerado!"
            )

            st.download_button(
                label="📥 Baixar PDF",
                data=pdf_buffer,
                file_name=f"{tipo_contrato[1]}.pdf",
                mime="application/pdf"
            )

        except Exception as e:

            st.error(
                f"Erro: {str(e)}"
            )