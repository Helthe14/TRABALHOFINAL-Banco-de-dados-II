# models.py
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

#Modelo do Aluno
class Aluno(db.Model):
    __tablename__ = 'tb_aluno'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(20), nullable=False)
    curso = db.Column(db.String(100), nullable=False)
    nivel = db.Column(db.String(50), nullable=False)

    emprestimos = db.relationship('Emprestimo', backref='aluno', lazy=True)

#Modelo do Livro
class Livro(db.Model):
    __tablename__ = 'tb_livro'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    id_status = db.Column(db.Integer, db.ForeignKey('tb_status.id'), nullable=False)
    imagem = db.Column(db.String(255), nullable=True)

    # Relacionamento com status
    id_status = db.Column(db.Integer, db.ForeignKey('tb_status.id'))
    status = db.relationship('Status', backref=db.backref('livros', lazy=True))

    emprestimos = db.relationship('Emprestimo', backref='livro', lazy=True)

#Modelo do Empréstimo
class Emprestimo(db.Model):
    __tablename__ = 'tb_emprestimo'
    id = db.Column(db.Integer, primary_key=True)
    id_aluno = db.Column(db.Integer, db.ForeignKey('tb_aluno.id'))
    id_livro = db.Column(db.Integer, db.ForeignKey('tb_livro.id'))
    data = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)  # A data é registrada automaticamente


#Modelo do Status
class Status(db.Model):
    __tablename__ = 'tb_status'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), nullable=False)

# config.py

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/biblioteca'  # Conecta ao banco "biblioteca" no XAMPP
    SQLALCHEMY_TRACK_MODIFICATIONS = False
