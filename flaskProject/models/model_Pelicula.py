from alchemyClasses import db
from alchemyClasses.Pelicula import Pelicula

def agrega_pelicula(nombre,genero=None,duracion=None,inventario=1):
    pelicula = Pelicula(nombre,genero,duracion,inventario)
    db.session.add(pelicula)
    db.session.commit()
    return "Operacion exitosa"

def muestra_peliculas():
    return Pelicula.query.all()

def muestra_pelicula(id_pelicula):
    return Pelicula.query.filter(Pelicula.idPelicula == id_pelicula).first()

def actualiza_pelicula(id_pelicula,nombre=None,genero=None,duracion=None,inventario=None):
    pelicula = Pelicula.query.filter(Pelicula.idPelicula == id_pelicula).first()
    if nombre != None:
        pelicula.nombre = nombre
    if genero != None:
        pelicula.genero = genero
    if duracion != None:
        pelicula.duracion = duracion
    if inventario != None:
        pelicula.inventario = inventario
    db.session.commit()
    return "Operacion exitosa"

def elimina_pelicula(id_pelicula):
    pelicula = Pelicula.query.filter(Pelicula.idPelicula == id_pelicula).first()
    db.session.delete(pelicula)
    db.session.commit()
    return "Operacion exitosa"

def elimina_peliculas():
    for pelicula in Pelicula.query.all():
        db.session.delete(pelicula)
    db.session.commit()
    return "Operacion exitosa"