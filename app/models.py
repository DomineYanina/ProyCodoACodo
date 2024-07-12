from app.database import get_db_connection


class Usuario:
    def __init__(self, nombreUsuario, clave, nombre, apellido, email, telefono):
        self.nombreUsuario = nombreUsuario
        self.clave = clave
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

    def guardar(self):
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO usuario (nombreUsuario, clave, nombre, apellido, email, telefono) VALUES (%s, %s, %s, %s, %s, %s)",
            (self.nombreUsuario, self.clave, self.nombre, self.apellido,
            self.email, self.telefono)
        )
        db.commit()
        cursor.close()


    @staticmethod
    def traer_todos():
        db = get_db_connection()
        cur = db.cursor()
        cur.execute("SELECT * FROM usuario")
        registros = cur.fetchall()
        usuarios = []
        for registro in registros:
            usuarios.append(Usuario(
                registro[0], registro[1], registro[2], registro[3], registro[4], registro[5]))
        cur.close()
        return usuarios

    @staticmethod
    def buscar_por_email(emailUsuario):
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuario WHERE email=%s", (emailUsuario,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Usuario(id=row[0], email=row[1], clave=row[2])
        return None

    def verificar_contrasena(self, clave):
        return self.clave == clave

    @staticmethod
    def traer_uno(id):
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuario WHERE id=%s", (id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Usuario(id=row[0], usuario=row[1], clave=row[2], nombre=row[3], apellido=row[4], email=row[5])
        return None

    def eliminar(self):
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("DELETE FROM usuario WHERE id=%s", (self.id,))
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'id': self.id,
            'usuario': self.nombreUsuario,
            'clave': self.clave,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'telefono': self.telefono
        }


class Reserva:
    def __init__(self, cantidadPersonas, fecha, ubicacion, ocasionEspecialCual, emailUsuario, telefonoUsuario, nombreCompletoUsuario):
        self.cantidadPersonas = cantidadPersonas
        self.fecha = fecha
        self.ubicacion = ubicacion
        self.ocasionEspecialCual = ocasionEspecialCual
        self.emailUsuario = emailUsuario
        self.telefonoUsuario = telefonoUsuario
        self.nombreCompletoUsuario = nombreCompletoUsuario

    def guardar(self):
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO reserva (cantidadPersonas, fecha, ubicacion, ocasionEspecialCual, mailUsuario, telefonoUsuario, nombreCompletoUsuario) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (self.cantidadPersonas, self.fecha, self.ubicacion, self.ocasionEspecialCual,
             self.emailUsuario, self.telefonoUsuario, self.nombreCompletoUsuario)
        )
        db.commit()
        cursor.close()

    @staticmethod
    def traer_todos():
        db = get_db_connection()
        cur = db.cursor()
        cur.execute("SELECT * FROM reserva")
        registros = cur.fetchall()
        reservas = []
        for registro in registros:
            reservas.append(Reserva(
                registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7]))
        cur.close()
        return reservas

    @staticmethod
    def traer_uno(emailUsuario):
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM reserva WHERE emailUsuario=%s", (emailUsuario,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Reserva(idReserva=row[0], cantidadPersonas=row[1], fecha=row[2], ubicacion=row[3], ocasionEspecialCual=row[4], idUsuario=row[5])
        return None

    def eliminar(self):
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("DELETE FROM reserva WHERE idReserva=%s",
                       (self.emailUsuario,))
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'idReserva': self.idReserva,
            'cantidadPersonas': self.cantidadPersonas,
            'fecha': self.fecha.isoformat(),  # Formatear la fecha si es necesario
            'ubicacion': self.ubicacion,
            'ocasionEspecialCual': self.ocasionEspecialCual,
            'emailUsuario': self.emailUsuario,
            'telefonoUsuario': self.telefonoUsuario,
            'nombreCompletoUsuario': self.nombreCompletoUsuario,
            # Añadir más campos si es necesario
        }
