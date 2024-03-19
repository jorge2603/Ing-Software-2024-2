from flask import Blueprint, request, render_template, flash, url_for
from random import randint
from models.model_Pelicula import *

pelicula_blueprint = Blueprint('peliculas', __name__, url_prefix='/peliculas')

@pelicula_blueprint.route('/') #localhost:5000/peliculas/
def inicio():
    return render_template('Pelicula.html')

@pelicula_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_pelicula():
    if request.method == 'GET':
        return render_template('agregar_pelicula.html')
    else:
        nombre = request.form['nombre']
        genero = request.form['genero']
        duracion = request.form['duracion']
        inventario = request.form['inventario']
        agrega_pelicula(nombre,genero,duracion,inventario)
        return "Operacion exitosa"



@pelicula_blueprint.route('/mostrar') #localhost:5000/peliculas/mostrar
def mostrar_peliculas():
    peliculas=muestra_peliculas()
    return render_template('regresa_peliculas.html', peliculas=peliculas)

@pelicula_blueprint.route('/actualizar',methods=['GET', 'POST']) #localhost:5000/peliculas/actualizar
def actualizar_pelicula():
    if request.method == 'GET':
        return render_template('actualizar_pelicula.html')
    else:
        id_pelicula = request.form['id']
        nombre = request.form['nombre']
        genero = request.form['genero']
        duracion = request.form['duracion']
        inventario = request.form['inventario']
        actualiza_pelicula(id_pelicula,nombre,genero,duracion,inventario)
        return "Operacion exitosa"
    
@pelicula_blueprint.route('/eliminar',methods=['GET', 'POST']) #localhost:5000/peliculas/eliminar
def eliminar_pelicula():
    if request.method == 'GET':
        return render_template('elimina_pelicula.html')
    else:
        id_pelicula = request.form['id']
        elimina_pelicula(id_pelicula)
        return "Operacion exitosa"
    



    
