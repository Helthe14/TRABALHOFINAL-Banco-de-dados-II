import os
from flask import Flask, render_template, request, redirect, url_for , flash 
from models import db, Livro, Emprestimo, Aluno, Status
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

app.secret_key = os.urandom(24)
# Inicializar o banco de dados
db.init_app(app)

# Rota para cadastrar ou atualizar um aluno
@app.route('/cadastrar_aluno', methods=['GET', 'POST'])
def cadastrar_aluno():
    aluno = None  # Para armazenar o aluno se estivermos editando
    message = 'Aluno Cadastro com Sucesso!'  # Para armazenar a mensagem de sucesso

    if request.method == 'POST':
        # Pegando os dados do formulário
        nome = request.form['nome']
        matricula = request.form['matricula']
        curso = request.form['curso']
        nivel = request.form['nivel']
        aluno_id = request.form.get('id')  # Se houver um ID, significa que estamos editando

        if aluno_id:  # Atualizando um aluno existente
            aluno = Aluno.query.get(aluno_id)
            aluno.nome = nome
            aluno.matricula = matricula
            aluno.curso = curso
            aluno.nivel = nivel
            message = "Aluno atualizado com sucesso!"
        else:  # Cadastrando um novo aluno
            novo_aluno = Aluno(nome=nome, matricula=matricula, curso=curso, nivel=nivel)
            db.session.add(novo_aluno)
            message = "Aluno cadastrado com sucesso!"

        # Salvando no banco de dados
        db.session.commit()
        flash(message)  # Exibe a mensagem de sucesso
        return redirect(url_for('cadastrar_aluno'))

    # Carregar dados do aluno para edição
    aluno_id = request.args.get('id')
    if aluno_id:
        aluno = Aluno.query.get(aluno_id)

    # Pesquisa de alunos ou carregando todos
    search_term = request.args.get('search')
    if search_term:
        alunos = Aluno.query.filter(Aluno.nome.like(f'%{search_term}%') | Aluno.matricula.like(f'%{search_term}%')).all()
    else:
        alunos = Aluno.query.all()

    return render_template('cadastrar_aluno.html', alunos=alunos, aluno=aluno, search_term=search_term)

# Rota para deletar aluno (opcional)
@app.route('/deletar_aluno/<int:id>', methods=['GET', 'POST'])
def deletar_aluno(id):
    aluno = Aluno.query.get(id)
    if aluno:
        db.session.delete(aluno)
        db.session.commit()
        flash('Aluno deletado com sucesso!')
    return redirect(url_for('cadastrar_aluno'))

# Rota para cadastrar um novo livro
@app.route('/cadastrar_livro', methods=['GET', 'POST'])
def cadastrar_livro():
    livro = None

    # Verifique se o parâmetro 'id' foi passado pela URL para carregar um livro específico
    livro_id = request.args.get('id')
    if livro_id:
        livro = Livro.query.get(livro_id)
        if not livro:
            flash(f'Livro com ID {livro_id} não encontrado.', 'error')

    if request.method == 'POST':
        if 'pesquisar' in request.form:  # Se o botão de pesquisa foi pressionado
            nome = request.form.get('nome').lower()
            livros_encontrados = Livro.query.filter(Livro.nome.ilike(f'%{nome}%')).all()
            if not livros_encontrados:
                flash(f"Nenhum livro encontrado com o nome '{nome}'", 'error')
            else:
                flash(f"Livros encontrados com o nome '{nome}'.", 'success')
                return render_template('cadastrar_livro.html', livros=livros_encontrados)

        elif 'update' in request.form:  # Se o botão de atualização foi pressionado
            livro_id = request.form.get('id')
            livro = Livro.query.get(livro_id)
            if livro:
                titulo = request.form.get('titulo')
                if not titulo:
                    flash('O campo título não pode estar vazio.', 'error')
                    return redirect(url_for('cadastrar_livro', id=livro_id))

                # Atualizar os campos do livro
                livro.nome = titulo
                livro.ano = request.form.get('ano')
                livro.autor = request.form.get('autor')
                livro.imagem = request.form.get('imagem')
                livro.id_status = request.form.get('status')

                db.session.commit()
                flash('Livro atualizado com sucesso!', 'success')
                return redirect(url_for('cadastrar_livro', id=livro_id))
            else:
                flash('Livro não encontrado para atualização.', 'error')
        elif 'titulo' in request.form:  # Caso seja um novo cadastro
            titulo = request.form.get('titulo')
            ano = request.form.get('ano')
            autor = request.form.get('autor')
            imagem = request.form.get('imagem')
            status_id = request.form.get('status')

            novo_livro = Livro(nome=titulo, ano=ano, autor=autor, id_status=status_id, imagem=imagem)
            db.session.add(novo_livro)
            db.session.commit()
            flash('Livro cadastrado com sucesso!', 'success')
            return redirect(url_for('cadastrar_livro'))

    # Pegando todos os status disponíveis para o dropdown de status
    status_list = Status.query.all()

    return render_template('cadastrar_livro.html', status_list=status_list, livro=livro)

