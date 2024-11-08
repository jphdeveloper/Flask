# importamos las clases y metodos
from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def aritmetica():
    if request.method == "POST":
        # Valores que recibo del form n1, n2 son pasados
        num1 = float(request.form.get('n1'))
        num2 = float(request.form.get('n2'))
        # Realizamos operaciones aritméticas
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        division = num1 / num2
        return render_template('index.html', total_suma=suma,
                               total_resta=resta,
                               total_multiplicacion=multiplicacion,
                               total_division=division)
    return render_template('index.html')

@app.route('/divisas', methods=['GET', 'POST'])
def divisas():
    tasa_cambio = 4398  # Tasa de cambio de ejemplo: 1 USD = 4398 COP
    if request.method == "POST":
        # Obtenemos el valor en dólares del formulario
        dolares = float(request.form.get('n1'))
        # Convertimos a pesos colombianos
        pesos_colombianos = dolares * tasa_cambio
        return render_template('divisas.html', resultado_conversion=pesos_colombianos)
    return render_template('divisas.html')

if __name__ == "__main__":
    app.run(debug=True)
