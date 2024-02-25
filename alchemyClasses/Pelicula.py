from sqlalchemy import Integer, String, Column

from alchemyClasses import db

class Pelicula(db.Model):
    __tablename__ = 'peliculas'
    idPelicula = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200))
    genero = Column(String(45), nullable=True)
    duracion = Column(Integer, nullable=True)
    inventario = Column(Integer)

    def __init__(self, nombre, genero=None, duracion=None, inventario=1):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.inventario = inventario
    
    def __str__(self):
        return f'Nombre:{self.nombre}\nGenero:{self.genero}\nDuracion:{self.duracion}\nInventario:{self.inventario}'