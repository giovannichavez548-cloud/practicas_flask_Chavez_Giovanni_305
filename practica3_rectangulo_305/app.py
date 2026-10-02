from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('rectangulo'))

@app.route('/rectangulo', methods=['GET', 'POST'])
def rectangulo():
    resultado = None
    resultado2 = None

    if request.method == 'POST':
        base_input = request.form.get('base')
        altura_input = request.form.get('altura')

        if base_input and altura_input:
            base = float(base_input)
            altura = float(altura_input)

            resultado = base * altura
            resultado2 = 2 * (base + altura)

    return render_template('rectangulo.html', resultado=resultado, resultado2=resultado2)

if __name__ == '__main__':
    app.run(debug=True)