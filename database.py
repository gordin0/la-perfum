import sqlite3

# =====================================================
# CRIAR TABELA
# =====================================================
def criar_tabela():
    conexao = sqlite3.connect('le_parfum.db')
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS perfume (
        id_perfume       INTEGER PRIMARY KEY AUTOINCREMENT,
        nome             TEXT NOT NULL,
        marca            TEXT NOT NULL,
        familia_olfativa TEXT NOT NULL,
        preco            REAL NOT NULL,
        estoque          INTEGER NOT NULL DEFAULT 0
    )
    ''')

    conexao.commit()
    conexao.close()


# =====================================================
# CADASTRAR PERFUME
# =====================================================
def cadastrar_perfume(nome, marca, familia_olfativa, preco, estoque):
    conexao = sqlite3.connect('le_parfum.db')
    cursor = conexao.cursor()

    cursor.execute('''
    INSERT INTO perfume (nome, marca, familia_olfativa, preco, estoque)
    VALUES (?, ?, ?, ?, ?)
    ''', (nome, marca, familia_olfativa, preco, estoque))

    conexao.commit()
    conexao.close()


# =====================================================
# LISTAR PERFUMES
# =====================================================
def listar_perfumes():
    conexao = sqlite3.connect('le_parfum.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM perfume')
    perfumes = cursor.fetchall()

    conexao.close()
    return perfumes


# =====================================================
# ATUALIZAR PERFUME
# =====================================================
def atualizar_perfume(id_perfume, nome, marca, familia_olfativa, preco, estoque):
    conexao = sqlite3.connect('le_parfum.db')
    cursor = conexao.cursor()

    cursor.execute('''
    UPDATE perfume
    SET nome = ?, marca = ?, familia_olfativa = ?, preco = ?, estoque = ?
    WHERE id_perfume = ?
    ''', (nome, marca, familia_olfativa, preco, estoque, id_perfume))

    conexao.commit()
    conexao.close()


# =====================================================
# EXCLUIR PERFUME
# =====================================================
def excluir_perfume(id_perfume):
    conexao = sqlite3.connect('le_parfum.db')
    cursor = conexao.cursor()

    cursor.execute('DELETE FROM perfume WHERE id_perfume = ?', (id_perfume,))

    conexao.commit()
    conexao.close()