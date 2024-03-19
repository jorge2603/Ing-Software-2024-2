from flask import Blueprint, request, render_template, flash, url_for
from random import randint
from models.model_Usuario import *

usuario_blueprint = Blueprint('Usuarios', __name__, url_prefix='/Usuarios')

@usuario_blueprint.route('/') #localhost:5000/Usuarios/
def inicio():
    return render_template('Usuario.html')

@usuario_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_Usuario():
    if request.method == 'GET':
        return render_template('agregar_Usuario.html')
    else:
        nombre = request.form['nombre']
        apPat = request.form['apPat']
        apMat = request.form['apMat']
        email = request.form['email']
        password = request.form['password']
        superUser = request.form['superUser']
        agrega_usuario(nombre,apPat,apMat,email,password,superUser)
        return "Operacion exitosa"



@usuario_blueprint.route('/mostrar') #localhost:5000/Usuarios/mostrar
def mostrar_Usuarios():
    Usuarios=muestra_usuarios()
    return render_template('regresa_Usuarios.html', Usuarios=Usuarios)

@usuario_blueprint.route('/actualizar',methods=['GET', 'POST']) #localhost:5000/Usuarios/actualizar
def actualizar_Usuario():
    if request.method == 'GET':
        return render_template('actualizar_Usuario.html')
    else:
        id_Usuario = request.form['id']
        nombre = request.form['nombre']
        apPat = request.form['apPat']
        apMat = request.form['apMat']
        email = request.form['email']
        password = request.form['password']
        superUser = request.form['superUser']
        actualiza_usuario(id_Usuario,nombre,apPat,apMat,email,password,superUser)
        return "Operacion exitosa"
    
@usuario_blueprint.route('/eliminar',methods=['GET', 'POST']) #localhost:5000/Usuarios/eliminar
def eliminar_Usuario():
    if request.method == 'GET':
        return render_template('elimina_Usuario.html')
    else:
        id_Usuario = request.form['id']
        elimina_usuario(id_Usuario)
        return "Operacion exitosa"
    



    
