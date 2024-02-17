from flask import Flask , render_template, request
app = Flask(__name__)  # é uma variável especial em Python que representa o nome do módulo. Quando um script Python é executado, o Python atribui automaticamente o valor __main__ à variável __name__ se o script estiver sendo executado como o programa principal. Se o script estiver sendo importado como um módulo em outro script, __name__ terá o nome do módulo.  Essa linha cria uma instância da classe Flask e a associa à variável app. A variável __name__ é passada como argumento para informar ao Flask onde encontrar os recursos do aplicativo, como modelos e arquivos estáticos.

lista=[]

@app.route("/")
@app.route('/index') #rota alternativa, caso o usuário digite no navegador o nome do site /index.
def index(): #cria o método index para executar o resultado de exibir a página html.
    return render_template ("index.html" ) # o index.html e todas as paginas html têm que estar dentro da pasta templates. 

@app.route('/cadastra', methods=['POST'])
def cadastra():
    nome = request.form.get('nome')
    data = request.form.get('data')
    descricao =request.form.get('descricao')
    lista.append({'nome': nome, 'data': data,'descicao':descricao})
    
    return """
    <script>
    alert('Dados adicionados com sucesso');
    window.location.href = '/';
    </script>
        
"""

@app.route('/exibirdados')
def exibirdados():
    return render_template('visualiza.html',lista=lista)

if __name__ == "__main__":
    app.run(debug=True)