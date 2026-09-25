from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

ARQUIVO_BANCO = 'tarefas.db'

# Conexão com o banco
def conectar_banco():
    """Conecta ao arquivo do banco. Se não existir, cria automaticamente."""
    caminho = os.path.join(os.path.dirname(__file__), ARQUIVO_BANCO)
    conexao = sqlite3.connect(caminho)
    conexao.row_factory = sqlite3.Row
    return conexao

# Inicializar as tabelas na primeira execução
def iniciar_banco():
    """Cria as tabelas se ainda não existirem."""
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    # Criar tabela de estudantes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estudantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    ''')
    
    # Criar tabela de tarefas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            disciplina TEXT,
            prazo DATETIME NOT NULL,
            status TEXT DEFAULT 'pendente',
            estudante_id INTEGER NOT NULL,
            FOREIGN KEY (estudante_id) REFERENCES estudantes(id)
        )
    ''')
    
    # Verificar se já tem estudante cadastrado
    cursor.execute("SELECT * FROM estudantes")
    if not cursor.fetchone():
        cursor.execute('''
            INSERT INTO estudantes (nome, email, senha)
            VALUES (?, ?, ?)
        ''', ('Seu Nome Completo', 'seuemail@exemplo.com', '123456'))
    
    conexao.commit()
    cursor.close()
    conexao.close()

# Páginas do Sistema
@app.route('/')
def pagina_inicial():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tarefas ORDER BY prazo ASC")
    lista_tarefas = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template('index.html', tarefas=lista_tarefas)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_tarefa():
    if request.method == 'POST':
        titulo = request.form['titulo']
        disciplina = request.form['disciplina']
        descricao = request.form['descricao']
        prazo = request.form['prazo']
        id_estudante = 1
        
        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute('''
            INSERT INTO tarefas (titulo, disciplina, descricao, prazo, estudante_id)
            VALUES (?, ?, ?, ?, ?)
        ''', (titulo, disciplina, descricao, prazo, id_estudante))
        conexao.commit()
        cursor.close()
        conexao.close()
        return redirect(url_for('pagina_inicial'))
    
    return render_template('cadastrar.html')

@app.route('/concluir/<int:tarefa_id>')
def concluir_tarefa(tarefa_id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("UPDATE tarefas SET status = 'concluida' WHERE id = ?", (tarefa_id,))
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect(url_for('pagina_inicial'))

@app.route('/excluir/<int:tarefa_id>')
def excluir_tarefa(tarefa_id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect(url_for('pagina_inicial'))

# Iniciar o programa
if __name__ == '__main__':
    iniciar_banco()
    print("=" * 50)
    print("✅ Banco de dados pronto!")
    print("🚀 Servidor rodando em: http://127.0.0.1:5000")
    print("=" * 50)
    app.run(debug=True)