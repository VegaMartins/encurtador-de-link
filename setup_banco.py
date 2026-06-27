import sqlite3

#  cria o arquivo banco.db 
conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

# script de criação da tabela 
sql_criar_tabela = '''
CREATE TABLE IF NOT EXISTS urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    long_url TEXT NOT NULL,
    short_code TEXT UNIQUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
'''

cursor.execute(sql_criar_tabela)
conexao.commit()
conexao.close()

print("arquivo 'banco.db' foi criado com a tabela 'urls'")