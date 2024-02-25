import pymysql.cursors
from faker import Faker
import random

faker=Faker()

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='lab',
                             password='Developer123!',
                             database='lab_ing_software',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

#CRUD
def insertar_usuario(nombre,apPat,apMat,email,password,tipo):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `usuarios` (`nombre`, `apPat`, `apMat`, `email`, `password`, `superUser`) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (nombre, apPat, apMat, email, password, tipo))
        connection.commit()
    finally:
        connection.close()
def insertar_pelicula(nombre,genero,duracion,inventario):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `peliculas` (`nombre`, `genero`, `duracion`, `inventario`) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (nombre, genero, duracion, inventario))
        connection.commit()
    finally:
        connection.close()

def insertar_renta(idUsuario,idPelicula,fecha_renta,dias_de_renta,estatus):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `rentar` (`idUsuario`, `idPelicula`, `fecha_renta`, `dias_de_renta`, `estatus`) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus))
        connection.commit()
    finally:
        connection.close()
def obtener_usuarios():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `usuarios`"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    finally:
        connection.close()
def obtener_peliculas():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `peliculas`"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    finally:
        connection.close()

def obtener_rentas():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `rentar`"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    finally:
        connection.close()

def actualizar_usuario(idUsuario,nombre,apPat,apMat,email,password,tipo):
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `usuarios` SET `nombre` = %s, `apPat` = %s, `apMat` = %s, `email` = %s, `password` = %s, `superUser` = %s WHERE `idUsuario` = %s"
            cursor.execute(sql, (nombre, apPat, apMat, email, password, tipo, idUsuario))
        connection.commit()
    finally:
        connection.close()
def actualizar_pelicula(idPelicula,nombre,genero,duracion,inventario):
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `peliculas` SET `nombre` = %s, `genero` = %s, `duracion` = %s, `inventario` = %s WHERE `idPelicula` = %s"
            cursor.execute(sql, (nombre, genero, duracion, inventario, idPelicula))
        connection.commit()
    finally:
        connection.close()

def actualizar_renta(idRenta,idUsuario,idPelicula,fecha_renta,dias_de_renta,estatus):
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `rentar` SET `idUsuario` = %s, `idPelicula` = %s, `fecha_renta` = %s, `dias_de_renta` = %s, `estatus` = %s WHERE `idRenta` = %s"
            cursor.execute(sql, (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus, idRenta))
        connection.commit()
    finally:
        connection.close()

def eliminar_usuario(idUsuario):
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `usuarios` WHERE `idUsuario` = %s"
            cursor.execute(sql, (idUsuario))
        connection.commit()
    finally:
        connection.close()

def eliminar_pelicula(idPelicula):
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `peliculas` WHERE `idPelicula` = %s"
            cursor.execute(sql, (idPelicula))
        connection.commit()
    finally:
        connection.close()

def eliminar_renta(idRenta):
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `rentar` WHERE `idRenta` = %s"
            cursor.execute(sql, (idRenta))
        connection.commit()
    finally:
        connection.close()



def obtener_ids(categoria,nombre):
    if categoria=='U':
            with connection.cursor() as cursor:
                sql = "SELECT `idUsuario` FROM `usuarios` WHERE `nombre` = %s"
                cursor.execute(sql, (nombre))
                result = cursor.fetchone()
                return result
    elif categoria=='P':
            with connection.cursor() as cursor:
                sql = "SELECT `idPelicula` FROM `peliculas` WHERE `nombre` = %s"
                cursor.execute(sql, (nombre))
                result = cursor.fetchone()
                return result
    
#Ejercicio 1
def inserta_tablas():
    nombre=faker.first_name()
    apPat=faker.last_name()
    apMat=faker.last_name()
    email=faker.email()
    password=faker.word()
    tipo=random.randint(0,1)
    nombre_pelicula=faker.word()
    genero=faker.word()
    duracion=random.randint(60,180)
    inventario=random.randint(0,100)
    fecha_renta=faker.date()
    dias_renta=random.randint(1,30)
    estatus=random.randint(0,1)

    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `usuarios` (`nombre`, `apPat`, `apMat`, `email`, `password`, `superUser`) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (nombre, apPat, apMat, email, password, tipo))
            #pelicula
            sql2="INSERT INTO `peliculas` (`nombre`, `genero`, `duracion`, `inventario`) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql2, (nombre_pelicula, genero, duracion, inventario))
            connection.commit()
            #rentar
            sql3="INSERT INTO `rentar` (`idUsuario`, `idPelicula`, `fecha_renta`, `dias_de_renta`, `estatus`) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql3, (obtener_ids('U','John')['idUsuario'], obtener_ids('P',"production")['idPelicula'], fecha_renta, dias_renta, estatus))
            connection.commit()
            
    finally:
        connection.close()

#Ejercicio 2
def filtrarappellido(cadena):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `usuarios` WHERE `apPat` LIKE %s or `apMat` LIKE %s"
            cadenaa_buscar = '%'+cadena
            cursor.execute(sql,(cadenaa_buscar,cadenaa_buscar))
            result = cursor.fetchall()
            print(result)
    finally:
        connection.close()

#Ejercicio 3
def cambio_genero(pelicula,genero_anterior,genero_nuevo):
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `peliculas` SET `genero` = %s WHERE `genero` = %s and `nombre` = %s"
            cursor.execute(sql,(genero_nuevo,genero_anterior,pelicula))
        connection.commit()
    finally:
        connection.close()

#Ejercicio 4
def eliminar_rentas_3dias():
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `rentas` WHERE `fecha` <= DATE_SUB(NOW(), INTERVAL 3 DAY)"
            cursor.execute(sql)
        connection.commit()
    finally:
        connection.close()





