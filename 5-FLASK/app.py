from flask import Flask, render_template, request
from lista_filmes import dados_json

app = Flask(__name__)

conteudos = []
registros = []
# Localhost:500/
@app.route('/', methods=['GET', 'POST'])
def principal():
    if request.method == 'POST':
        if request.form.get('conteudo'): # GET pq quer só pegar o conteudo do html
            conteudos.append(request.form.get('conteudo'))
    return render_template(
        "index.html",
        conteudos=conteudos
    ) # retornando conteúdo para a pág web


@app.route('/diario', methods=['GET', 'POST'])
def diario():
    if request.method == "POST":
        if request.form.get('aluno') and request.form.get('nota'):
            aluno = request.form.get('aluno')
            nota = request.form.get('nota')
            registros.append(
                {
                    'aluno': aluno,
                    'nota': nota
                }
            )
    return render_template(
        'sobre.html',
        registros=registros
    )


@app.route('/filmes')
def lista_filmes():
    return render_template(
        'filmes.html',
        filmes=dados_json['results']
    )
app.run(debug=True) # debug seria atualização do meu código em tempo real