from database.database import conectar


# =========================
# SALVAR CONTRATO
# =========================

def salvar_contrato(
    usuario_id,
    dados
):

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO contratos (

        usuario_id,

        tipo_contrato,

        nome_contratante,

        nome_contratado,

        objeto_servico,

        valor_servico,

        data_inicio,

        data_fim

    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (

        usuario_id,

        dados['tipo_contrato'],

        dados['nome_contratante'],

        dados['nome_contratado'],

        dados['objeto_servico'],

        dados['valor_servico'],

        dados['data_inicio'],

        dados['data_fim']
    ))

    conn.commit()

    conn.close()


# =========================
# LISTAR CONTRATOS
# =========================

def listar_contratos(
    usuario_id
):

    conn = conectar()

    cursor = conn.cursor()

    query = """
    SELECT
        id,
        tipo_contrato,
        nome_contratante,
        valor_servico,
        data_geracao

    FROM contratos

    WHERE usuario_id = ?

    ORDER BY id DESC
    """

    cursor.execute(
        query,
        (usuario_id,)
    )

    contratos = cursor.fetchall()

    conn.close()

    return contratos


# =========================
# TOTAL DE CONTRATOS
# =========================

def total_contratos(
    usuario_id
):

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)

    FROM contratos

    WHERE usuario_id = ?
    """, (usuario_id,))

    total = cursor.fetchone()[0]

    conn.close()

    return total


# =========================
# VALOR TOTAL
# =========================

def valor_total_contratos(
    usuario_id
):

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT valor_servico

    FROM contratos

    WHERE usuario_id = ?
    """, (usuario_id,))

    valores = cursor.fetchall()

    conn.close()

    total = 0

    for valor in valores:

        try:

            valor_limpo = (
                valor[0]
                .replace("R$", "")
                .replace(".", "")
                .replace(",", ".")
                .strip()
            )

            total += float(valor_limpo)

        except:

            pass

    return total


# =========================
# BUSCAR CONTRATOS
# =========================

def buscar_contratos(
    usuario_id,
    nome="",
    tipo_contrato=""
):

    conn = conectar()

    cursor = conn.cursor()

    query = """
    SELECT
        id,
        tipo_contrato,
        nome_contratante,
        valor_servico,
        data_geracao

    FROM contratos

    WHERE usuario_id = ?
    """

    parametros = [usuario_id]

    # FILTRO NOME
    if nome:

        query += """
        AND nome_contratante LIKE ?
        """

        parametros.append(
            f"%{nome}%"
        )

    # FILTRO TIPO
    if tipo_contrato:

        query += """
        AND tipo_contrato = ?
        """

        parametros.append(
            tipo_contrato
        )

    query += """
    ORDER BY id DESC
    """

    cursor.execute(
        query,
        parametros
    )

    contratos = cursor.fetchall()

    conn.close()

    return contratos


# =========================
# EXCLUIR CONTRATO
# =========================

def excluir_contrato(
    id_contrato
):

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM contratos

    WHERE id = ?
    """, (id_contrato,))

    conn.commit()

    conn.close()


# =========================
# ATUALIZAR CONTRATO
# =========================

def atualizar_contrato(
    id_contrato,
    dados
):

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""
    UPDATE contratos

    SET

        tipo_contrato = ?,

        nome_contratante = ?,

        nome_contratado = ?,

        objeto_servico = ?,

        valor_servico = ?,

        data_inicio = ?,

        data_fim = ?

    WHERE id = ?
    """, (

        dados['tipo_contrato'],

        dados['nome_contratante'],

        dados['nome_contratado'],

        dados['objeto_servico'],

        dados['valor_servico'],

        dados['data_inicio'],

        dados['data_fim'],

        id_contrato
    ))

    conn.commit()

    conn.close()