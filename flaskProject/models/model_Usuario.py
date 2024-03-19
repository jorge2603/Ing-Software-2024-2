from alchemyClasses import db
from alchemyClasses.Usuario import Usuario

def muestra_usuarios():
    return Usuario.query.all()

def muestra_usuario(id_usuario):
    return Usuario.query.filter(Usuario.idUsuario == id_usuario).first()

def actualiza_usuario(id_usuario,nombre):
    usuario = Usuario.query.filter(Usuario.idUsuario == id_usuario).first()
    usuario.nombre = nombre
    db.session.commit()
    return "Operacion exitosa"

def elimina_usuario(id_usuario):
    usuario = Usuario.query.filter(Usuario.idUsuario == id_usuario).first()
    db.session.delete(usuario)
    db.session.commit()
    return "Operacion exitosa"

def elimina_usuarios():
    for usuario in Usuario.query.all():
        db.session.delete(usuario)
    db.session.commit()
    return "Operacion exitosa"