from alchemyClasses import db
from alchemyClasses.Pelicula import Pelicula

def muestra_peliculas():
    return Pelicula.query.all()

def muestra_pelicula(id_pelicula):
    return Pelicula.query.filter(Pelicula.idPelicula == id_pelicula).first()

def actualiza_pelicula(id_pelicula,nombre):
    pelicula = Pelicula.query.filter(Pelicula.idPelicula == id_pelicula).first()
    pelicula.nombre = nombre
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
