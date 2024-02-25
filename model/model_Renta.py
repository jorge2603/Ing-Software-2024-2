from alchemyClasses import db
from alchemyClasses.Renta import Renta

def muestra_rentas():
    return Renta.query.all()

def muestra_renta(id_renta):
    return Renta.query.filter(Renta.idRentar == id_renta).first()

def actualiza_renta(id_renta,fecha_renta):
    renta = Renta.query.filter(Renta.idRentar == id_renta).first()
    renta.fecha_renta = fecha_renta
    db.session.commit()
    return "Operacion exitosa"

def elimina_renta(id_renta):
    renta = Renta.query.filter(Renta.idRentar == id_renta).first()
    db.session.delete(renta)
    db.session.commit()
    return "Operacion exitosa"

def elimina_rentas():
    for renta in Renta.query.all():
        db.session.delete(renta)
    db.session.commit()
    return "Operacion exitosa"
