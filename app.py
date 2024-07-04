from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3307,
        user="root",
        password="",
        database="proycodoacodo"
    )

@app.route('/')
def index():
    return render_template('Reserva.html')

@app.route('/reservar', methods=['POST'])
def reservar():
    # Obtener datos del formulario
    nombre = request.form.get('name')
    apellido = request.form.get('lastName')
    telefono = request.form.get('number')
    email = request.form.get('email')
    num_personas = request.form.get('npersonas')
    fecha_reserva = request.form.get('message')
    ubicacion = request.form.get('ubicacion')
    festejo = request.form.get('festejos') if request.form.get('Festejo') == 'true' else None

    # Realizar la conexión a la base de datos
    conn = get_db_connection()
    cursor = conn.cursor()

    # Ejecutar la consulta SQL para insertar los datos
    query = """
    INSERT INTO reserva (nombre, apellido, telefono, email, num_personas, fecha_reserva, ubicacion, festejo)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (nombre, apellido, telefono, email, num_personas, fecha_reserva, ubicacion, festejo)
    cursor.execute(query, values)
    conn.commit()

    # Cerrar la conexión y redirigir a la página principal
    cursor.close()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
