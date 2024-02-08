from flask import redirect, render_template, request, url_for

from app import app

# Importar modelos conforme necessário


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


# Rotas para Alunos
@app.route("/alunos")
def alunos():
    # Lógica para listar alunos
    return render_template("alunos/alunos.html")


@app.route("/alunos/novo", methods=["GET", "POST"])
def novo_aluno():
    # Lógica para criar um novo aluno
    if request.method == "POST":
        # Processar dados do formulário
        pass
    return render_template("novo_aluno.html")


# Rotas para Pacientes
@app.route("/pacientes")
def pacientes():
    # Lógica para listar pacientes
    return render_template("pacientes.html")


@app.route("/pacientes/novo", methods=["GET", "POST"])
def novo_paciente():
    # Lógica para criar um novo paciente
    if request.method == "POST":
        # Processar dados do formulário
        pass
    return render_template("novo_paciente.html")


# Rotas para Professores
@app.route("/professores")
def professors():
    # Lógica para listar professors
    return render_template("professores.html")


@app.route("/professores/novo", methods=["GET", "POST"])
def novo_professor():
    # Lógica para criar um novo professor
    if request.method == "POST":
        # Processar dados do formulário
        pass
    return render_template("novo_professor.html")


# Rotas para Cursos
@app.route("/cursos")
def cursos():
    # Lógica para listar cursos
    return render_template("cursos.html")


@app.route("/cursos/novo", methods=["GET", "POST"])
def novo_curso():
    # Lógica para criar um novo curso
    if request.method == "POST":
        # Processar dados do formulário
        pass
    return render_template("novo_curso.html")


# Rotas para Disciplinas
@app.route("/disciplinas")
def disciplinas():
    # Lógica para listar disciplinas
    return render_template("disciplinas.html")


@app.route("/disciplinas/novo", methods=["GET", "POST"])
def novo_disciplina():
    # Lógica para criar um novo disciplina
    if request.method == "POST":
        # Processar dados do formulário
        pass
    return render_template("novo_disciplina.html")


# Rotas para Prontuários
@app.route("/prontuarios")
def prontuarios():
    # Lógica para listar prontuários
    return render_template("prontuarios.html")


@app.route("/prontuarios/novo", methods=["GET", "POST"])
def novo_prontuario():
    # Lógica para criar um novo prontuário
    return render_template("novo_prontuario.html")


# Rotas para Artigos (Blog)
@app.route("/artigos")
def artigos():
    # Lógica para listar artigos
    return render_template("artigos.html")


@app.route("/artigos/novo", methods=["GET", "POST"])
def novo_artigo():
    # Lógica para criar um novo artigo
    return render_template("novo_artigo.html")
