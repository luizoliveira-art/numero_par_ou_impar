from flask import Flask, request

app = Flask(__name__)

# Rotas
@app.route('/')
def home():
    return 'bem-vindo à homepage, digite "/num" para começar.'

@app.route('/num', methods=['GET', 'POST'])
def num():
    if request.method == 'POST':
        numero = int(request.form.get('numero'))
        if numero % 2 == 0:
            return 'O número é Par' 
        else:
            return'O número é Ímpar'
    return """
    <form method="POST">
        Numero: <input type="number" step="any" name="numero" required>
        <button type="submit">Enviar</button>
    </form>
    """

if __name__ == '__main__':
    app.run(debug=True)
# cd num_par_ou_imp, cd flask, python3 main.py
