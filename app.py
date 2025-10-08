from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('plantilla-base.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/animales-exoticos')
def animales_exoticos():
    return render_template('animales-exoticos.html')

@app.route('/vehiculos-antiguos')
def vehiculos_antiguos():
    return render_template('vehiculos')

@app.route('/las-maravillas-del-mundo')
def las_maravillas_del_mundo():
    return render_template('las-maravillas-del-mundo.html')

@app.route('/acerca-de')
def acerca_de():
    return render_template('acerca-de.html')

if __name__ == '__main__':
    app.run(debug=True)