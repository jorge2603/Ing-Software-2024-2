from flask import Flask, render_template

from alchemyClasses import db
from contollers.PrimerControlador import mi_primer_blueprint
from contollers.ControllerUsuario import usuario_blueprint

from contollers.ControllerPeliculas import pelicula_blueprint
from models.model_Pelicula import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)


app.register_blueprint(mi_primer_blueprint)
app.register_blueprint(pelicula_blueprint)
app.register_blueprint(usuario_blueprint)

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        print(muestra_peliculas())
    app.run()
