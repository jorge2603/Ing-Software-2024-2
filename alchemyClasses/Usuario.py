from sqlalchemy import Integer, String, Column

from alchemyClasses import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200))
    apPat = Column(String(200))
    apMat = Column(String(200))
    password = Column(String(64))
    email = Column(String(500), nullable=True, unique=True)
    profilePicture = Column(String(200), nullable=True)
    superUser = Column(Integer)



    def __init__(self, nombre, apPat, apMat,email,password,superUser,profilePicture=None):
        self.nombre = nombre
        self.ap_pat = apPat
        self.ap_mat = apMat
        self.password = password
        self.email = email
        self.profilePicture = profilePicture
        self.superUser = superUser

    def __str__(self):
        return f'Nombre:{self.nombre}\nApellidos:{self.apPat} {self.apMat}\nEmail:{self.email}\nPassword:{self.password}\nSuperUser:{self.superUser}\nProfilePicture:{self.profilePicture}'