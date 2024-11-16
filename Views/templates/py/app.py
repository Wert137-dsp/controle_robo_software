# Importa a classe Flask e a função render_template da biblioteca Flask
from flask import Flask, render_template

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Define a rota para a página inicial
@app.route('/')
def home():
    # Renderiza o template 'telaHome.html' quando a rota '/' é acessada
    return render_template('telaPrincipal.html')

# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    # Executa a aplicação Flask em modo de depuração
    app.run(debug=True)
