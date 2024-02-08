from app import db
from datetime import datetime


class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(14))  # Formato: 000.000.000-00
    matricula = db.Column(db.String(20))
    data_nascimento = db.Column(db.Date)
    curso = db.Column(db.String(100))
    periodo = db.Column(db.Integer)
    celular = db.Column(db.String(15))  # Formato: (00) 00000-0000
    email = db.Column(db.String(120))
    ativo = db.Column(db.Boolean)


class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(14))
    rg = db.Column(db.String(20))
    data_nascimento = db.Column(db.Date)
    logradouro = db.Column(db.String(150))
    numero = db.Column(db.String(10))
    complemento = db.Column(db.String(50))
    bairro = db.Column(db.String(100))
    cep = db.Column(db.String(9))  # Formato: 00000-000
    cidade = db.Column(db.String(100))
    uf = db.Column(db.String(2))
    celular = db.Column(db.String(15))
    telefone = db.Column(db.String(14))  # Formato: (00) 0000-0000
    email = db.Column(db.String(120))
    ativo = db.Column(db.Boolean)


class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(14))
    matricula = db.Column(db.String(20))
    data_nascimento = db.Column(db.Date)
    # Cursos e Disciplinas podem ser implementados como relacionamentos
    celular = db.Column(db.String(15))
    email = db.Column(db.String(120))
    ativo = db.Column(db.Boolean)


class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    area = db.Column(db.String(100))
    carga_horaria = db.Column(db.Integer)


class Disciplina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    curso_id = db.Column(db.Integer, db.ForeignKey("curso.id"))
    carga_horaria = db.Column(db.Integer)


class Prontuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey("aluno.id"))
    supervisor_id = db.Column(db.Integer, db.ForeignKey("professor.id"))
    data_atendimento = db.Column(db.Date)
    horario_inicio = db.Column(db.Time)
    horario_final = db.Column(db.Time)
    registro_atendimento = db.Column(db.Text)
    observacoes_supervisor = db.Column(db.Text)


class Artigo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200))
    autor_id = db.Column(db.Integer, db.ForeignKey("professor.id"))
    data_hora_publicacao = db.Column(db.DateTime, default=datetime.utcnow)
    conteudo = db.Column(db.Text)
    tags = db.Column(db.String(200))  # Lista de tags separadas por vírgula
