import flask 
import sqlalchemy

from alchemyClasses import db

app = flask.Flask(__name__)
from hashlib import sha256
from alchemyClasses.Pelicula import Pelicula
from alchemyClasses.Usuario import Usuario
from alchemyClasses.Renta import Renta 
from alchemyClasses import db
from cryptoUtils.CryptoUtils import cipher
from model.model_Pelicula import *
from model.model_Renta import *
from model.model_Usuario import *

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)
if __name__ == '__main__':
 with app.app_context():
  bandera = True
  while bandera:
    print("Que tabla quieres modificar?")
    print("1. Usuarios")
    print("2. Peliculas")
    print("3. Rentas")
    print("4. Salir")
    respuesta=input()
    if respuesta == "1":
      print("Que quieres hacer con la tabla de usuarios?")
      print("1. Ver los registros")
      print("2. Filtrar los registros por id")
      print("3. Actualizar el nombre del usuario")
      print("4. Eliminar un usuario")
      print("5. Eliminar todos los usuarios")
      print("6. Regresar")
      respuesta2=input()
      if respuesta2 == "1":
        print(muestra_usuarios())
      elif respuesta2 == "2":
        print("Ingresa id del usuario")
        id_usuario = input()
        print(muestra_usuario(id_usuario))
      elif respuesta2 == "3":
        print("Ingresa id del usuario")
        id_usuario = input()
        print("Ingresa el nuevo nombre")
        nombre = input()
        print(actualiza_usuario(id_usuario,nombre))
      elif respuesta2 == "4":
        print("Ingresa id del usuario")
        id_usuario = input()
        print(elimina_usuario(id_usuario))
      elif respuesta2 == "5":
        print(elimina_usuarios())
      elif respuesta2 == "6":
        print("Regresando...")

    elif respuesta == "2":
        print("Que quieres hacer con la tabla de peliculas?")
        print("1. Ver los registros")
        print("2. Filtrar los registros por id")
        print("3. Actualizar el nombre de la pelicula")
        print("4. Eliminar una pelicula")
        print("5. Eliminar todas las peliculas")
        print("6. Regresar")
        respuesta2=input()
        if respuesta2 == "1":
            print(muestra_peliculas())
        elif respuesta2 == "2":
            print("Ingresa id de la pelicula")
            id_pelicula = input()
            print(muestra_pelicula(id_pelicula))
        elif respuesta2 == "3":
            print("Ingresa id de la pelicula")
            id_pelicula = input()
            print("Ingresa el nuevo nombre")
            nombre = input()
            print(actualiza_pelicula(id_pelicula,nombre))
        elif respuesta2 == "4":
            print("Ingresa id de la pelicula")
            id_pelicula = input()
            print(elimina_pelicula(id_pelicula))
        elif respuesta2 == "5":
            print(elimina_peliculas())
        elif respuesta2 == "6":
            print("Regresando...")
    elif respuesta == "3":
        print("Que quieres hacer con la tabla de rentas?")
        print("1. Ver los registros")
        print("2. Filtrar los registros por id")
        print("3. Actualizar la fecha de la renta")
        print("4. Eliminar una renta")
        print("5. Eliminar todas las rentas")
        print("6. Regresar")
        respuesta2=input()
        if respuesta2 == "1":
            print(muestra_rentas())
        elif respuesta2 == "2":
            print("Ingresa id de la renta")
            id_renta = input()
            print(muestra_renta(id_renta))
        elif respuesta2 == "3":
            print("Ingresa id de la renta")
            id_renta = input()
            print("Ingresa la nueva fecha")
            fecha = input()
            print(actualiza_renta(id_renta,fecha))
        elif respuesta2 == "4":
            print("Ingresa id de la renta")
            id_renta = input()
            print(elimina_renta(id_renta))
        elif respuesta2 == "5":
            print(elimina_rentas())
        elif respuesta2 == "6":
            print("Regresando...")
    elif respuesta == "4":
        bandera = False
        print("Saliendo...")
    else:
       print("Opcion no valida")


