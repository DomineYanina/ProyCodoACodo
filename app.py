from flask import Flask, request, render_template, redirect, url_for
import mysql.connector
from tkinter.messagebox import showinfo as MsgBox
app = Flask(__name__)

# Configuración de la base de datos


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="proycodoacodo"
    )  # OJO CON EL PUERTO!!!!
# OJO CON EL PUERTO!!!!
# OJO CON EL PUERTO!!!!


@app.route('/')
def index():
    return render_template('Reserva.html')


@app.route("/crear_usuario", methods=['POST'])
def crear_usuario():
    # Datos del formulario
    usuario = request.form.get("usuario")
    clave = request.form.get("clave")
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    email = request.form.get("email")
    telefono = request.form.get("telefono")
    
    # Aseguramos el uso de parámetros para prevenir inyección SQL
    query = """INSERT INTO usuario 
               (usuario, clave, nombre, apellido, email, telefono) 
               VALUES (%s, %s, %s, %s, %s, %s)"""
    params = (usuario, clave, nombre, apellido, email, telefono)
    
    # Conexión a la base de datos y ejecución de la consulta
    con = get_db_connection()
    cur = con.cursor()
    cur.execute(query, params)
    con.commit()
    con.close()
    
    # Responder al cliente
    return "Usuario creado exitosamente", 201  # Código de estado 201: Created



@app.route("/iniciar_sesion", methods=['POST'])
def iniciar_sesion():
    usuario = request.form.get("usuario")
    clave = request.form.get("clave")

    con = get_db_connection()
    cur = con.cursor()
    cur.execute("SELECT usuario, clave FROM usuario")
    usuarios = cur.fetchall()
    con.close()

    for u, c in usuarios:
        if u == usuario and c == clave:
            return "ACCESO CONCEDIDO"

    return "ACCESO DENEGADO"



@app.route('/reservar', methods=['POST'])
def reservar():
    # Obtener datos del formulario
    num_personas = request.form.get('npersonas')
    fecha_reserva = request.form.get('fecha')
    ubicacion = request.form.get('ubicacion')
    festejo = request.form.get('festejos') if request.form.get(
        'Festejo') == 'true' else None

    # Realizar la conexión a la base de datos
    conn = get_db_connection()
    cursor = conn.cursor()

    # Ejecutar la consulta SQL para insertar los datos
    query = """
    INSERT INTO reserva (num_personas, fecha_reserva, ubicacion, festejo)
    VALUES (%s, %s, %s, %s)
    """
    values = (num_personas, fecha_reserva, ubicacion, festejo)
    cursor.execute(query, values)
    conn.commit()

    # Cerrar la conexión y redirigir a la página principal
    cursor.close()
    conn.close()

    return redirect(url_for('index'))

    # TABLA BORRAME
    # nombre = request.form.get('nombre')
    # edad = request.form.get('edad')
    # conn = get_db_connection()
    # cur = conn.cursor()
    # cur.execute(
    #     f"INSERT INTO Borrame (Nombre, Edad) VALUES ('{nombre}',{str(edad)})")
    # conn.commit()
    # return "OK"


if __name__ == '__main__':
    app.run(debug=True)
