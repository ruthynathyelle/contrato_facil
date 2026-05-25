import bcrypt

from database.database import conectar


# =========================
# CRIAR USUÁRIO
# =========================

def criar_usuario(
    nome,
    email,
    senha
):

    conn = conectar()

    cursor = conn.cursor()

    # HASH DA SENHA
    senha_hash = bcrypt.hashpw(
        senha.encode(),
        bcrypt.gensalt()
    )

    cursor.execute("""
    INSERT INTO usuarios (

        nome,

        email,

        senha

    ) VALUES (?, ?, ?)
    """, (

        nome,

        email,

        senha_hash.decode()
    ))

    conn.commit()

    conn.close()


# =========================
# LOGIN
# =========================

def autenticar_usuario(
    email,
    senha
):

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        nome,
        senha

    FROM usuarios

    WHERE email = ?
    """, (email,))

    usuario = cursor.fetchone()

    conn.close()

    if not usuario:

        return None

    senha_correta = bcrypt.checkpw(
        senha.encode(),
        usuario[2].encode()
    )

    if senha_correta:

        return (
            usuario[0],
            usuario[1]
        )

    return None