# Rota para emprestar um livro
@app.route('/emprestar_livro', methods=['GET', 'POST'])
def emprestar_livro():
    resultados = []
    termo = None
    ver_mais = request.args.get('ver_mais', False)
    livro_selecionado = None

    if request.method == 'POST':
        if 'pesquisar' in request.form:
            termo = request.form['termo'].lower()
            resultados = Livro.query.filter(Livro.nome.ilike(f'%{termo}%')).all()
            if not resultados:
                flash(f"Nenhum livro encontrado com o nome '{termo}'", 'error')
        elif 'emprestar' in request.form:
            livro_id = request.form['livro_id']
            aluno_matricula = request.form['aluno_matricula']

            aluno = Aluno.query.filter_by(matricula=aluno_matricula).first()
            livro = Livro.query.get(livro_id)

            if not aluno:
                flash(f'Aluno com matrícula "{aluno_matricula}" não encontrado.', 'error')
            else:
                # Realizar o empréstimo (correção aqui: use 'data' e não 'data_emprestimo')
                emprestimo = Emprestimo(id_aluno=aluno.id, id_livro=livro.id, data=datetime.now())
                livro.id_status = 2  # Alterar o status do livro para "Emprestado"
                db.session.add(emprestimo)
                db.session.commit()
                flash(f'Empréstimo do livro "{livro.nome}" para {aluno.nome} realizado com sucesso.', 'success')

    # Exibir lista de livros disponíveis (id_status = 1)
    if ver_mais:
        livros_disponiveis = Livro.query.filter_by(id_status=1).all()  # Exibe todos
    else:
        livros_disponiveis = Livro.query.filter_by(id_status=1).limit(5).all()  # Limita a 5 livros

    return render_template('emprestimo.html', resultados=resultados, termo=termo, livros_disponiveis=livros_disponiveis, livro_selecionado=livro_selecionado)



# Rota para listar livros emprestados
@app.route('/livros_emprestados')
def listar_emprestimos():
    emprestimos = Emprestimo.query.join(Livro).join(Aluno).all()
    return render_template('livros_emprestados.html', emprestimos=emprestimos)

# Rota Pesquisar Livro
@app.route('/pesquisar_livro', methods=['GET', 'POST'])
def pesquisar_livro():
    resultados = []
    termo = None
    ver_mais = request.args.get('ver_mais', False)

    if request.method == 'POST':
        termo = request.form['termo'].lower()
        resultados = Livro.query.filter(Livro.nome.ilike(f'%{termo}%')).all()
        if not resultados:
            flash(f"Nenhum livro encontrado com o nome '{termo}'", 'error')

    # Lista apenas os livros disponíveis (id_status = 1)
    if ver_mais:
        livros_disponiveis = Livro.query.filter_by(id_status=1).all()  # Exibe todos
    else:
        livros_disponiveis = Livro.query.filter_by(id_status=1).limit(5).all()  # Limita a 5 livros

    return render_template('pesquisar_livro.html', resultados=resultados, termo=termo, livros_disponiveis=livros_disponiveis, ver_mais=ver_mais)



# Rota para a página inicial
@app.route('/')
def index():
    livros = Livro.query.all()  # Buscando todos os livros no banco de dados
    print(livros)  # Verifique se a lista de livros não está vazia
    return render_template('index.html', livros=livros)  # Passando a lista de livros para o template

# Rota Devolução
@app.route('/devolucao', methods=['GET', 'POST'])
def devolucao():
    emprestimos = []
    termo = None

    if request.method == 'POST':
        # Verificar se a devolução foi solicitada (o 'livro_id' deve estar presente)
        livro_id = request.form.get('livro_id')

        if livro_id:
            # Buscar o empréstimo do livro
            emprestimo = Emprestimo.query.filter_by(id_livro=livro_id).first()
            
            if emprestimo:
                # Atualizar o status do livro para disponível (id_status = 1)
                livro = Livro.query.get(livro_id)
                livro.id_status = 1  # Disponível
                
                # Remover o empréstimo
                db.session.delete(emprestimo)
                db.session.commit()
                
                flash(f'Livro "{livro.nome}" devolvido com sucesso!', 'success')
            else:
                flash(f'Livro não encontrado para devolução.', 'error')
            
            return redirect(url_for('devolucao'))

        # Pesquisa de livros por nome (caso não seja devolução)
        termo = request.form.get('termo', '').lower()

        # Buscar empréstimos com o nome correspondente e status de emprestado (id_status = 2)
        emprestimos = Emprestimo.query.join(Livro).join(Aluno).filter(
            Livro.nome.ilike(f'%{termo}%'), Livro.id_status == 2  # Status 2 = Emprestado
        ).all()

        if not emprestimos:
            flash(f"Nenhum livro encontrado para devolução com o nome '{termo}'.", 'error')
        else:
            flash(f"Livro(s) encontrado(s) com o nome '{termo}' para devolução.", 'success')
    
    else:
        # Caso não haja uma pesquisa, carregar todos os livros emprestados (id_status = 2)
        emprestimos = Emprestimo.query.join(Livro).join(Aluno).filter(
            Livro.id_status == 2  # Status 2 para Emprestado
        ).all()

    return render_template('devolucao.html', emprestimos=emprestimos, termo=termo)


if __name__ == '__main__':
    app.run(debug=True)
