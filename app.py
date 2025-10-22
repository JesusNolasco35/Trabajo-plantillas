from flask import Flask, render_template, request, redirect, url_for, flash

hola 

app = Flask(__name__)
app.secret_key = '2423415414'  

@app.route('/')
def inicio():
    return redirect(url_for('index')) 

@app.route('/index')
def index():
    return render_template('inicio.html')

@app.route('/registro', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nombres = request.form.get('nombres')
        email = request.form.get('email')
        contraseña = request.form.get('pass')  
        confirmarcontraseña = request.form.get('passConfirm')  
        dia = request.form.get('dia')


        if contraseña != confirmarcontraseña:
            flash("Las contraseñas no coinciden.", "error")
            return redirect(url_for('registrar'))

        print(f"Nuevo registro: {nombres}- {email}")
        return redirect(url_for('index'))

    return render_template('registro.html')

@app.route('/acerca')
def acerca():
    return render_template('Acerca-de.html')     

@app.route('/animales')
def animales():
    return render_template('animales-exoticos.html')

@app.route('/vehiculos')
def vehiculos():
    return render_template('vehiculos.html')

@app.route('/maravillas')
def maravillas():
    return render_template('maravillas.html')

if __name__ == '__main__':
    app.run(debug=True)
