from sqlalchemy import Integer, String, Column,ForeignKey,DateTime
from alchemyClasses import db, Usuario, Pelicula

class Renta(db.Model):
    __tablename__ = 'rentar'
    idRentar = Column(Integer, primary_key=True, autoincrement=True)
    idUsuario = Column(Integer,ForeignKey('usuarios.idUsuario'), nullable=False)
    idPelicula = Column(Integer,ForeignKey('peliculas.idPelicula'), nullable=False)
    fecha_renta = Column(DateTime, nullable=False)
    dias_de_renta = Column(Integer)
    estatus = Column(Integer)

    def __init__(self, idUsuario, idPelicula, fechaRenta, dias_de_renta=5, estatus=0):
        self.idUsuario = idUsuario
        self.idPelicula = idPelicula
        self.fechaRenta = fechaRenta
        self.dias_de_renta = dias_de_renta
        self.estatus = estatus

    def __str__(self):
        return f'IdUsuario:{self.idUsuario}\nIdPelicula:{self.idPelicula}\nFecha de Renta:{self.fecha_renta}\nDias de Renta:{self.dias_de_renta}\nEstatus:{self.estatus}'
