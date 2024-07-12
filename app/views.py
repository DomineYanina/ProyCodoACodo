from flask import app, jsonify, render_template, request, jsonify, url_for
from app.models import Reserva, Usuario  # Ajusta la importación de modelos según la estructura de tu proyecto

def index():
    return jsonify({'message': "Bienvenidos a la API de la Taberna de Moe"})

def crear_usuario():
    nombreUsuario = request.form.get("usuario")
    clave = request.form.get("clave")
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    email = request.form.get("email")
    telefono = request.form.get("telefono")

    nuevo_usuario = Usuario(
        nombreUsuario=nombreUsuario,
        clave=clave,
        nombre=nombre,
        apellido=apellido,
        email=email,
        telefono=telefono,
    )
    nuevo_usuario.guardar()

    return render_template("confirmaciónNuevoUsuario.html"), 201

def traer_usuarios():
    usuarios = Usuario.traer_todos()
    return jsonify([usuario.serialize() for usuario in usuarios])

def traer_usuario(id):
    usuario = Usuario.traer_uno(id)
    if not usuario:
        return jsonify({'message': 'Usuario no encontrado'}), 404
    return jsonify(usuario.serialize())

def actualizar_usuario(id):
    usuario = Usuario.traer_uno(id)
    if not usuario:
        return jsonify({'message': 'Usuario no encontrado'}), 404
    data = request.json
    usuario.nombreUsuario = data['usuario']
    usuario.clave = data['clave']
    usuario.nombre = data['nombre']
    usuario.apellido = data['apellido']
    usuario.email = data['email']
    usuario.telefono = data['telefono']
    usuario.guardar()
    return jsonify({'message': 'Usuario actualizado.'})

def eliminar_usuario(id):
    usuario = Usuario.traer_uno(id)
    if not usuario:
        return jsonify({'message': 'Usuario no encontrado'}), 404
    usuario.eliminar()
    return jsonify({'message': 'Usuario eliminado satisfactoriamente.'})

# Aquí comienza la corrección para la parte de reservas

def crear_reserva():
    cantidadPersonas = request.form.get("npersonas")
    fecha = request.form.get("fecha")
    ubicacion = request.form.get("ubicacion")
    ocasionEspecialCual = request.form.get("festejos")
    emailUsuario = request.form.get("mailUsuario")
    telefonoUsuario = request.form.get("telefonoUsuario")
    nombreCompletoUsuario = request.form.get("nombreUsuario")

    nueva_reserva = Reserva(
        cantidadPersonas=cantidadPersonas,
        fecha=fecha,
        ubicacion=ubicacion,
        ocasionEspecialCual=ocasionEspecialCual,
        emailUsuario=emailUsuario,
        telefonoUsuario=telefonoUsuario,
        nombreCompletoUsuario=nombreCompletoUsuario
    )
    nueva_reserva.guardar()

    return render_template("confirmaciónReserva.html"), 201

def traer_reservas():
    reservas = Reserva.traer_todos()
    return jsonify([reserva.serialize() for reserva in reservas]), 200

def traer_reserva(emailUsuario):
    reserva = Reserva.traer_uno(emailUsuario)
    if not reserva:
        return jsonify({'message': 'Reserva no encontrada'}), 404

    reserva_data = {
        'idReserva': reserva.idReserva,
        'cantidadPersonas': reserva.cantidadPersonas,
        'fecha': reserva.fecha.strftime('%Y-%m-%d'),
        'ubicacion': reserva.ubicacion,
        'ocasionEspecialCual': reserva.ocasionEspecialCual,
        'emailUsuario': reserva.emailUsuario,
        'telefonoUsuario': reserva.telefonoUsuario,
        'nombreCompletoUsuario': reserva.nombreCompletoUsuario
    }

    return jsonify(reserva_data)

def actualizar_reserva(emailUsuario):
    reserva = Reserva.traer_uno(emailUsuario)
    if not reserva:
        return jsonify({'message': 'Reserva no encontrado'}), 404

    data = request.json
    reserva.cantidadPersonas = data['cantidadPersonas']
    reserva.fecha = data['fecha']
    reserva.ubicacion = data['ubicacion']
    reserva.ocasionEspecialCual = data['ocasionEspecialCual']
    reserva.idUsuario = data['idUsuario']
    reserva.guardar()
    return jsonify({'message': 'Reserva actualizada.'})

def eliminar_reserva(emailUsuario):
    reserva = Reserva.traer_uno(emailUsuario)
    if not reserva:
        return jsonify({'message': 'Reserva no encontrada'}), 404

    reserva.eliminar()
    return jsonify({'message': 'Reserva eliminada satisfactoriamente.'})
