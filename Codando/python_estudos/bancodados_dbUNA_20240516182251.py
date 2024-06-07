import streamlit as st
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('db_UNA.db')
cursor = conn.cursor()

# Criar as tabelas se não existirem
cursor.execute("""
CREATE TABLE IF NOT EXISTS tb_cursos (
    id_Curso INTEGER PRIMARY KEY,
    nome_curso TEXT NOT NULL
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS tb_aluno (
    id_Aluno TEXT PRIMARY KEY,
    nome_aluno TEXT NOT NULL,
    curso_aluno INTEGER,
    FOREIGN KEY (curso_aluno) REFERENCES tb_cursos(id_Curso)
);
""")
conn.commit()

# Funções para interagir com as tabelas

def inserir_curso():
    """Insere um novo curso na tabela tb_cursos."""
    st.subheader(":blue[Inserir Novo Curso]")
    nome_curso = st.text_input("Nome do Curso:")
    if st.button("Salvar Curso"):
        try:
            cursor.execute("INSERT INTO tb_cursos (nome_curso) VALUES (?)", (nome_curso,))
            conn.commit()
            st.toast("Curso inserido com sucesso!", icon="🆗")
            #st.success("Curso inserido com sucesso!")
        except sqlite3.IntegrityError:
            st.error("Erro: Já existe um curso com esse nome.")

def inserir_aluno():
    """Insere um novo aluno na tabela tb_aluno."""
    st.subheader(":green[Inserir Novo Aluno]")
    id_aluno = st.text_input("ID do Aluno:")
    nome_aluno = st.text_input("Nome do Aluno:")
    
    # Obter lista de cursos para o dropdown
    cursor.execute("SELECT id_Curso, nome_curso FROM tb_cursos")
    cursos = cursor.fetchall()
    cursos_dict = {curso[0]: curso[1] for curso in cursos}
    
    curso_aluno = st.selectbox("Curso:", cursos_dict.keys(), format_func=lambda x: cursos_dict.get(x))
    if st.button("Salvar Aluno"):
        try:
            cursor.execute("INSERT INTO tb_aluno (id_Aluno, nome_aluno, curso_aluno) VALUES (?, ?, ?)", (id_aluno, nome_aluno, curso_aluno))
            conn.commit()
            st.toast("Aluno inserido com sucesso!", icon="🆗")
            #st.success("Aluno inserido com sucesso!")
        except sqlite3.IntegrityError:
            st.error("Erro: Já existe um aluno com esse ID.")

def exibir_dados():
    """Exibe os dados das tabelas."""
    st.subheader(":gray[Dados das Tabelas]")
    
    st.write("### Tabela tb_cursos:")
    cursor.execute("SELECT * FROM tb_cursos")
    cursos = cursor.fetchall()
    st.table(cursos)

    st.write("### Tabela tb_aluno:")
    cursor.execute("SELECT * FROM tb_aluno")
    alunos = cursor.fetchall()
    st.table(alunos)

# Interface do Streamlit
st.title("Sistema de gerenciamento de :orange[alunos] 🤖")
st.divider()

# Menu lateral
opcoes = ["Inserir Curso", "Inserir Aluno", "Exibir Dados"]
escolha = st.sidebar.selectbox("Selecione uma opção:", opcoes)

if escolha == "Inserir Curso":
    inserir_curso()
elif escolha == "Inserir Aluno":
    inserir_aluno()
elif escolha == "Exibir Dados":
    exibir_dados()

# Fechar a conexão com o banco de dados
conn.close()

