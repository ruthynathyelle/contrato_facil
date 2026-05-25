from database.database import conectar

def criar_tabelas():

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contratos (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        usuario_id INTEGER,

        tipo_contrato TEXT,

        nome_contratante TEXT,

        nome_contratado TEXT,

        objeto_servico TEXT,

        valor_servico TEXT,

        data_inicio TEXT,

        data_fim TEXT,

        data_geracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(usuario_id)
        REFERENCES usuarios(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        nome TEXT,

        email TEXT UNIQUE,

        senha TEXT
    )
    """)

    conn.commit()

    conn.close()